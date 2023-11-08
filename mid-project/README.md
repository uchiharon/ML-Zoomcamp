# House Price Prediction

## Project Description

This project develops a machine learning model to accurately forecast house prices using a comprehensive dataset of residential properties in Ames, Iowa. It empowers home buyers to make informed decisions, assists real estate agents, guides property developers, and supports financial institutions in their respective domains.

### Problem Statement

Traditionally, house price estimations have relied on subjective appraisals and market trends, which can be time-consuming, inconsistent, and prone to bias. This project addresses this issue by employing a machine learning model that analyzes a vast amount of data to identify patterns and predict house prices with greater accuracy.

### Project Benefits

* **Empowered Home Buyers:** Accurate house price predictions enable buyers to make informed decisions, ensuring they purchase properties at fair market value.

* **Enhanced Real Estate Services:** Equipped with reliable price forecasts, real estate agents can provide better guidance to their clients, enhancing their credibility and customer satisfaction.

* **Data-Driven Property Development:** By understanding the factors that influence house prices, developers can make informed decisions regarding property design, location, and pricing strategies.

* **Risk-Managed Financial Decisions:** Accurate house price assessments are essential for mortgage lending and risk management in financial institutions.

### Stakeholders

* **Individual Home Buyers:** Seeking to purchase a home and make informed decisions about property values.

* **Real Estate Agents:** Assisting clients in buying and selling homes, providing market insights and property valuations.

* **Property Developers:** Designing, constructing, and selling residential properties, aiming to maximize profits and meet market demand.

* **Financial Institutions:** Assessing creditworthiness of potential borrowers, evaluating property values, and managing mortgage risk.

### Future Work

* **Feature Engineering:** Explore additional features that could enhance the model's predictive power, such as neighborhood characteristics, amenities, and proximity to public transportation.

* **Model Selection and Optimization:** Experiment with different machine learning algorithms and optimize hyperparameters to improve the model's accuracy and generalizability.

* **Data Preprocessing:** Refine data cleaning and handling techniques to ensure data quality and consistency.

### Contributions

I welcome contributions from anyone interested in improving the project and advancing the field of house price prediction. Please feel free to propose enhancements, suggest new features, or share your expertise in machine learning and data analysis.

### Additional Information

* The current model achieves a score of 0.14 on Kaggle, indicating room for improvement.

* The model is trained on a dataset of over 79 explanatory variables covering various aspects of residential properties in Ames, Iowa.

* The project utilizes various machine learning techniques, including data preprocessing, feature engineering, model selection, and hyperparameter optimization.




## Prerequisites

This project requires the following prerequisites:

* Python 3.x
  * Download: https://www.python.org/downloads/
* Docker
  * Setup Guide: https://docs.docker.com/get-docker/
* Google Cloud Platform (GCP) account
  * Create an account: https://support.google.com/accounts/answer/27441?hl=en
* Cloud Run
  * Enable API: https://cloud.google.com/api-gateway/docs/get-started-cloud-run
* Artifact Registry
  * Enable API: https://cloud.google.com/artifact-registry/docs/enable-service
* pipenv
  * Installation: https://codingpub.dev/python-pip3-pipenv/

### Additional Notes

* Ensure you have the necessary permissions to use the required resources in your GCP project.
* Adjust the installation instructions based on your specific environment.
* Refer to the official documentation for the relevant software or services if you encounter any issues.




## Testing Instructions

1. **Fork the Repository:**

Navigate to the repository containing the model and click the "Fork" button in the top-right corner. This will create a copy of the repository under your GitHub account.

2. **Clone the Forked Repository:**

Clone the forked repository to your local machine using the following command:

```bash
git clone <URL_OF_FORKED_REPOSITORY>
```

3. **Set Up the Virtual Environment:**
```
Bash
cd house-price-prediction
pipenv install
```

4. **Activate the Virtual Environment:**
```
Bash
pipenv shell
```

5. **Run the Prediction Test Script:**
```
Bash
python predict_test.py
```


This will send the JSON data in the `predict_test.py` file to the model endpoint and display the predicted house price.

6. **Modify the JSON Data:**

You can modify the JSON data in the `predict_test.py` file to test different property details and observe the corresponding predicted house prices.

## JSON Data Format

The JSON payload should contain the following property details:

* `Id`: Unique identifier for the property
* `MSSubClass`: Zoning classification (e.g., 20, 30, 40)
* `MSZoning`: Residential zoning (e.g., A, C, I, RL)
* `LotFrontage`: Width of the property in feet
* `LotArea`: Area of the property in square feet
* `Street`: Type of street (e.g., Pave, Grvl)
* `Alley`: Type of access to the property (e.g., Pos, Neg, NA)
* `LotShape`: Shape of the property (e.g., Reg, IRreg)
* `LandContour`: Slope of the property (e.g., Bkg, Lev, Slw)
* `Utilities`: Utility services available (e.g., AllPub, NoSewr)
* `LotConfig`: Configuration of the property (e.g., Inside, Corner, Cul-de-sac)
* `LandSlope`: Slope of the land (e.g., Gtl, Mod, Sev)
* `Neighborhood`: Neighborhood where the property is located
* `Condition1`: Overall condition of the property exterior (e.g., Norm, Remod, Dilap)
* `Condition2`: Overall condition of the property basement (e.g., Norm, Remod, Dilap)
* `BldgType`: Type of building (e.g., 1Fam, 2Fam, Twnhouse)
* `HouseStyle`: Architectural style of the house (e.g., 1Story, 2Story, 1.5Story)
* `OverallQual`: Overall quality of the property (1 - 10 scale)
* `OverallCond`: Overall condition of the property (1 - 9 scale)
* `YearBuilt`: Year the property was originally built
* `YearRemodAdd`: Year the property was remodeled or added to
* `RoofStyle`: Style of the roof (e.g., Gable, Hip, Mansard)
* `RoofMatl`: Material of the roof (e.g., CompShg, Metal, WoodShg)
* `Exterior1st`: Exterior material on the first floor (e.g., VinylSd, WoodSd, CemntBd)
* `Exterior2nd`: Exterior material on the second floor (e.g., VinylSd, WoodSd, CemntBd)
* `MasVnrType`: Type of masonry veneer (e.g., BrkFace, Stone, None)
* `MasVnrArea`: Area of masonry veneer in square feet
* `ExterQual`: Exterior quality (e.g., Ex, Gd, TA)
* `ExterCond`: Exterior condition (e.g., Ex, Gd, TA)
* `Foundation`: Type of foundation (e.g., PConc, CBlock, Craw)
* `BsmtQual`: Quality of the basement (e.g., Ex, Gd, TA, NA)





### Testing With Docker

1. **Build Docker file:**

Use `docker build -t house-predict` 

2. **Run the Docker Image:**

Use `winpty docker run -it --rm -p 9696:9696 house-pricing`

3. **Run the Prediction Test Script:**
```
Bash
python predict_test.py
```



# Deploying a Dockerized Application to GCP Cloud Run

For this Project, I choosed cloud run because it was serverless and because I have more than 120,000 free request per month

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
```

2. **Create a Docker image:**

Build your application into a Docker image following your project's specific build instructions. This will create a Docker image file (e.g., `my-image.tar`) on your local machine.

3. **Tag the Docker image with the Artifact Registry repository URL:**
```
bash
docker tag my-image gcr.io/<PROJECT_ID>/artifact-repository/<REPOSITORY_NAME>/<IMAGE_TAG>
```

Replace `<PROJECT_ID>` with your GCP project ID, `<REPOSITORY_NAME>` with the name of your Artifact Registry repository, and `<IMAGE_TAG>` with the desired tag for your image.

4. **Push the tagged Docker image to the Artifact Registry repository:**
```
bash
docker push gcr.io/<PROJECT_ID>/artifact-repository/<REPOSITORY_NAME>
```

Replace `<PROJECT_ID>`, `<REPOSITORY_NAME>`, and `<IMAGE_TAG>` with the appropriate values. This will push the Docker image to your Artifact Registry repository.

## Verification

1. **Verify the image in the Artifact Registry repository:**
```
bash
gcloud artifacts repositories list
```

This will list all the Artifact Registry repositories in your project. Identify the repository where you pushed your image.

2. **Verify the image details:**

```
bash
gcloud artifacts repositories list tags <REPOSITORY_NAME>
```

Replace `<REPOSITORY_NAME>` with the name of your Artifact Registry repository. This will list all the tags associated with the repository, including the tag you used when pushing your image.

3. **Pull the image from the Artifact Registry repository:**
```
bash
docker pull gcr.io/<PROJECT_ID>/artifact-repository/<REPOSITORY_NAME>/<IMAGE_TAG>
```

Replace `<PROJECT_ID>`, `<REPOSITORY_NAME>`, and `<IMAGE_TAG>` with the appropriate values. This will pull the Docker image from the Artifact Registry repository to your local machine.
