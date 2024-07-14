# machine_failure_prediction

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

MLOps for managing web service which predicts machine failure.

Initial exploratory data analysis is in notebooks/1.0-cvd-machine-failure-eda.ipynb


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

