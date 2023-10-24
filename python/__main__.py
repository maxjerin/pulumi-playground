"""An AWS Python Pulumi program"""

from istio_chart import istio_pulumi_chart
from istio_release import istio_pulumi_release

# istio_pulumi_release()
istio_pulumi_chart()
