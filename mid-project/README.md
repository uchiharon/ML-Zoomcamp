# House Price Prediction

## Project Description

This project develops a machine learning model to accurately forecast house prices using a comprehensive dataset of residential properties in Ames, Iowa. It empowers home buyers to make informed decisions, assists real estate agents, guides property developers, and supports financial institutions in their respective domains.

## Problem Statement

Traditionally, house price estimations have relied on subjective appraisals and market trends, which can be time-consuming, inconsistent, and prone to bias. This project addresses this issue by employing a machine learning model that analyzes a vast amount of data to identify patterns and predict house prices with greater accuracy.

## Project Benefits

* **Empowered Home Buyers:** Accurate house price predictions enable buyers to make informed decisions, ensuring they purchase properties at fair market value.

* **Enhanced Real Estate Services:** Equipped with reliable price forecasts, real estate agents can provide better guidance to their clients, enhancing their credibility and customer satisfaction.

* **Data-Driven Property Development:** By understanding the factors that influence house prices, developers can make informed decisions regarding property design, location, and pricing strategies.

* **Risk-Managed Financial Decisions:** Accurate house price assessments are essential for mortgage lending and risk management in financial institutions.

## Stakeholders

* **Individual Home Buyers:** Seeking to purchase a home and make informed decisions about property values.

* **Real Estate Agents:** Assisting clients in buying and selling homes, providing market insights and property valuations.

* **Property Developers:** Designing, constructing, and selling residential properties, aiming to maximize profits and meet market demand.

* **Financial Institutions:** Assessing creditworthiness of potential borrowers, evaluating property values, and managing mortgage risk.

## Future Work

* **Feature Engineering:** Explore additional features that could enhance the model's predictive power, such as neighborhood characteristics, amenities, and proximity to public transportation.

* **Model Selection and Optimization:** Experiment with different machine learning algorithms and optimize hyperparameters to improve the model's accuracy and generalizability.

* **Data Preprocessing:** Refine data cleaning and handling techniques to ensure data quality and consistency.

## Contributions

We welcome contributions from anyone interested in improving the project and advancing the field of house price prediction. Please feel free to propose enhancements, suggest new features, or share your expertise in machine learning and data analysis.

## Additional Information

* The current model achieves a score of 0.14 on Kaggle, indicating room for improvement.

* The model is trained on a dataset of over 79 explanatory variables covering various aspects of residential properties in Ames, Iowa.

* The project utilizes various machine learning techniques, including data preprocessing, feature engineering, model selection, and hyperparameter optimization.









## Prerequisites

* Python 3.x
* pipenv
* Requests library



## Testing Instructions

1. **Fork the Repository:**

Navigate to the repository containing the model and click the "Fork" button in the top-right corner. This will create a copy of the repository under your GitHub account.

2. **Clone the Forked Repository:**

Clone the forked repository to your local machine using the following command:

```bash
git clone <URL_OF_FORKED_REPOSITORY>











waitress-serve --listen=localhost:9696 prediction:app

pipenv install scikit-learn==1.3.0 numpy pandas flask

To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.

gcloud auth login {Then sign it from your browser} (link)[https://cloud.google.com/sdk/gcloud/reference/auth/login]

net localgroup docker-users DOMAIN\USERNAME /add (link)


docker tag house-price gcr.io/climate-team-1/house-pricing
docker push gcr.io/climate-team-1/house-pricing



Select the image from cloud registry
Set the port through which request would be sent to the container
Select vCPU to 1
Set CPU allocation and pricing to 'CPU is Only allocated during request processing'
Reduce maximum number of instances to 4 to reduce cost, as well as prevent downtime


# Deploying a Dockerized Application to GCP Cloud Run

## Prerequisites

1. Docker installed on your local machine
2. GCP project with Cloud Run enabled
3. Docker image of your application built and pushed to Google Container Registry (GCR)

## Steps

### 1. Create a Cloud Run service

1. Go to the Cloud Run console in the GCP Console.
2. Click on the "Create Service" button.
3. Enter a name for your service.
4. Select the "Region" where you want to deploy your service.
5. Under "Container Image", select "Container registry" and then choose your Docker image from GCR.
6. Under "Container Port", enter the port through which requests will be sent to the container.
7. Under "Machine resources", select "1 vCPU".
8. Under "CPU allocation and pricing", select "CPU is only allocated during request processing".
9. Under "Maximum number of instances", enter "4".
10. Click on the "Create" button.

### 2. Verify your service

Once your service is created, it will be listed in the Cloud Run console. You can click on the service name to view its details, including its URL.

To test your service, open a web browser and navigate to the URL of your service. You should see a message indicating that your application is running.

## Tips

* To reduce costs, you can set a lower maximum number of instances. However, this may result in downtime if your application receives a sudden surge in traffic.
* You can also use the Cloud Run API or the gcloud command-line tool to create and manage Cloud Run services.

## Additional Resources

* [Cloud Run documentation](https://cloud.google.com/run/docs/)
* [GCR documentation](https://cloud.google.com/container-registry/docs/)






# Uploading a Docker Image to GCP Artifact Repository

## Prerequisites

- Docker installed on your local machine
- GCP project with Artifact Registry enabled
- Service account credentials with Artifact Registry access

## Steps

1. **Authenticate Docker with your GCP project:**

```bash
gcloud auth configure-docker


2. **Create a Docker image:**

Build your application into a Docker image following your project's specific build instructions. This will create a Docker image file (e.g., `my-image.tar`) on your local machine.

3. **Tag the Docker image with the Artifact Registry repository URL:**

bash
docker tag my-image gcr.io/<PROJECT_ID>/artifact-repository/<REPOSITORY_NAME>/<IMAGE_TAG>


Replace `<PROJECT_ID>` with your GCP project ID, `<REPOSITORY_NAME>` with the name of your Artifact Registry repository, and `<IMAGE_TAG>` with the desired tag for your image.

4. **Push the tagged Docker image to the Artifact Registry repository:**

bash
docker push gcr.io/<PROJECT_ID>/artifact-repository/<REPOSITORY_NAME>


Replace `<PROJECT_ID>`, `<REPOSITORY_NAME>`, and `<IMAGE_TAG>` with the appropriate values. This will push the Docker image to your Artifact Registry repository.

## Verification

1. **Verify the image in the Artifact Registry repository:**

bash
gcloud artifacts repositories list


This will list all the Artifact Registry repositories in your project. Identify the repository where you pushed your image.

2. **Verify the image details:**

bash
gcloud artifacts repositories list tags <REPOSITORY_NAME>


Replace `<REPOSITORY_NAME>` with the name of your Artifact Registry repository. This will list all the tags associated with the repository, including the tag you used when pushing your image.

3. **Pull the image from the Artifact Registry repository:**

bash
docker pull gcr.io/<PROJECT_ID>/artifact-repository/<REPOSITORY_NAME>/<IMAGE_TAG>


Replace `<PROJECT_ID>`, `<REPOSITORY_NAME>`, and `<IMAGE_TAG>` with the appropriate values. This will pull the Docker image from the Artifact Registry repository to your local machine.
