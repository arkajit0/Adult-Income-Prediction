from flask import Flask, request, render_template
import xgboost as xgb
import pickle

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        # try:
            education_dict = {'Preschool': 1, '1st-4th': 2, '5th-6th': 3, '7th-8th': 4, '9th': 5, '10th': 6, '11th': 7,
                              '12th': 8, 'HS-grad': 9, 'Some-college': 10, 'Assoc-voc': 11, 'Assoc-acdm': 12,
                              'Bachelors': 13, 'Masters': 14, 'Prof-school': 15, 'Doctorate': 16}

            gender = {'Male': 0, 'Female': 1}
            country = {'United-States': 67159, 'Mexico': 1080, 'Philippines': 522, 'Germany': 381, 'Canada': 349,
                       'India': 321, 'England': 289, 'Puerto-Rico': 267, 'China': 236, 'Cuba': 232, 'Japan': 222,
                       'El-Salvador': 221, 'Jamaica': 188, 'South': 184, 'Italy': 177, 'Taiwan': 158, 'Poland': 156,
                       'Dominican-Republic': 153, 'Vietnam': 139, 'Iran': 127, 'Haiti': 121, 'Guatemala': 121,
                       'Greece': 120, 'Columbia': 120, 'Portugal': 111, 'France': 109, 'Ecuador': 95, 'Nicaragua': 90,
                       'Ireland': 87, 'Peru': 84, 'Cambodia': 84, 'Hong': 84, 'Thailand': 82, 'Trinadad&Tobago': 76,
                       'Outlying-US(Guam-USVI-etc)': 72, 'Yugoslavia': 71, 'Honduras': 55, 'Hungary': 54,
                       'Scotland': 53, 'Laos': 42, 'Holand-Netherlands': 18}
            wage_class = {0: 'earns more than 50000', 1: 'earns less than 50000'}

            wageclass_dict = {'Local-gov': 0, 'Never-worked': 1, 'Private': 2, 'Self-emp-inc': 3, 'Self-emp-not-inc': 4,
                               'State-gov': 5, 'Without-pay': 6, 'Federal-gov': None}
            marital_status = {'Married-AF-spouse': 0, 'Married-civ-spouse': 1, 'Married-spouse-absent': 2,
                              'Never-married': 3, 'Separated': 4, 'Widowed': 5, 'Divorced': None}
            occupation = {'Armed-Forces': 0, 'Craft-repair': 1, 'Exec-managerial': 2, 'Farming-fishing': 3,
                          'Handlers-cleaners': 4, 'Machine-op-inspct': 5, 'Other-service': 6, 'Priv-house-serv': 7,
                          'Prof-specialty': 8, 'Protective-serv': 9, 'Sales': 10, 'Tech-support': 11,
                          'Transport-moving': 12, 'Adm-clerical': None}
            relationship = {'Not-in-family': 0, 'Other-relative': 1, 'Own-child': 2, 'Unmarried': 3, 'Wife': 4,
                            'Husband': None}
            race_dict = {'Asian-Pac-Islander': 0, 'Black': 1, 'Other': 2, 'White': 3, 'Amer-Indian-Eskimo': None}

            # print(request.form)
            age = float(request.form['age'])
            education = education_dict[request.form['education']]
            sex = gender[request.form['gender']]
            c_gain = float(request.form['capital_gain'])
            c_loss = float(request.form['capital_loss'])
            hrs_per_week = float(request.form['hrs_per_week'])
            native_country = country[request.form['native_country']]
            fnlwgt = (float(request.form['fnlwgt'])**(0.4579124374001098) -1)/0.4579124374001098
            marital = marital_status[request.form['marital_status']]
            occ = occupation[request.form['occupation']]
            race = race_dict[request.form['race']]
            wageclass = wageclass_dict[request.form['wageclass']]
            relation_status = relationship[request.form['relation_status']]

            wg_class = [0]*7
            if wageclass == None:
                wg0, wg1, wg2, wg3, wg4, wg5, wg6 = wg_class
            else:
                wg_class[wageclass] = 1
                wg0, wg1, wg2, wg3, wg4, wg5, wg6 = wg_class

            maritalstatus = [0]*6
            if marital == None:
                m0, m1, m2, m3, m4, m5 = maritalstatus
            else:
                maritalstatus[marital] = 1
                m0, m1, m2, m3, m4, m5 = maritalstatus

            occ_ = [0]*13
            if occ == None:
                o0, o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11, o12 = occ_
            else:
                occ_[occ] = 1
                o0, o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11, o12 = occ_

            relation = [0]*5
            if relation_status == None:
                r0, r1, r2, r3, r4 = relation
            else:
                relation[relation_status] = 1
                r0, r1, r2, r3, r4 = relation

            race_ = [0]*4
            if race == None:
                ra0, ra1, ra2, ra3 = race_
            else:
                race_[race] = 1
                ra0, ra1, ra2, ra3 = race_


            scale = pickle.load(open('scale.pkl', 'rb'))
            model = pickle.load(open('final_model_v2.pkl', 'rb'))

            predict = model.predict(scale.transform([[age, education, sex, c_gain, c_loss, hrs_per_week, native_country,
                                                       fnlwgt, m0, m1, m2, m3, m4, m5, o0, o1, o2, o3, o4, o5, o6, o7,
                                                       o8, o9, o10, o11, o12, ra0, ra1, ra2, ra3, wg0, wg1, wg2, wg3,
                                                       wg4, wg5, wg6, r0, r1, r2, r3, r4]]))[0]

            print(predict)

            return render_template("result.html", prediction=wage_class[predict])

        # except Exception as e:
        #     print(e)
        #     print('something went wrong')

if __name__ == '__main__':
    app.run(debug=True)


