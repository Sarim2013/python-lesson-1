print("Welcome To My Restaurant!")
Menu={"Burger":"9,99$",
          "Burger Menu":"12,99$",
          "Nuggets":"5,99$",
          "Nuggets Menu":"8,99$",
          "Wings":"7,99$",
          "Wings Menu":"10,99"}
ask=input("Enter A Dish To Know Its Price ").capitalize()
if ask in Menu:
    print(Menu[ask])
else:
    print("Not On The Menu :[")