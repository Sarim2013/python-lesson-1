print("country and capitals")
capitals={"Netherlands":"Amsterdam",
          "Pakistan":"Islamabad",
          "India":"New Delhi",
          "France":"Paris",
          "Spain":"Madrid"}
ask=input("Enter A Country To Know Its Capital")
if ask in capitals:
    print(capitals[ask])
else:
    print("Not Found :[")