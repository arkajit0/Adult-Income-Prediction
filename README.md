# Adult-Income-Prediction
Adult-Income-Prediction deployment URL: https://adult-income-scaleprediction.herokuapp.com/

## Introduction

### Here we will build a classification model to check the income scales. The dataset we  are using has total 15 columns where 14 are feature columns and 1 label column.

The description of different columns are as follows:-

- age: the age of an individual
○ Integer greater than 0
- workclass: a general term to represent the employment status of an individual
○ Private, Self­emp­not­inc, Self­emp­inc, Federal­gov, Local­gov, State­gov,
Without­pay, Never­worked.
- fnlwgt: final weight. In other words, this is the number of people the census believes
the entry represents..
○ Integer greater than 0
- education: the highest level of education achieved by an individual.
○ Bachelors, Some­college, 11th, HS­grad, Prof­school, Assoc­acdm, Assoc­voc,
9th, 7th­8th, 12th, Masters, 1st­4th, 10th, Doctorate, 5th­6th, Preschool.
- education­num: the highest level of education achieved in numerical form.
○ Integer greater than 0
- marital­status: marital status of an individual. Married­civ­spouse corresponds to a
civilian spouse while Married­AF­spouse is a spouse in the Armed Forces.
○ Married­civ­spouse, Divorced, Never­married, Separated, Widowed,
Married­spouse­absent, Married­AF­spouse.
- occupation: the general type of occupation of an individual
○ Tech­support, Craft­repair, Other­service, Sales, Exec­managerial,
Prof­specialty, Handlers­cleaners, Machine­op­inspct, Adm­clerical,
Farming­fishing, Transport­moving, Priv­house­serv, Protective­serv,
Armed­Forces.
- relationship: represents what this individual is relative to others. For example an
individual could be a Husband. Each entry only has one relationship attribute and is
somewhat redundant with marital status. We might not make use of this attribute at all
○ Wife, Own­child, Husband, Not­in­family, Other­relative, Unmarried.
- race: Descriptions of an individual’s race
○ White, Asian­Pac­Islander, Amer­Indian­Eskimo, Other, Black.
- sex: the biological sex of the individual
○ Male, Female
- capital­gain: capital gains for an individual
○ Integer greater than or equal to 0
- capital­loss: capital loss for an individual
○ Integer greater than or equal to 0
- hours­per­week: the hours an individual has reported to work per week
○ continuous.
- native­country: country of origin for an individual
○ United­States, Cambodia, England, Puerto­Rico, Canada, Germany,
Outlying­US(Guam­USVI­etc), India, Japan, Greece, South, China, Cuba, Iran,
Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal,
Ireland, France, Dominican­Republic, Laos, Ecuador, Taiwan, Haiti, Columbia,
Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El­Salvador,
Trinadad&Tobago, Peru, Hong, Holand­Netherlands.
- the label: whether or not an individual makes more than $50,000 annually.
○ <=50k, >50k

### Instruction to run the file
***Step 1***
**Create and activate an environment**
- Using Conda <br>
conda create -n [your environment name] python=3.7 <br>
Then activate the environment by writing <br>
conda activate [your environment name] <br>

- Using default Environments <br>
python3 -m venv [your environment name] <br>
Then activate the environment by writing <br>
[your environment name]\Scripts\activate.bat [For windows users] <br>
source [your environment name]/bin/activate [For Mac/Ubuntu users] <br>

NOTE: you can give any python version and ignore brackets while giving environment name

***Step 2***
**Install Dependencies**
- For library installations  write <br>
pip install -r requirements.txt 

***Step 3***
**Run The File**
- To run the file write <br>
python app.py
