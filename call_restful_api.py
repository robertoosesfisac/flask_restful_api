from requests import get, put

x= get('http://127.0.0.1:5000/model1', 
       data={'name':'Jon','age':'30'}).json()
       
print(x)

#TODO: Python code works, calls from the browser do not - error 400 - sthg related with request.form['name']
#TODO: test curl works as well
#TODO: test from POSTMAN as well