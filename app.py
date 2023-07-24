#creating a simple web application
from flask import Flask,render_template,request, redirect, url_for

#create a flask app
app = Flask(__name__)



@app.route('/')
def home():
     return render_template('index.html')

@app.route('/welcome')
def welcome():
     return 'welcome to the flask tutorial'

@app.route('/index')
def index():
     return 'Welcome to index page welcome'

@app.route('/success/<int:score>')
def success(score):
     return 'The person is passed with score '+str(score)
@app.route('/fail/<int:score>')
def fail(score):
     return 'The person is failed with score '+str(score)



@app.route('/calculate', methods= ['POST', 'GET']) 
def calculate():
     if request.method == "GET":
          return render_template('calculate.html') 
     else:
         maths =  float(request.form['maths']) 
         science =  float(request.form['science'])
         history =  float(request.form['history'])
         
         average_marks = (maths+science+history)/3
         result = ""
         if average_marks >= 50:
              result = "success"
         else:
              result = "fail"
              
     # return redirect(url_for(result, score =  average_marks))
         
         return render_template('result.html', results = average_marks)  
    
    
@app.route('/dictionary')
def dictionary():
     dict = {
     "name":"Basit",
     "age": 25,
     "course": "mca"
}
     return render_template('dict.html', values = dict)

     

if __name__ == "__main__":
     app.run(debug=True)     #debug = True helps in reloading whenever we make any changes