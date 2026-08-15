#City Name, Ticket Price Per Person, Money For Food Per Person, Hotel Price Per Person A Night, Overall /10 Rating
France=("Paris",250,100,50,8)
NetherLands=("Amsterdam",100,70,30,8)
America=("Newyork",300,150,100,7)
Russia=("Moscow",200,50,40,9)
Uae=("Dubai",250,100,80,10)

city=input("Enter The City You Want To Go To ").capitalize()
if city in (France[0],NetherLands[0],America[0],Russia[0],Uae[0]):
    print("You Can Go There!")
else:
    print("Sorry, Not On The List Yet")