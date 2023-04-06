# Flask webapp with Jenkins CI/CD pipeline

This repository contains a simple Flask web application with a Jenkins CI/CD pipeline. The pipeline builds, tests, and deploys the application using Docker.

## Prerequisites

Before you begin, ensure you have the following installed and configured:

1. Python (version 3.8 or higher): https://www.python.org/downloads/
2. Docker: https://docs.docker.com/get-docker/
3. Jenkins: https://www.jenkins.io/doc/book/installing/
4. Jenkins plugins:
   - Git plugin: Provides Git support in Jenkins.
   - Pipeline plugin: Enables the use of Jenkins Pipelines.
   - Docker Pipeline plugin: Adds Docker-related functionality to Jenkins Pipelines.

## Setting Up the Jenkins CI/CD Pipeline

Follow these steps to set up the Jenkins CI/CD pipeline for this project:

1. Clone this repository to your local machine:

```bash
git clone git@github.com:lexivanx/webapp-cicd-flask.git
cd webapp-cicd-flask
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Ensure the necessary Jenkins plugins are installed (see Prerequisites).

4. Create a new Jenkins Pipeline project:
   - In Jenkins, click on "New Item".
   - Enter a name for the project, choose "Pipeline", and click "OK".
   - Under "Pipeline", choose "Pipeline script from SCM" for the "Definition" field.
   - Choose "Git" for the "SCM" field, and enter your repository URL in the "Repository URL" field.
   - Set the "Script Path" field to "Jenkinsfile" (without quotes), which is the path to the Jenkinsfile in this repository.
   - Click "Save".

## Using the Jenkins CI/CD Pipeline

Once the Jenkins CI/CD pipeline is set up, it will automatically build, test, and deploy your Flask application whenever you push changes to the repository. The pipeline has three stages:

1. Build: Compiles the application (if necessary) and creates a Docker image.
2. Test: Runs the unit tests for the application.
3. Deploy: Deploys the application to a target environment (e.g., staging or production).

To manually trigger the pipeline, go to your Jenkins project, and click "Build Now". You can view the pipeline's progress and logs in the "Build History" section.
