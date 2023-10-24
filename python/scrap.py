import os
import pulumi
from pulumi_aws import s3
from pulumi_kubernetes import Provider
import pulumi_kubernetes as k8s
from pulumi_kubernetes.helm.v3 import Chart, ChartOpts

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket')

# Assumes you have a 'kubeconfig.json' file in the same directory.
kubeconfig_file_path = "/Users/maxjerin/.kube/minikube-config"

# Make sure that the kubeconfig file exists
assert os.path.isfile(kubeconfig_file_path), f"'{kubeconfig_file_path}' file not found"

# Read the kubeconfig file
with open(kubeconfig_file_path, 'r') as kubeconfig_file:
    kubeconfig_str = kubeconfig_file.read().strip()

# Create a provider using the kubeconfig string
k8s_provider = Provider('k8sProvider', kubeconfig=kubeconfig_str)

# Exporting the cluster name
pulumi.export('clusterName', k8s_provider.id)

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

def get_namespace(name):
        return k8s.core.v1.Namespace.get(name, name)

existing_namespace = get_namespace("kube-system")
istio_cni = Chart('istiocni',
                    config=ChartOpts(
                        chart='cni',
                        namespace=existing_namespace.metadata["name"],
                        fetch_opts={
                            "repo": "https://istio-release.storage.googleapis.com/charts"
                        },
                        version='1.19.3',
                    ),
                    opts=pulumi.ResourceOptions(depends_on=[istio_base])
            )
