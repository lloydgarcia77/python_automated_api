
import os
from handy_tools import value_checker
from functionalities import jfrog_registries_repositories,  qualys_repositories, all_onboarded_difference_repositories

loop = True 

while loop: 
    print("\n[----QUALYS AUTOMATED API JSON----]")
    print("[1] - JFrog Registries & Repositories \n[2] - Qualys Repositories \n[3] - All, Onboarded, & Difference Repositories \n[4] - POST Onboarding CS Module \n[5] - Exit")
    value = input("Enter selected option: ")
    valid, value = value_checker(value)
    if valid:
        value = int(value)
        print(value)
        if value == 1:
            jfrog_registries_repositories()
        elif value == 2:
            qualys_repositories()
        elif value == 3:
            all_onboarded_difference_repositories()
        elif value == 5:
            print("Good Bye!!!\n")
            loop = False
            break
        else: 
            print("Invalid choice!!!\n")
            os.system("cls")
            continue
    else:
        os.system("cls")
        print("Invalid value!!!\n")
