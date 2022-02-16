from flask import Flask, request
from flask_restful import Api, Resource

app=Flask(__name__)
api=Api(app)

def machine_learning_model_implementation(age_data):
    # my machine learning model calculations here
    return age_data*2
        
class MyApp(Resource):
    def get(self, model1):
        # no parsing applied
        name=str(request.form['name'])
        print(name + '\n')
        age=float(request.form['age'])
        print(age + '\n')
        
        key1='data'
        val1={'name': name, 'age': age}
        key2='result'
        val2=machine_learning_model_implementation(age)
        result={key1:val1, key2:val2}
        print(result + '\n')
        
        return result
    
    def post(self, model1):
        
        # no parsing applied
        name=str(request.form['name'])
        print(name + '\n')
        age=float(request.form['age'])
        print(age + '\n')
        
        key1='data'
        val1={'name': name, 'age': age}
        key2='result'
        val2=machine_learning_model_implementation(age)
        result={key1:val1, key2:val2}
        print(result + '\n')
        
        return result
    

api.add_resource(MyApp, '/<string:model1>')

if __name__=='__main__':
    app.run(debug=True)