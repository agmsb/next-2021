# next-2021

## Setup

Create Cloud Build Trigger for builds. 

```
gcloud beta builds triggers create github \
    --repo-name=next-2021 \
    --repo-owner=agmsb \
    --branch-pattern=development \
    --build-config=build/build.yaml \
    --service-account=build-next-2021@agmsb-k8s.iam.gserviceaccount.com
```
Create Cloud Build Trigger for deploys. 

```
gcloud beta builds triggers create github \
    --repo-name=next-2021 \
    --repo-owner=agmsb \
    --branch-pattern=main \
    --build-config=build/deploy.yaml \
    --require-approval \
    --service-account=deploy-next-2021@agmsb-k8s.iam.gserviceaccount.com
```
