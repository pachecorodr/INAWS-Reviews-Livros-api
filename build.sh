ECR_REGISTRY="992382503552.dkr.ecr.us-east-1.amazonaws.com"
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 992382503552.dkr.ecr.us-east-1.amazonaws.com
docker build -t reviewlivros/backend .
docker tag reviewlivros/backend:latest $ECR_REGISTRY/reviewlivros/backend:latest
docker push $ECR_REGISTRY/reviewlivros/backend:latest