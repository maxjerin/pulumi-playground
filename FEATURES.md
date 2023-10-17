# Targetted State Create/Update/Destroy

> ?

# State Move

> ?
* [ ] Create another stack (stack2) that uses localstack.
* [ ] Point stack2 to stack1 resources.
* [ ] Migrate code from an exsiting stack (stack1) to stack2.
* [ ] Migrate state from stack2 to stack1.
* [ ] Run `pulumi preview` to validate pulumi sees the resources.

# Refresh State from Existing Resource

> ?
* [ ] Manually create buckets on localstack.
* [ ] Add pulumi code that creates the same bucket but do not run it.
* [ ] Run `pulumi preview` and verify that pulumi does not inteded to create anything.

OR

* [ ] Check if pulumi has any command to translate existing resources into pulumi state.

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
