import os
import json
import csv
from handy_tools import value_checker, api_authentication
from api_methods import get_fetch
from requests.auth import HTTPBasicAuth  

def jfrog_registries_repositories():
    os.system("cls")
    while True:
        print("[----{title}----]".format(title="JFrog Registries & Repositories".upper()))
        print("[1] - GET and print registry & repositories \n[2] - Print to CSV all results \n[3] - Back")
        value = input("Enter your choice: ")
        valid, value = value_checker(value)
        if valid:
            value = int(value)
            if value == 1: 
                username, password = api_authentication()
                auth = HTTPBasicAuth(username,password)
                url = "https://blockone.jfrog.io/artifactory/api/repositories?type=local&packageType=docker"  

                data = get_fetch(url=url,auth=auth)
                if data:
                    for key in data:
                        key = key["key"]
                        print("\nKey:",key,":")
                        url = "https://blockone.jfrog.io/artifactory/api/docker/{key}/v2/_catalog".format(key=key) 
                        repositories = get_fetch(url=url,auth=auth)["repositories"]
                        if repositories:
                            repository = json.dumps(repositories, indent=4, sort_keys=True)
                            print(repository)
                        print("Total:", len(repositories),"\n")

            elif value == 2:
                print("WARNING:", "Any file name that is existing already will be overwriten!")
                username, password = api_authentication()
                auth = HTTPBasicAuth(username,password)
                url = "https://blockone.jfrog.io/artifactory/api/repositories?type=local&packageType=docker" 
                data = get_fetch(url=url,auth=auth)
                if data:
                    filename = input("Enter your filename: ")
                    if filename:
                        filename = "files_csv/{filename}.csv".format(filename=filename)
                        print("Writting...")
                        with open(filename, 'w', newline='') as file:
                            writer = csv.writer(file)
                            for key in data:
                                key = key["key"] 
                                url = "https://blockone.jfrog.io/artifactory/api/docker/{key}/v2/_catalog".format(key=key)
                                writer.writerow(["key:",key])  
                                writer.writerow(["Repositories:"])  
                                repositories = get_fetch(url=url,auth=auth)["repositories"]
                                if repositories:
                                    for repository in repositories:
                                        writer.writerow(['',repository])   
                                writer.writerow(["Total:",str(len(repositories))]) 
                                writer.writerow([""])
                            os.system("cls")
                            print("Sucessfully printed to csv!\n")
            elif value == 3:
                os.system("cls")
                print("Returning to main page!!!\n")
                break
            else:
                print("Invalid value!!!\n")
        else:
            os.system("cls")
            print("Invalid value!!!\n")
 
def qualys_repositories():
    os.system("cls")
    while True:
        print("[----{title}----]".format(title="Qualys Repositories".upper()))
        print("[1] - GET and print qualys repositories \n[2] - Print to CSV all results \n[3] - Back")
        value = input("Enter your choice: ")
        valid, value = value_checker(value)
        if valid:
            value = int(value)
            if value == 1:
                username, password = api_authentication()
                auth = HTTPBasicAuth(username,password)  
                url = "https://qualysapi.qg3.apps.qualys.com/csapi/v1.1/registry?pageNo=1&pageSize=50" 
                data = get_fetch(url=url,auth=auth)
                if data:
                    data = data["data"]
                    for item in data:
                        registryUuid = item["registryUuid"]
                        print("Registry UUID:", registryUuid)
                        url = "https://qualysapi.qg3.apps.qualys.com/csapi/v1.1/registry/{registry}/repository?pageNo=1&pageSize=200".format(registry=registryUuid)  
                        data = get_fetch(url=url,auth=auth)
                        if data:
                            data = data["data"]
                            for item in data:
                                print("-",item["repoName"])
                            print("Total: "+str(len(data)),"\n")
                        else:
                            print("-> No results found!\n")                      
            elif value == 2:
                print("WARNING:", "Any file name that is existing already will be overwriten!")
                username, password = api_authentication()
                auth = HTTPBasicAuth(username,password) 
                url = "https://qualysapi.qg3.apps.qualys.com/csapi/v1.1/registry?pageNo=1&pageSize=50"
                data = get_fetch(url=url,auth=auth)
                if data:
                    filename = input("Enter your filename: ")
                    if filename:
                        filename = "files_csv/{filename}.csv".format(filename=filename)
                        print("Writting...")
                        with open(filename, 'w', newline='') as file:
                            writer = csv.writer(file)
                            data = data["data"]
                            for item in data:
                                registryUuid = item["registryUuid"]
                                writer.writerow(["Registry UUID:",registryUuid])  
                                writer.writerow(["Repositories:"])  
                                url = "https://qualysapi.qg3.apps.qualys.com/csapi/v1.1/registry/{registry}/repository?pageNo=1&pageSize=200".format(registry=registryUuid) 
                                data = get_fetch(url=url,auth=auth)
                                if data:
                                    data = data["data"]
                                    for item in data:
                                        writer.writerow(['',item["repoName"]])    
                                    writer.writerow(['Total:',len(data)]) 
                                    writer.writerow([""])
                                else:
                                    writer.writerow(["No results found!"])  
                                    writer.writerow([""])   
                            os.system("cls")
                            print("Sucessfully printed to csv!\n")
            elif value == 3:
                os.system("cls")
                print("Returning to main page!!!\n")
                break
            else:
                print("Invalid value!!!\n")
        else:
            os.system("cls")
            print("Invalid value!!!\n")

def all_onboarded_difference_repositories():
    os.system("cls")
    while True:
        print("[----{title}----]".format(title="All, Onboarded, & Difference Repositories".upper()))
        print("[1] - GET and print all, onboarded, & difference repositories \n[2] - Print to CSV all results \n[3] - Back")
        value = input("Enter your choice: ")
        valid, value = value_checker(value)
        if valid:
            value = int(value)
            if value == 1: 
                print("--------------[JFROG LOGIN]--------------")
                username, password = api_authentication()
                jfrog_auth = HTTPBasicAuth(username,password) 
                print("--------------[QUALYS LOGIN]--------------")
                username, password = api_authentication()
                qualys_auth = HTTPBasicAuth(username,password) 
 
                repositories = [['b1fs-b1x-docker-buildkite-local','e92b970d-17aa-47b8-833f-4d34fcaec4bc'],['b1fs-b1x-docker-dev-local','7bb778cf-4d89-4e3d-bd84-0ee2dbd873a3']]
                
                jfrog_list, qualys_list = [], []

                for jfrog, qualys in repositories:
                    # JFrog
                    jfrog_url = "https://blockone.jfrog.io/artifactory/api/docker/{jfrog}/v2/_catalog".format(jfrog=jfrog)
                    jfrog_data = get_fetch(url=jfrog_url,auth=jfrog_auth) 
                    if jfrog_data:
                        print(jfrog,":")
                        repositories = jfrog_data["repositories"]
                        for repository in repositories:
                            print('-',repository)
                            jfrog_list.append(repository)
                        print("Total:",len(repositories),"\n")
                    # Qualys
 
                    qualys_url = "https://qualysapi.qg3.apps.qualys.com/csapi/v1.1/registry/{qualys}/repository?pageNo=1&pageSize=200".format(qualys=qualys)
                    qualys_data = get_fetch(url=qualys_url,auth=qualys_auth) 
                    if qualys_data: 
                        print(qualys,":")
                        qualys_data = qualys_data["data"]
                        for repoName in qualys_data:
                            repoName = repoName["repoName"]
                            print("-",repoName)
                            qualys_list.append(repoName)
                        print("Total:",len(qualys_data),"\n")
                
                    # Symmetric difference
                    print("Symmetric difference: ")
                    symmetric_difference = set(jfrog_list) ^ set(qualys_list)
                    for diff in symmetric_difference:
                        print('-', diff)
                    print("Total:", len(symmetric_difference),"\n")

                    # clearing the list
                    jfrog_list.clear()
                    qualys_list.clear()

            elif value == 2:
                print("WARNING:", "Any file name that is existing already will be overwriten!")
                 
                print("--------------[JFROG LOGIN]--------------")
                username, password = api_authentication()
                jfrog_auth = HTTPBasicAuth(username,password) 
                print("--------------[QUALYS LOGIN]--------------")
                username, password = api_authentication()
                qualys_auth = HTTPBasicAuth(username,password) 
                repositories = [['b1fs-b1x-docker-buildkite-local','e92b970d-17aa-47b8-833f-4d34fcaec4bc'],['b1fs-b1x-docker-dev-local','7bb778cf-4d89-4e3d-bd84-0ee2dbd873a3']]
                
                jfrog_list, qualys_list = [], []
                
                filename = input("Enter your filename: ")
                if filename:
                    filename = "files_csv/{filename}.csv".format(filename=filename)
                    print("Writting...")
                    with open(filename, 'w', newline='') as file:
                        writer = csv.writer(file)
                        for jfrog, qualys in repositories:
                            # JFrog
                            jfrog_url = "https://blockone.jfrog.io/artifactory/api/docker/{jfrog}/v2/_catalog".format(jfrog=jfrog)
                            jfrog_data = get_fetch(url=jfrog_url,auth=jfrog_auth) 
                            if jfrog_data:
                                writer.writerow(["JFROG"])
                                writer.writerow(['Key',jfrog]) 
                                writer.writerow(['Repositories','']) 
                                repositories = jfrog_data["repositories"]
                                for repository in repositories:
                                    writer.writerow(['',repository])  
                                    jfrog_list.append(repository)
                                writer.writerow(['Total',len(repositories)])   
                            # Qualys
        
                            qualys_url = "https://qualysapi.qg3.apps.qualys.com/csapi/v1.1/registry/{qualys}/repository?pageNo=1&pageSize=200".format(qualys=qualys)
                            qualys_data = get_fetch(url=qualys_url,auth=qualys_auth) 
                            if qualys_data: 
                                qualys_data = qualys_data["data"]
                                writer.writerow(["QUALYS"])
                                writer.writerow(['Registry UUID',qualys])  
                                writer.writerow(['Repository Name','']) 
                                
                                for repoName in qualys_data:
                                    repoName = repoName["repoName"]
                                    writer.writerow(['',repoName])  
                                    qualys_list.append(repoName) 

                                writer.writerow(['Total',len(qualys_data)])  
                        
                            # Symmetric difference
                            
                            writer.writerow(["Symmetric difference"]) 
                            writer.writerow(['Repositories','']) 
                            symmetric_difference = set(jfrog_list) ^ set(qualys_list)
                            for diff in symmetric_difference: 
                                writer.writerow(['',diff]) 
                            writer.writerow(['Total',len(symmetric_difference)])  
                            writer.writerow(['']) 
                            # clearing the list
                            jfrog_list.clear()
                            qualys_list.clear()
                        print("Sucessfully printed to csv!\n")
            elif value == 3:
                os.system("cls")
                print("Returning to main page!!!\n")
                break
            else:
                print("Invalid value!!!\n")
        else:
            os.system("cls")
            print("Invalid value!!!\n")

def post_onboarding_cs_module():
    os.system("cls")
    while True:
       
        print("[----{title}----]".format(title="POST Onboarding CS Module".upper())) 
        print("[1] - All at once \n[2] - Back")
        value = input("Enter your choice: ")
        valid, value = value_checker(value)
        if valid:
            value = int(value)
            if value == 1: 
                print("--------------[JFROG LOGIN]--------------")
                username, password = api_authentication()
                jfrog_auth = HTTPBasicAuth(username,password) 
                print("--------------[QUALYS LOGIN]--------------")
                username, password = api_authentication()
                qualys_auth = HTTPBasicAuth(username,password) 
                repositories = [['b1fs-b1x-docker-buildkite-local','e92b970d-17aa-47b8-833f-4d34fcaec4bc','07:00'],['b1fs-b1x-docker-dev-local','7bb778cf-4d89-4e3d-bd84-0ee2dbd873a3','06:30']]
                repositories = dict(zip([e for e in range(len(repositories))],repositories))
                while True:
                    print("Select the key of your choice:",repositories) 
                    value = input("Enter your choice: ")
                    valid, value = value_checker(value)
                    if valid:
                        value = int(value)
                        choice = repositories.get(value)
                        if choice is not None:  
                            print("->",choice,"Selected!\nFetching...")
                            jfrog, qualys, schedule = choice 
                            jfrog_url = "https://blockone.jfrog.io/artifactory/api/docker/{jfrog}/v2/_catalog".format(jfrog=jfrog)
                            jfrog_data = get_fetch(url=jfrog_url,auth=jfrog_auth) 
                            if jfrog_data:
                                jfrog_list = [data for data in jfrog_data["repositories"]]
                                # print(jfrog_list)

                            qualys_url = "https://qualysapi.qg3.apps.qualys.com/csapi/v1.1/registry/{qualys}/repository?pageNo=1&pageSize=200".format(qualys=qualys)
                            qualys_data = get_fetch(url=qualys_url,auth=qualys_auth) 
                            if qualys_data:  
                                qualys_list = [repoName["repoName"] for repoName in [data for data in qualys_data["data"]] ]
                                # print(qualys_list)
                            symmetric_difference = set(jfrog_list) ^ set(qualys_list)
                            print("Symmteric Difference:\n")
                            for diff in symmetric_difference:
                                print("->",diff)
                            print("Total: ",len(symmetric_difference),"\n")

                            value = input("Do you want to post/onboard this difference: (Y/N)? ")
                            if value.lower() == 'Y'.lower():
                                payload = '''
                                            {
                                                "filters": [
                                                {
                                                    "days":null,
                                                    "repoTags":  [
                                                        {
                                                        "repo":    "b1x-buildkite-cypress-runner",
                                                        "tag":null
                                                        }
                                                    ]
                                                }
                                            ],
                                                "name":   "Automatic Scan Schedule",
                                                "onDemand":  false,
                                                "schedule":   "07:00"
                                            }  
                                          '''
                                for diff in symmetric_difference:
                                    json_payload = json.loads(payload)
                                    json_payload["filters"][0]["repoTags"][0]["repo"] = diff
                                    json_payload["schedule"] = schedule
                                    json_payload = json.dumps(json_payload, indent=4, sort_keys=True)
                                    print(json_payload) 
                                    # Posting
                                    url = "https://qualysguard.qg3.apps.qualys.com/cs/rest/1.0/registry/{qualys}/schedule".format(qualys=qualys)
                                    """
                                    Pre itong line 350 and 351 uncomment mo para ma post ung mga registries para ma try mo ma test mo
                                    """
                                    #   request = requests.request("POST", url, headers={}, data=json_payload, auth=qualys_auth) 
                                    #   print(request.text) 
                                    print(url)
                            else:
                                os.system("cls")
                                print("Cancelling returning to main...")
                                break
                            # Posting
                            break
                        else:
                            os.system("cls")
                            break
                            print("Invalid key!!!")
                    else:
                        os.system("cls")
                        print("Invalid value!!!\n") 
            elif value == 2:
                os.system("cls")
                print("Returning to main page!!!\n")
                break
            else:
                print("Invalid value!!!\n")
        else:
            os.system("cls")
            print("Invalid value!!!\n")

    
