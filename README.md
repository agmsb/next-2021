# next-2021

## Setup

Create Cloud Build Trigger for builds. 

```
gcloud beta builds triggers create development-trigger \
    --repo-name=next-2021 \
    --repo-owner=agmsb \
    --branch-pattern=development \ 
    --build-config=buid/build.yaml \
    --service-account=build-next-2021@agmsb-k8s.iam.gserviceaccount.com 
```
