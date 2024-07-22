from django.shortcuts import redirect, render
import requests

# Create your views here.


def viewState(request):
    stateData = requests.post('https://lgdirectory.gov.in/webservices/lgdws/stateList').json()

    # print(stateData)
    return render(request,'showState.html',context={'state':stateData})

def viewDistrict(request,id):
    print(id)

    # if scode==27:
    #     query='https://lgdirectory.gov.in/webservices/lgdws/districtList?stateCode='+id
    #     print(query)
    #     districtData = requests.post(query).json()
    #     return redirect('district_url')

    query='https://lgdirectory.gov.in/webservices/lgdws/districtList?stateCode='+id
    districtData = requests.post(query).json()
    return render(request,'showDistrict.html',context={'district':districtData})

def viewTaluka(request):
    talukaData = requests.post('https://lgdirectory.gov.in/webservices/lgdws/subdistrictList').json()
    return render(request,'showTaluka.html',context={'taluka' : talukaData})
