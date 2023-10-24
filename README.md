# Pulumi Playground with Go

## Setup with Localstack

### Prerequisites

#### CLI's
```
$ brew install pulumi/tap/pulumi
$ brew install go

$ brew install docker
$ brew install minikube
$ brew install localstack
```

#### Local AWS

```
$ localstack start -d

$ export AWS_ACCESS_KEY_ID="test"
$ export AWS_SECRET_ACCESS_KEY="test"
$ export AWS_DEFAULT_REGION="us-east-1"

$ aws --endpoint-url=http://localhost:4566 kinesis list-streams

$ aws configure --profile localstack
$ export AWS_PROFILE=localstack

# To stop localstack
$ localstack stop
```

#### Local Minikube

```
$ minikube addons enable volumesnapshots
$ minikube addons enable csi-hostpath-driver

$ minikube start --nodes=5
$ minikube status

# To stop minikube
$ minikube stop
```

#### Remote Minikube

If you have a spare machine lying around (running a flavor of mac or linux), these instructions should help you use it as your kubernetes cluster.

[Instructions to setup remote Minikube](https://github.com/maxjerin/kubernetes-playground/blob/main/Minikube.md)

##### Known issues

* `port-forwarding` does not seem to work when accessing the cluster remotely.

## References

## Drop-in replacement for AWS CLI
https://docs.localstack.cloud/user-guide/integrations/aws-cli/#localstack-aws-cli-awslocal

## Drop-in replacement for Pulum CLI
https://docs.localstack.cloud/user-guide/integrations/pulumi/
