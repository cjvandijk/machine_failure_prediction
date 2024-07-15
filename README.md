# machine_failure_prediction

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

MLOps for managing web service which predicts machine failure.

Initial exploratory data analysis is in notebooks/1.0-cvd-machine-failure-eda.ipynb

Launch EC2 instance, ssh into it
Prepare environment ()
Install conda
Set python version 
`conda install python=3.10`
Install pipenv
`sudo apt install pipenv`
Using pipenv on EC2 with conda installed
`pipenv --python=$(conda run which python) --site-packages`
Install mlflow
`pipenv install mlflow`

Start mlflow server. Creates sqlite database to store model experiments and artifacts.
`mlflow server --backend-store-uri sqlite///backend.db --default-artifact-root ./artifact_local`
Forward port via VS Code and visit UI in url pointed at `http://127.0.0.1:5000`

Run mage
Install and launch via docker
`docker run -it -p 6789:6789 -v $(pwd):/home/src mageai/mageai /app/run_app.sh mage start machine_failure_prediction`
Open browser to http://localhost:6789

Launch Mage and the database service (PostgreSQL):
`./scripts/start.sh`
Open mage UI in browser [`http://localhost:6789`](http://localhost:6789)




## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, DictVectorizers, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebook for exploratory data analysis
│
├── Pipfile            <- Dependencies for reproducing the analysis environment via pipenv
|
|── Pipfile.lock       <- Locked dependency versions for pipenv installations 
│
├── setup.cfg          <- Configuration file for flake8
│
└── machine_failure_prediction                <- Source code for use in this project.
    │
    ├── __init__.py       <- Makes machine_failure_prediction a Python module
    │
    ├── build_features.py <- Script to turn raw data into features for modeling
    │
    ├── models            <- Scripts to train models and then use trained models to make
        │                    predictions
        ├── predict_model.py
        └── train_model.py

```

--------

