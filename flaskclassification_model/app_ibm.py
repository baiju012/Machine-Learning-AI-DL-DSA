# Step 1 - Importing the required lib

from flask import Flask,request,render_template
import pickle

# Step 2 - Initializing the flask

app = Flask(__name__)
model = pickle.load(open('classification_rf.pkl', 'rb'))

# Step 3 - Routing to the templates with some functionalities
@app.route('/')
def home():
    return render_template('input.html')


@app.route('/input',methods = ['POST'])
def pred():
    gender = request.form.get('gender')
    age = request.form.get('age')
    salary = request.form.get('salary')
    input = [[int(gender), int(age), float(salary)]]
    op = model.predict(input)
    print(op)
    
    
    
    

    return render_template('input.html',Output=str(op))


# Step 4 - Run the application

if __name__ == '__main__':
    app.run()