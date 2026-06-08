import sys
from flask import Flask,request,render_template
from src.pipeline import predict_pipeline

predict = predict_pipeline.Predicted()
from src.logger import logging
from src.exception import HRmodel_Exception

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Predictor',methods = ['GET','POST'])
def predictor():
    if request.method == 'GET':
        return render_template('predict.html')
    else:
        satisfication = request.form.get('satisfaction_level')
        last_evaluation = request.form.get('last_evaluation')
        number_project = request.form.get('number_project')
        average_montly_hours = request.form.get('average_montly_hours')
        time_spend_company = request.form.get('time_spend_company')
        Work_accident = request.form.get('Work_accident')
        promotion_last_5years=request.form.get('promotion_last_5years')
        Departments = request.form.get('Departments ')
        salary = request.form.get('salary')
        try:
            get_data = predict_pipeline.GetData(
                satisfaction_level=satisfication,last_evaluation=last_evaluation,number_project=number_project,
                average_montly_hours=average_montly_hours,time_spend_company=time_spend_company,Work_accident=Work_accident,
                promotion_last_5years=promotion_last_5years,Departments=Departments,salary=salary)
            result = predict.predict(get_data.get_dataFrame())
            logging.info('-------------Prediction Done-----------')
        except Exception as e:
            raise HRmodel_Exception(e, sys)


        return render_template('predict.html',result = result[0])
     