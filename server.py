from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

# @app. is decorator
@app.route('/index.html')
def home():
    return render_template('index.html')

# @app.route('/<username>')
# def hello_world(username=None):
#     return render_template('index.html',name=username)

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        # file = database.write('\nemail :- {}, subject :- {}, message :- {}'.format(email,subject,message))
        file = database.write(f'\nemail :- {email}, subject :- {subject}, message :- {message}')

def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_write = csv.writer(database2,delimiter=',' ,quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Some thing went wrong. Try again'



# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/thankyou.html')
# def thankyou():
#     return render_template('thankyou.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')
