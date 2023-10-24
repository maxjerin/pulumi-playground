# Pulimi Python Implementation

## Pre-requisite

Python venv should get created when using `pulumi init`. If it does not, then a lot of other things won't work.
```
# This should create python venv
pulimi-playground/python $ pulumi init
```

# Dependency Management

## Save dependencies

`./venv/bin/pip freeze > requirements.txt`

## Install dependencies to Pulumi venv

`./venv/bin/pip pulumi-kubernetes==3.30.2   `
