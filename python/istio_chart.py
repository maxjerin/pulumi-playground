import pulumi
import pulumi_kubernetes
from pulumi_kubernetes.core.v1 import Namespace, NamespacePatch
from pulumi_kubernetes.helm.v3 import Chart, ChartOpts
from istio_constants import ISTIO_REPO_URL, ISTIO_VERSION

def get_namespace(name):
    try:
        return pulumi_kubernetes.core.v1.Namespace.get(name, name)
    except:
        return None



def enable_istio_sidecar_injection(namespace):
    ns = get_or_create_namespace(namespace)

    NamespacePatch(
        resource_name = f'patch-{namespace}',
        metadata={
            "name": ns.metadata["name"],
            "labels": {
                "istio-injection": "enabled"
                }
            }
        )

def get_or_create_namespace(namespace):
    ns = get_namespace(namespace)
    if ns is None:
        ns = Namespace(namespace, metadata={
            "name": namespace
        })

    return ns


def istio_pulumi_chart():
    ns_istio_system_name = 'istio-system'
    ns_istio_ingress_name = 'istio-ingress'

    # Create a Namespace for the Istio
    ns_istio_system = get_or_create_namespace(ns_istio_system_name)
    ns_istio_ingress = get_or_create_namespace(ns_istio_ingress_name)

    # Enable sidecar injection into default namespace
    sidecar_enabled_namespace = ['default', 'secondary']
    for ns in sidecar_enabled_namespace: enable_istio_sidecar_injection(ns)

    # Install a Helm Chart from a remote repo into the namespace that was created above.
    istio_base = Chart('istio-base',
                    config=ChartOpts(
                        chart='base',
                        namespace=ns_istio_system.metadata["name"],
                        fetch_opts={
                            "repo": ISTIO_REPO_URL
                        },
                        values={
                            "defaultRevision": "default",
                        },
                        version=ISTIO_VERSION,
                    ),
                    opts=pulumi.ResourceOptions(depends_on=[ns_istio_system])
                )

    Chart('istiod',
        config=ChartOpts(
            chart='istiod',
            namespace=ns_istio_system.metadata["name"],
            fetch_opts={
                "repo": ISTIO_REPO_URL
            },
            version=ISTIO_VERSION,
        ),
        opts=pulumi.ResourceOptions(depends_on=[istio_base, ns_istio_system])
    )

    Chart('istio-ingress',
        config=ChartOpts(
            chart='gateway',
            namespace=ns_istio_ingress.metadata["name"],
            fetch_opts={
                "repo": ISTIO_REPO_URL
            },
            version=ISTIO_VERSION,
        ),
        opts=pulumi.ResourceOptions(depends_on=[istio_base, ns_istio_ingress])
    )
