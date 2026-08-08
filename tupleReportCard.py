#name,math,eng,dutch,science
report_card1=("Sarim",100,100,100,99)
report_card2=("Tanshi",87,98,93,94)


name=input("Enter Your Name: ").capitalize()
if name in (report_card1[0],report_card2[0]):
    print("you got it!")
else:
    print("Name Not Found In Record")