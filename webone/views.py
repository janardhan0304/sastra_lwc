from django.shortcuts import render, redirect
from django.http import HttpResponse
import pickle
import pandas as pd
def home_page(request):
    return render(request, 'main_page.html')
    
def my_view(request):
    crops=['apple',
    'banana',
    'blackgram',
    'chickpea',
    'coconut',
    'coffee',
    'cotton',
    'grapes',
    'jute',
    'kidneybeans',
    'lentil',
    'maize',
    'mango',
    'mothbeans',
    'mungbean',
    'muskmelon',
    'orange',
    'papaya',
    'pigeonpeas',
    'pomegranate',
    'rice',
    'watermelon']
    text_data = request.GET['hidden-text-area']
    text_data = text_data.split("|")
    state,district,month,n_val,p_val,k_val,ph_val,humidity,temperature,precip = text_data[:]
    value_data = {
        "state":state,"district":district,"month":month,"n_val":int(n_val),"p_val":int(p_val),"k_val":int(k_val),"ph_val":round(float(ph_val),2),"humidity":round(float(humidity),2),"temperature":round(float(temperature),2),"precip":round(float(precip),2)
    }
    one_set = [state,district,month,  int(n_val),int(p_val),int(k_val),float(ph_val),float(humidity),float(temperature),float(precip)]
    two_set = [state,district,month,  int(n_val),int(p_val),int(k_val),float(ph_val)-0.3,float(humidity)-2,float(temperature)-2,float(precip)-12]
    third_set = [state,district,month,int(n_val),int(p_val),int(k_val),float(ph_val)+0.3,float(humidity)+2,float(temperature)+2,float(precip)+12]
    file = open('/home/ubuntu/sastra-lwc/webone/modelfile.pkl','rb')
    # file = open(r'C:\Users\dksr1\OneDrive\Desktop\sastra-lwc\webone\modelfile.pkl','rb')
    model = pickle.load(file)
    dictionary_1 = {
    'N':[one_set[3]],
    'P':[one_set[4]],
    'K':[one_set[5]],
    'temperature':[one_set[8]],
    'humidity':[one_set[7]],
    'ph':[one_set[6]],
    'rainfall':[one_set[9]]
    }
    dictionary_2 = {
    'N':[two_set[3]],
    'P':[two_set[4]],
    'K':[two_set[5]],
    'temperature':[two_set[8]],
    'humidity':[two_set[7]],
    'ph':[two_set[6]],
    'rainfall':[two_set[9]]
    }
    dictionary_3 = {
    'N':[third_set[3]],
    'P':[third_set[4]],
    'K':[third_set[5]],
    'temperature':[third_set[8]],
    'humidity':[third_set[7]],
    'ph':[third_set[6]],
    'rainfall':[third_set[9]]
    }
    dictionary_4 = {
    'N':[third_set[3]],
    'P':[third_set[4]],
    'K':[third_set[5]],
    'temperature':[third_set[8]+3],
    'humidity':[third_set[7]-3],
    'ph':[third_set[6]+0.5],
    'rainfall':[third_set[9]-7]
    }
    dictionary_5 = {
    'N':[third_set[3]],
    'P':[third_set[4]],
    'K':[third_set[5]],
    'temperature':[third_set[8]-3],
    'humidity':[third_set[7]+3],
    'ph':[third_set[6]+0.5],
    'rainfall':[third_set[9]+7]
    }
    dictionary_6 = {
    'N':[third_set[3]],
    'P':[third_set[4]],
    'K':[third_set[5]],
    'temperature':[third_set[8]+2],
    'humidity':[third_set[7]-2],
    'ph':[third_set[6]+0.5],
    'rainfall':[third_set[9]-5]
    }
    dictionary_7 = {
    'N':[third_set[3]],
    'P':[third_set[4]],
    'K':[third_set[5]],
    'temperature':[third_set[8]-2],
    'humidity':[third_set[7]+2],
    'ph':[third_set[6]+0.5],
    'rainfall':[third_set[9]+9]
    }

    t = pd.DataFrame(dictionary_1)
    ans_1 = model.predict(t)
    # print(crops[ans_1[0]])

    t = pd.DataFrame(dictionary_2)
    ans_2 = model.predict(t)
    # print(crops[ans_2[0]])

    t = pd.DataFrame(dictionary_3)
    ans_3 = model.predict(t)
    # print(crops[ans_3[0]])

    t = pd.DataFrame(dictionary_4)
    ans_4 = model.predict(t)
    # print(crops[ans_4[0]])

    t = pd.DataFrame(dictionary_5)
    ans_5 = model.predict(t)
    # print(crops[ans_5[0]])

    t = pd.DataFrame(dictionary_6)
    ans_6 = model.predict(t)
    # print(crops[ans_6[0]])

    t = pd.DataFrame(dictionary_7)
    ans_7 = model.predict(t)
    # print(crops[ans_7[0]])
    crops_suggested = []
    crops_had = [crops[ans_1[0]],crops[ans_2[0]],crops[ans_3[0]],crops[ans_4[0]],crops[ans_5[0]],crops[ans_6[0]],crops[ans_7[0]]]
    for i in crops_had:
        if i  not in crops_suggested:
            crops_suggested.append(i)
    new_x = {}
    for i in range(len(crops_suggested)):
        new_x[i] = crops_suggested[i]
    file.close()
    
    return render(request, 'display.html',{'x':value_data,'y':crops_suggested})
