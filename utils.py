import pickle
import json
import numpy as np
import config

with open(config.JSON_PATH,'r') as f:
    json_data = json.load(f)

with open(config.PICKLE_PATH,'rb') as f:
    model = pickle.load(f)

def get_predicted_performance(Hours_Studied,
                                Previous_Scores,
                                Extracurricular_Activities,
                                Sleep_Hours,
                                Sample_Question_Papers_Practiced):
    dict1 = {"Yes" : 1 , "No" : 0}
    test_array = np.zeros([1,5])
    test_array[0,0] = Hours_Studied
    test_array[0,1] = Previous_Scores
    test_array[0,2] = dict1[Extracurricular_Activities]
    test_array[0,3] = Sleep_Hours
    test_array[0,4] = Sample_Question_Papers_Practiced

    predict = model.predict(test_array)

    return predict

