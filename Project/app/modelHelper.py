# Imports
import pandas as pd
import numpy as np
import pickle

class ModelHelper():
    def __init__(self):
        pass

    def makePrediction(self, gender, customer_type, age, travel_type, travel_class, 
                        distance, wifi, time_convenience, booking, gate, food,
                        boarding, comfort, entertainment, onboard_service, legroom, 
                        baggage, checkin_service, inflight_service, cleanliness, delay_d, delay_a):

        df_surv = pd.DataFrame()
        df_surv['Inflight wifi service'] = [wifi]
        df_surv['Departure/Arrival time convenient'] = [time_convenience]
        df_surv['Ease of Online booking'] = [booking]
        df_surv['Gate location'] = [gate]
        df_surv['Food and drink'] = [food]
        df_surv['Online boarding'] = [boarding]
        df_surv['Seat comfort'] = [comfort]
        df_surv['Inflight entertainment'] = [entertainment]
        df_surv['On-board service'] = [onboard_service]
        df_surv['Leg room service'] = [legroom]
        df_surv['Baggage handling'] = [baggage]
        df_surv['Checkin service'] = [checkin_service]
        df_surv['Inflight service'] = [inflight_service]
        df_surv['Cleanliness'] = [cleanliness]
        
        df_num = pd.DataFrame()
        df_num['Age'] = [age]
        df_num['Flight Distance'] = [distance]
        df_num['Departure Delay in Minutes'] = [delay_d]
        df_num['Arrival Delay in Minutes'] = [delay_a]

        scaler = pickle.load(open("satisfaction_scaler.h5", 'rb'))
        
        scaled_data = scaler.transform(df_num)
        df_scaled = pd.DataFrame(scaled_data, columns = ['Age', 'Flight Distance', 'Departure Delay in Minutes', 'Arrival Delay in Minutes'])

        df_encoded = pd.DataFrame()
        if gender == 'Male':
            df_encoded['Gender'] = [0]
        else:
            df_encoded['Gender'] = [1]

        if customer_type == 'disloyal Customer':
            df_encoded['Customer Type'] = [0]
        else:
            df_encoded['Customer Type'] = [1]

        if travel_type == 'Business travel':
            df_encoded['Type of Travel'] = [0]
        else:
            df_encoded['Type of Travel'] = [1]

        class_b = 0
        class_e = 0
        class_ep = 0

        if travel_class == 'Business':
            class_b = 1
        elif travel_class == 'Eco':
            class_e = 1
        else:
            class_ep = 1

        df_encoded['Class_Business'] = [class_b]
        df_encoded['Class_Eco'] = [class_e]
        df_encoded['Class_Eco Plus'] = [class_ep]
        
        df = pd.concat([df_encoded, df_scaled], axis=1)
        df = pd.concat([df, df_surv], axis=1)

        model = pickle.load(open("satisfaction_model.h5", 'rb'))

        preds = model.predict_proba(df)
        return(preds[0][1])