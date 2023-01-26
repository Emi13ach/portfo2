from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', 'a') as file: 
        email = data['email']
        subject = data['subject']
        message = data['message']
        file.write(f'\n{email}, {subject}, {message}')
        

def write_to_csv(data):
    with open('database.csv', 'a') as data_csv: 
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(data_csv, delimiter=',', lineterminator='\n', quotechar='|', quoting=csv.QUOTE_NONE)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("thankyou.html")
        except:
            return 'did not save to database'
    else:
        return 'Invalid data'
    
if __name__ == "__main__":
    app.run(debug=True)
    