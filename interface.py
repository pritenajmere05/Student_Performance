from flask import Flask , request , jsonify , render_template
from utils import get_predicted_performance
import config

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_performance' , methods = ['POST'])
def predict():
     
     data = request.form

     Hours_Studied = int(data['Hours_Studied'])
     Previous_Scores = int(data['Previous_Scores'])
     Extracurricular_Activities = data['Extracurricular_Activities']
     Sleep_Hours = int(data['Sleep_Hours'])
     Sample_Question_Papers_Practiced = int(data['Sample_Question_Papers_Practiced'])

     predicted_performance = get_predicted_performance(Hours_Studied,
                                                        Previous_Scores,
                                                        Extracurricular_Activities,
                                                        Sleep_Hours,
                                                        Sample_Question_Papers_Practiced)
     
     return render_template('index.html',final_performance = predicted_performance)

if __name__ == '__main__':
     app.run(host='0.0.0.0' , port=config.PORT_NUMBER)