

## This is a sample FastAPI Repo that can be Dockerized to run in the cloud.

It was built as a tutorial to get a simple Python API up and running on AWS ECS Fargate.

**IMPORTANT:** Don't run this as is in production.

**To run on ECS Fargate, do the following:**

1. Create a repository on DockerHub.
2. In your CLI (at the root of the project), run:
```sh
poetry install
```
   You should now be able to run the API locally with:
```sh
poetry run python backend/main.py
```
   and see `{"Hello":"World"}` at [http://localhost:8001/](http://localhost:8001/).

3. To build the container, run:

```sh
docker build -t fastapi_fargate .
```

4. Tag the container with:

```sh
docker tag fastapi_fargate:latest <Your_DockerHub_Username>/<Your_DockerHub_RepositoryName>:latest
```

   and push with:

```sh
docker push <DockerHub_Username>/<DockerHub_RepositoryName>:latest
```

5. In AWS, create an IAM role with permissions `SecretsManagerReadWrite` and `AmazonECSTaskExecutionRolePolicy`.
6. Go to AWS Secrets Manager and create a secret with key-value pairs for "username" and "password". Username is your Docker username, and the password is an access token that you can create at [DockerHub Security](https://hub.docker.com/settings/security).
7. Under ECS, create a cluster and then create a Task Definition. Select your IAM role you just created under Task Roles.
8. Under Container Details, use `docker.io/<Your_DockerHub_Username>/<Your_DockerHub_RepositoryName>:latest`, select Private registry authentication, and use the Secrets Manager ARN that you created in step 6.
9. Create your service in your ECS cluster with the Task Definition you just created.
10. Once your service is up and running, click into your service, go to the Networking tab, and go to the attached security group. Under inbound rules, add port 80 with source `0.0.0.0/0`.

You should see `{"Hello":"World"}` if you go to the running task in ECS and visit the public IP address in your browser.
