package main

import (
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	"github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create an AWS resource (S3 Bucket)
		bucket, err := s3.NewBucket(ctx, "my-bucket", nil)
		if err != nil {
			return err
		}

		ns, err := corev1.NewNamespace(ctx, "istio-system", &corev1.NamespaceArgs{
			Metadata: metav1.ObjectMetaArgs{
				Name: pulumi.String("istio-system"),
			},
		})
		if err != nil {
			return err
		}

		istiobase, err := helm.NewChart(ctx, "istio-base", helm.ChartArgs{
			Chart:   pulumi.String("base"),
			Version: pulumi.String("1.19.3"),
			FetchArgs: helm.FetchArgs{
				Repo: pulumi.String("https://istio-release.storage.googleapis.com/charts"),
			},
		}, pulumi.DependsOn([]pulumi.Resource{ns}))
		if err != nil {
			return err
		}

		istiod, err := helm.NewChart(ctx, "istiod", helm.ChartArgs{
			Chart:   pulumi.String("istiod"),
			Version: pulumi.String("1.19.3"),
			FetchArgs: helm.FetchArgs{
				Repo: pulumi.String("https://istio-release.storage.googleapis.com/charts"),
			},
		}, pulumi.DependsOn([]pulumi.Resource{ns}))
		if err != nil {
			return err
		}

		// Export the name of the bucket
		ctx.Export("bucketName", bucket.ID())
		ctx.Export("chart", istiobase.URN())
		ctx.Export("chart", istiod.URN())
		ctx.Export("namespace", ns.URN())
		return nil
	})
}
