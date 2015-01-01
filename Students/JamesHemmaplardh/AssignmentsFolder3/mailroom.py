#!/usr/bin/env python 

Donators = {
    u"James Hemmaplardh": [10, 50, 900],
    u"Bill Gates": [999, 9999, 999],
    u"The Batman": [1],
    u"Dash Berlin": [10, 5],
    u"Avicii Levels": [69, 99, 101] 
    }

def send_thankyou():
    while True:
        name = raw_input(u"Enter 'list' for a list of donor names. Enter First and Last name:")
        if name == u"list":
            print Donators
        else:
            Donators[name]=[]
            return name

def collect_donation(DonorName):
    while True:
        name = int(raw_input(u"Enter the donation ammount:"))
        try:
            name <= 0
        except ZeroDivisionError:
            value = float(u'infinity')
        for i in Donators:
                if i == DonorName:
                    Donators[i].append(name)
                    return name
        else:
            print u"Enter an integer:"

def send_ThankYou(DonorName, name):
    print u"Dear %s,"%(DonorName)
    print u"    Thank you for your donation of $%s."%(name)
    print u"                            Regards, The NSA"

def create_report():
    report = []
    for i in Donators:
        report.append([i,sum(Donators[i]), len(Donators[i]), (sum(Donators[i])/len(Donators[i]))])
        report.sort(key=lambda i: i[1])
    for i in report:
        print (u"DonorName:%s, TotalDonated:$%i, Donations:%i, AverageDonation:$%i" % (i[0], i[1], i[2], i[3]))

while True:
    user_choice = raw_input(u"Enter '1' ,'2' or '3'. 1 to Send a ThankYou, 2 to Create a Report, 3 to exit:")
    if user_choice == u"1":
        DonorName = send_thankyou()
        name = collect_donation(DonorName)
        send_ThankYou(DonorName,name)
    elif user_choice == u"2":
        create_report()
    elif user_choice == u"3":
        print u"The program will now terminate."
        break
    else:
        continue 