"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3
from pulumi_kubernetes.core.v1 import Namespace
from pulumi_eks import Cluster
from pulumi_kubernetes.helm.v3 import Chart, ChartOpts

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket')

namespace_name = 'istio-system'

# Create a Namespace for the EKS cluster
ns = Namespace(namespace_name,
               metadata={"name": namespace_name},
)

# Install a Helm Chart from a remote repo into the namespace that was created above.
istio_base = Chart('istio-base',
                 config=ChartOpts(
                     chart='base',
                     fetch_opts={
                         "repo": "https://istio-release.storage.googleapis.com/charts"
                     },
                     version='1.19.3',
                 ),
                 opts=pulumi.ResourceOptions(depends_on=[ns]))


istio_base = Chart('istiod',
                 config=ChartOpts(
                     chart='istiod',
                     fetch_opts={
                         "repo": "https://istio-release.storage.googleapis.com/charts"
                     },
                     version='1.19.3',
                 ),
                 opts=pulumi.ResourceOptions(depends_on=[ns]))

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
