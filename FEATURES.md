# Targetted State Create/Update/Destroy

> ?

# State Move

> ?

# Refresh State from Existing Resource

> ?


# State Backends

## Local storage

```
$> pulumilocal logout
$> pulumilocal login --local
```

## AWS S3

```
pulumi login 's3://<bucket-name>?region=us-east-1&awssdk=v2&profile=localstack'
```

# State Operations

```
pulumi stack -u -i

Enter your passphrase to unlock config/secrets
    (set PULUMI_CONFIG_PASSPHRASE or PULUMI_CONFIG_PASSPHRASE_FILE to remember):
Enter your passphrase to unlock config/secrets
Current stack is localstack:
    Managed by Anilas-Laptop
    Last updated: 29 minutes ago (2023-10-12 23:23:24.259369 -0400 EDT)
    Pulumi version used: v3.88.1
Current stack resources (3):
    TYPE                     NAME
    pulumi:pulumi:Stack      pulumi-playground-localstack
    │  URN: urn:pulumi:localstack::pulumi-playground::pulumi:pulumi:Stack::pulumi-playground-localstack
    ├─ aws:s3/bucket:Bucket  my-bucket
    │     URN: urn:pulumi:localstack::pulumi-playground::aws:s3/bucket:Bucket::my-bucket
    │     ID: my-bucket-f6e6ff0
    └─ pulumi:providers:aws  default
          URN: urn:pulumi:localstack::pulumi-playground::pulumi:providers:aws::default
          ID: 65da9c7d-8e2c-4b37-92b2-9a1bedc83342

Current stack outputs (1):
    OUTPUT      VALUE
    bucketName  my-bucket-f6e6ff0

Use `pulumi stack select` to change stack; `pulumi stack ls` lists known ones
```
