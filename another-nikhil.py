import random

user_name=[]
username=['nambi', 'nikhil']
password=['nambi', 'nikhil']

def available_bus():
    bus_index = 0
    bus_no = 0
    buses_available=['A2', 'B6', 'S2']
    bus_destination=['Nagercoil', 'Kottaram', 'Mylaudy']
    departure = ['16:00', '12:00', '00:00']
    arrival = ['17:00', '20:00', '02:45']
    for i in buses_available:
        bus_index += 1
        print(f"{bus_index}. {i}")
    buss_no = input("Enter bus number: ")
    bus_no = int(buss_no) - 1
    print(f"Bus Details \nBus Name: {buses_available[bus_no]} \nDestination: {bus_destination[bus_no]} \nDeparture Time: {departure[bus_no]} \nArrival Time: {arrival[bus_no]} \n")
    
while True:
    what = input("Welcome to Nikhil Travels! \nTo Login enter 1 \nTo create a new account enter 2: ")
    if what == "1":
        print ("Enter login details")
        usrn = input("Enter username: ").lower()
        pasw = input("Enter password: ").lower()
        if usrn in username and pasw in password:
            print("You are logged in!")
            available_bus()
            break
        else:
            print("Account not found!")
    if what == "2":
        usrn = input("Enter username: ").lower()
        pasw = input("Enter password: ").lower()
        username.append(usrn)
        password.append(pasw)