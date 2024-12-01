# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

The model chosen for the classification task was the RandomForestClassifier from sklearn.model.RandomForestClassifier.

The default parameters were used for the training.

## Intended Use

This model can be used to predict if an individual has a salary over 50k based off of a number of collected cesnus data attributes. 

The usage is meant for research and academic purposes.

## Training Data

The Census Income Dataset was obtained from the UCI Machine Learning Repository  https://archive.ics.uci.edu/ml/datasets/census+income

#### Data Features:

age: continuous.
workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
fnlwgt: continuous.
education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
education-num: continuous.
marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
sex: Female, Male.
capital-gain: continuous.
capital-loss: continuous.
hours-per-week: continuous.
native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.

The original data set has 32.561 rows and 15 columns composed of the target label "salary", 8 categorical features and 6 numerical features. Details on each of the features ae available at the UCI link above. Target label "salary" has two classes ('<=50K', '>50K') and shows class imbalance with a ratio of circa 75% / 25%. A simple data cleansing was performed on the original dataset to remove leading and trailing whitespaces.

## Evaluation Data

After the original dataset was preprocessed it was then split into training and evaluation data with evaluation data size of 20%

## Metrics

Performances of the model:

precision: 0.7300
recall: 0.6445
fbeta: 0.6846

## Ethical Considerations

This model is trained on census data collected in a relatively unbiased process. Care should be used however, and a holistic view of the results and underlying data should be applied before making rigid decisions regarding outcomes.

## Caveats and Recommendations

The dataset used is from a 1994 cesnus database. While the underlying process used is still valid, it may not be a good statistical representation of the current population.