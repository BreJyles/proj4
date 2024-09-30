import pandas as pd
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(self, sex_flag, age, fare, familySize, p_class, embarked, has_cabin):
        # create dataframe of one row for inference
        df = pd.DataFrame()
        df["Sex"] = [sex_flag]
        df["Age"] = [age]
        df["Fare"] = [fare]
        df["Has_Cabin"] = [has_cabin]
        df["Family_Size"] = [familySize]
        df["Pclass"] = [p_class]
        df["Embarked"] = [embarked]

        # model
        model = pickle.load(open("titanic_model_pipeline2.h5", 'rb'))

        # columns in order
        df = df.loc[:, ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'Has_Cabin', 'Family_Size']]

        preds = model.predict_proba(df)
        return(preds[0][1])
