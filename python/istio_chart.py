import pulumi
from pulumi_kubernetes.core.v1 import Namespace
from pulumi_kubernetes.helm.v3 import Chart, ChartOpts

def istio_pulumi_chart():
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

    # Install a Helm Chart from a remote repo into the namespace that was created above.
    istio_base = Chart('istio-base',
                    config=ChartOpts(
                        chart='base',
                        namespace=ns_istio_system.metadata["name"],
                        fetch_opts={
                            "repo": "https://istio-release.storage.googleapis.com/charts"
                        },
                        values={
                            "defaultRevision": "default",
                        },
                        version='1.19.3',
                    ),
                    opts=pulumi.ResourceOptions(depends_on=[ns_istio_system])
                )

    istiod = Chart('istiod',
                    config=ChartOpts(
                        chart='istiod',
                        namespace=ns_istio_system.metadata["name"],
                        fetch_opts={
                            "repo": "https://istio-release.storage.googleapis.com/charts"
                        },
                        version='1.19.3',
                    ),
                    opts=pulumi.ResourceOptions(depends_on=[istio_base, ns_istio_system])
                )

    istio_ingress = Chart('istio-ingress',
                        config=ChartOpts(
                            chart='gateway',
                            namespace=ns_istio_ingress.metadata["name"],
                            fetch_opts={
                                "repo": "https://istio-release.storage.googleapis.com/charts"
                            },
                            version='1.19.3',
                        ),
                        opts=pulumi.ResourceOptions(depends_on=[istio_base, ns_istio_ingress])
                    )
