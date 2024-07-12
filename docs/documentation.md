# Climate Impact on Agricultural Yield

## Project Overview

This project analyzes the impact of climate change on agricultural yield using various datasets related to temperature change, land cover, sea level, and atmospheric conditions. The goal is to build a predictive model that can forecast agricultural production based on climate variables.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Installation

To run this project, you will need to have Python installed on your system. You can install the required packages using `conda` or `pip`.

### Using Conda

```sh
conda create -n climate_impact_env python=3.8
conda activate climate_impact_env
conda install pandas numpy scikit-learn matplotlib seaborn joblib

pip install -r requirements.txt

Climate_Impact_Agriculture_Yield/
├── data/
│   ├── final/
│   ├── processed/
│   ├── raw/
├── models/
│   └── random_forest_model.pkl
├── notebooks/
│   ├── EDA.ipynb
│   ├── feature_engineering.ipynb
├── results/
│   ├── visualizations/
│   ├── metrics/
│   ├── data_samples/
│   ├── reports/
├── src/
│   ├── load_data.py
│   ├── merge_data.py
│   ├── feature_engineering.py
│   ├── eda.py
│   ├── train_model.py
│   ├── evaluate_model.py
├── LICENSE
├── README.md
└── requirements.txt

python src/load_data.py

python src/merge_data.py

python src/feature_engineering.py

python src/eda.py

python src/train_model.py

python src/evaluate_model.py

jupyter notebook notebooks/EDA.ipynb

