from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from time import localtime, time, asctime

app = Flask(__name__)
app.static_folder = 'static'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
testlist = [1, 2, 4]
testvar = 'testme'

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     completed = db.Column(db.Integer, default=0)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return '<Task %r>' % self.id

namelist =  ['Johnson', 'Jackson', 'Smith', 'Frank', 'Wilson']
attendtype = ['Call In', 'Call Out', 'Conference', 'Notes', 'Research']
attendon = ['Client', 'Other Side', 'Counsel', 'Other']
today = date.today()
largetime = asctime(localtime(time()))
smalltime = largetime[11:13] + "." + largetime[14:16]

def sortnamelist():
    namelist.sort()
    return namelist

sortnamelist()

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', namelist=namelist, attendtype=attendtype, attendon=attendon, today=today,
                           smalltime=smalltime)

@app.route('/previewfn', methods=['GET', 'POST'])
def previewfn():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Submit':
            return render_template('previewfn')
        else:
            pass
    elif request.method == 'GET':
        return render_template('previewfn')


    # def index():
    # if request.method == 'POST':
    #     task_content = request.form['content']
    #     new_task = Todo(content=task_content)
    #
    #     try:
    #         db.session.add(new_task)
    #         db.session.commit()
    #         return redirect('/')
    #     except:
    #         return 'an issue adding the content'
    #
    # else:
    #     tasks = Todo.query.order_by(Todo.date_created).all()
    #     return render_template('index.html', namelist = namelist, attendtype = attendtype, attendon = attendon, today = today, smalltime = smalltime)
    #, tasks = tasks)

if __name__ == "__main__":
    app.run(debug=True)
