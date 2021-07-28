#imporrting used libraries
from datetime import date
import os
from os import system
system("title " + "@c9zd - Age Calculator")

print("""
    
░█████╗░░██████╗░███████╗  ░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░██╗
██╔══██╗██╔════╝░██╔════╝  ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║
███████║██║░░██╗░█████╗░░  ██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝██║
██╔══██║██║░░╚██╗██╔══╝░░  ██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗╚═╝
██║░░██║╚██████╔╝███████╗  ╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║██╗
╚═╝░░╚═╝░╚═════╝░╚══════╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝
    """)
print("""
Cᴏᴅᴇᴅ Bʏ Aʜᴍᴇᴅ Iɴsᴛᴀ: @c9zd
""")

def age(birth_date): #defining the way age is calculated
    today = date.today()
    y = today.year - birth_date.year
    if today.month < birth_date.month or today.month == birth_date.month and today.day < birth_date.day:
        y -= 1

    return y

def main_calculator(): #main calculator definition
    Name = input("Tell us Your Name: ")
    while True: #to make sure the user only enters numbers as input
        try:
            year = int(input("Enter Your Year of Birth: "))
        except:
            print("Value must be a number!")
            continue
        else: break
    while True: #to make sure the user only enters numbers as input
        try:
            month = int(input("Enter Your Month of Birth: "))
        except:
            print("Value must be a number!")
            continue
        else: break
    while True: #to make sure the user only enters numbers as input
        try:
            day = int(input("Enter Your Day of Birth: "))
        except:
            print("Value must be a number!")
            continue
        else: break

    birth_date = date(int(year),int(month),int(day)) #defining entered birth date 

    age_years = age(birth_date)
    
    print("Hello "+ Name)
    print("You are "+ str(age_years) + " years old")

while 1: #Main Loop
    startQ = input("Want me to Calculate Your Age? ").lower()
    if startQ == "yes":
        main_calculator()
    else:
        break

