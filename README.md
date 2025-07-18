
# Project

## Aim

### Primary: Predict two types of diabtes

This project aims to predict two types of diabtes in a person or if the person is healthy (i.e. has no diabetes) based on the history of the patient.

The primary metric is f1-score.

### Revised Aim: Distinguish healthy from persons with diabtes

This project aims to predict whether a person has diabetes.

This change is necessary, because separating the two types of diabetes in person from healthy is not satisfyingly possible with this data. See section _Results > Primary_.

## Results

### Primary: Predict two types of diabtes

All shown models are default RandomForests with `class_weight="balanced"`. All evaluation was done on a held-out test set.

The majority class of healthy people prevents effective learning of patterns of diabetes. The baseline model `2025-06-27_10-12-18` heavily favors class 0 (healthy) and never predicts class 1.

_Confusion Matrix of 2025-06-27_10-12-18_

| True \ Pred |   0   |   1   |   2   |
|-------------|-------|-------|-------|
| **0**       | 20712 |   64  |  688  |
| **1**       |  449  |   0   |  39   |
| **2**       | 2968  |   7   |  567  |

Neither default SMOTE (model `2025-06-27_10-08-08`) nor sole upsampling of class 1 (model `2025-06-27_10-26-03`) improves the prediction.

_Confusion Matrix of 2025-06-27_10-08-08_

| True \ Pred |   0   |   1   |   2   |
|-------------|-------|-------|-------|
| **0**       | 20067 |  39   | 1358  |
| **1**       |  405  |   0   |  83   |
| **2**       | _2490_  |   8   | 1044  |

A baseline model `2025-06-27_11-25-16` to distinguish classes 1 and 2 confirms that the data lacks sufficient structure to distinguish class 1 from class 2.

_Confusion Matrix of 2025-06-27_11-25-16_

| True \ Pred |   1   |   2   |
|-------------|-------|-------|
| **1**       |  14   |  _474_  |
| **2**       |  46   | 3496  |

The aim of this project is therefore revised to **predict any form of diabetes**.

## Data

Collected from `https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/data`.

> The Behavioral Risk Factor Surveillance System (BRFSS) is a health-related telephone survey that is collected annually by the CDC. Each year, the survey collects responses from over 400,000 Americans on health-related risk behaviors, chronic health conditions, and the use of preventative services. It has been conducted every year since 1984. For this project, a csv of the dataset available on Kaggle for the year 2015 was used. This original dataset contains responses from 441,455 individuals and has 330 features. These features are either questions directly asked of participants, or calculated variables based on individual participant responses.
>
> This dataset contains 3 files:
>
>     diabetes_012_health_indicators_BRFSS2015.csv is a clean dataset of 253,680 survey responses to the CDC's BRFSS2015. The target variable Diabetes_012 has 3 classes. 0 is for no diabetes or only during pregnancy, 1 is for prediabetes, and 2 is for diabetes. There is class imbalance in this dataset. This dataset has 21 feature variables
>     diabetes_binary_5050split_health_indicators_BRFSS2015.csv is a clean dataset of 70,692 survey responses to the CDC's BRFSS2015. It has an equal 50-50 split of respondents with no diabetes and with either prediabetes or diabetes. The target variable Diabetes_binary has 2 classes. 0 is for no diabetes, and 1 is for prediabetes or diabetes. This dataset has 21 feature variables and is balanced.
>     diabetes_binary_health_indicators_BRFSS2015.csv is a clean dataset of 253,680 survey responses to the CDC's BRFSS2015. The target variable Diabetes_binary has 2 classes. 0 is for no diabetes, and 1 is for prediabetes or diabetes. This dataset has 21 feature variables and is not balanced.

This data set is a modified version:
> Acknowledgements
> It it important to reiterate that I did not create this dataset, it is just a cleaned and consolidated dataset created from the BRFSS 2015 dataset already on Kaggle. That dataset can be found here and the notebook I used for the data cleaning can be found here.
>
> Inspiration
> Zidian Xie et al for Building Risk Prediction Models for Type 2 Diabetes Using Machine Learning Techniques using the 2014 BRFSS was the inspiration for creating this dataset and exploring the BRFSS in general. `https://www.cdc.gov/pcd/issues/2019/19_0109.htm`
