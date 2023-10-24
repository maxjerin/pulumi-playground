Pulumi Playground with Go

# Setup with Localstack

## Prerequisites

#### CLI's
```
$> brew install pulumi/tap/pulumi
$> pip install pulumi-local
$> brew install go

$> brew install docker
$> brew install localstack
$> localstack start -d

$> localstack stop
```

#### Local AWS

```
$ export AWS_ACCESS_KEY_ID="test"
$ export AWS_SECRET_ACCESS_KEY="test"
$ export AWS_DEFAULT_REGION="us-east-1"

$ aws --endpoint-url=http://localhost:4566 kinesis list-streams

$ aws configure --profile localstack
$ export AWS_PROFILE=localstack
```

#### Local Minikube

```
$ minikube addons enable volumesnapshots
$ minikube addons enable csi-hostpath-driver

$ minikube start --nodes=3 --memory=4096
```

#### Remote Minikube

Refer to [these instructions](https://github.com/maxjerin/kubernetes-playground/blob/main/Minikube.md)

## Init Pulumi Project

```
mkdir <pulumi-project-folder> && cd <pulumi-project-folder>
$> pulumilocal new aws-go
$> pulumilocal config set aws:profile localstack
$> pulumilocal preview
```

# References

## Drop-in replacement for AWS CLI
https://docs.localstack.cloud/user-guide/integrations/aws-cli/#localstack-aws-cli-awslocal

## Drop-in replacement for Pulum CLI
https://docs.localstack.cloud/user-guide/integrations/pulumi/
