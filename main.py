from flask import Flask, Response, render_template, request, url_for, redirect, jsonify, send_file

from faker import Faker

from helper import locales, random_locale
from extra import countries_dict, country_names_sorted, continents

from random import randint
from openpyxl import Workbook
from io import BytesIO, StringIO, TextIOWrapper
import json, csv, os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')

#@app.route('/')
#def home():
#    return render_template('home.html')

@app.route('/')
def generate():
    return render_template('generate.html',
                           countries=countries_dict,
                           continents=continents)

@app.route('/results')
def results():
    num_users = request.args['numberUsers']
    all_keys = [i for i in request.args.keys()]
    #print(all_keys)
    countries = []
    other_keys = []
    for key in all_keys:
        if key in ('numberUsers', 'EU', 'NA', 'SA', 'AS', 'OC', 'AF', 'world'):
            continue
        if len(key) == 5 and '_' in key:
            countries.append(key)
        else:
            other_keys.append(key)
    
    #print(num_users)
    #print(other_keys)
    #print(countries)

    fake_users_dict = {}
    for i in range(int(num_users)):
        index = randint(0, len(countries)-1)
        fake = Faker(countries[index])
        fake_users_dict[i+1] = {'Name': fake.name()}
        if 'Address' in other_keys:
            fake_users_dict[i+1]['Address'] = (fake.address()).replace('\n', ', ').replace("'", " ")
        if 'PhoneNumber' in other_keys:
            fake_users_dict[i+1]['Phone'] = fake.phone_number()
        if 'Job' in other_keys:
            fake_users_dict[i+1]['Job'] = fake.job()


    users_json = json.dumps(fake_users_dict)
    print(users_json)
    
    return render_template('results.html',
                           num_users=num_users,
                           users=fake_users_dict,
                           other_keys=other_keys,
                           users_json=users_json)

@app.route('/download_excel/', methods=['GET', 'POST'])
def download_excel():
    data = request.json
    print('BACKEND')
    users_data = data['data']
    first_user = users_data['1']
    workbook_categories = []
    for key, value in first_user.items():
        workbook_categories.append(key)
    print(workbook_categories)

    wb = Workbook()
    ws = wb.active

    # Add column headers

    ws.append(workbook_categories)

    # Add rows

    for key, value in users_data.items():
        user = value
        print(user)
        row = []
        for key1, value1 in user.items():
            row.append(value1)
        ws.append(row)
    
    excel_buffer = BytesIO()
    wb.save(excel_buffer)
    excel_buffer.seek(0)
    
    return send_file(excel_buffer, as_attachment=True, download_name="users.xlsx")

@app.route('/download_csv/', methods=['POST'])
def download_csv():
    data = request.json
    print('BACKEND')
    
    users_data = data
    first_user = users_data['1']
    workbook_categories = ['#']
    for key, value in first_user.items():
        workbook_categories.append(key)
    print(workbook_categories)

    # Create a CSV in memory
    csv_buffer = StringIO()
    
    # Write column headers
    csv.writer(csv_buffer).writerow(workbook_categories)

    # Write data
    
    for key, value in users_data.items():
        user = value
        row = [int(key)]
        for key1, value1 in user.items():
            row.append(value1)
        csv.writer(csv_buffer).writerow(row)

    csv_buffer.seek(0)
    
    return csv_buffer


@app.route('/fake_info')
def fake_info():
    locale = random_locale(locales)
    fake = Faker(locale)
    random_user = {}
    
    random_user['name'] = fake.name()
    random_user['address'] = fake.address()
    random_user['job'] = fake.job()
    try: 
        random_user['phone'] = fake.phone_number()
    except:
        random_user['phone'] = 'Phone numbers missing for this provider'

    return jsonify(random_user)



if __name__ == "__main__":
    app.run(debug=True)