# Duplicate Values

## Error
` error: pulumi:providers:aws resource 'default' has a problem: could not validate provider configuration: Duplicate Set Element. This attribute contains duplicate values of`

## Cause

Running `pulumilocal` creates duplicate entries in `Pulumi.<stack>.yaml` and since it adds entries in yaml list format, it does not overwrite older entries.

## Resolution

Delete all entries and only keep the one you need

# S3 Style Path Provider Config

## Error

`error: pulumi:providers:aws resource 'default' has a problem: could not validate provider configuration: Invalid or unknown key. Check pulumi config get aws:s3ForcePathStyle.`

## Cause

This `aws:s3ForcePathStyle` aws provider config added by `pulumilocal` into  `Pulumi.<stack>.yaml` is not compatible with `pulumi` cli.

## Resolution

Remove it and save the yaml file.
