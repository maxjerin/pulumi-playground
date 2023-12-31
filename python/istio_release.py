import pulumi
from pulumi_kubernetes.core.v1 import Namespace
from pulumi_kubernetes.helm.v3 import Release, ReleaseArgs, RepositoryOptsArgs
from istio_constants import ISTIO_REPO_URL, ISTIO_VERSION

def istio_pulumi_release():
    ns_istio_system_name = 'istio-system'
    ns_istio_ingress_name = 'istio-ingress'

    # Create a Namespace for the EKS cluster
    ns_istio_system = Namespace(ns_istio_system_name, metadata={"name": ns_istio_system_name})
    ns_istio_ingress = Namespace(
         ns_istio_ingress_name,
         metadata={
              "name": ns_istio_ingress_name,
              "labels": {
                   "istio-injection": "enabled"
                }
            }
        )

    istio_base = Release(
         "istio-base",
         ReleaseArgs(
              chart="base",
              version=ISTIO_VERSION,
              namespace=ns_istio_system.metadata["name"],
            #   create_namespace=False,
              repository_opts=RepositoryOptsArgs(
                   repo=ISTIO_REPO_URL
                ),
              skip_await=False
              ),
        opts=pulumi.ResourceOptions(depends_on=[ns_istio_system])
    )

    istiod = Release(
         "istiod",
         ReleaseArgs(
              chart="istiod",
              version=ISTIO_VERSION,
              namespace=ns_istio_system.metadata["name"],
            #   create_namespace=False,
              repository_opts=RepositoryOptsArgs(
                   repo=ISTIO_REPO_URL
                ),
              skip_await=False
              ),
        opts=pulumi.ResourceOptions(depends_on=[ns_istio_system, istio_base])
    )

    istiod_ingress = Release(
         "istio-ingress",
         ReleaseArgs(
              chart="gateway",
              version=ISTIO_VERSION,
              namespace=ns_istio_ingress.metadata["name"],
              repository_opts=RepositoryOptsArgs(
                   repo=ISTIO_REPO_URL
                ),
              skip_await=False
              ),
        opts=pulumi.ResourceOptions(depends_on=[ns_istio_ingress])
    )
