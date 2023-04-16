import requests
import json 

def get_IOC():
    #http://acsioc01.francecentral.cloudapp.azure.com:8080/api/get_ips
    list = [] #list new IOC 
    response = requests.get(
        'http://acsioc01.francecentral.cloudapp.azure.com:8080/api/get_all_ip'
    )   
    response = response.json()
    #print(response)
    #print(response['all_ip_list'])
    for i in response['all_ip_list'] :
        list.append(i['ip'])
    return list