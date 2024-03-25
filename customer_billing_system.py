vegetables={'carrot':50,'onion':100,'potato':90,'tomato':60}
chips={'kurkure':20,'lays':20,'cheetos':35,'Doritos':30}
Sweets={"Kit-Kat":20,"Dairy Milk":50,"M&M's":95,"Hershey's Kisses":50}
Biscuits={'oreo':30,"hide and seek":20,'parle-g':5,'bourbon':50,'Dark Fantasy':40}


cart_items=[]
cart_quantity=[]
cart_price=[]
c=0
print("Welcome to YESrm foods")
while True:
  print("Which section would you like to browse")
  o=int(input("1.Vegetables \n2.Chips \n3.Chocolates \n4.Biscuits \n5.Check out \n"))
  
  cost=0
  if (o==1) :
    print("Available Vegetables : ")
    for i in (vegetables):
      print(i,"price ",vegetables[i])
   
    while True:
      v=int(input("What do you want to add to cart(in int) :"))
      if(v==1):
        cart_items.append("carrot")
        q=int(input("How many do you want"))
        cart_quantity.append(q)
        price=vegetables.get("carrot")
        cart_price.append(price)
        cost+=price*q          
        cn=input("Do you wish to continue to browse vegetables (y/n): ")
        print("\n")
        if(cn=="n"):
          break
        elif(cn=='y'):
          v=int(input("What do you want to add to cart(in int) :"))        
          
      if(v==2):
        cart_items.append("onion")
        q=int(input("How many do you want"))
        cart_quantity.append(q)
        price=vegetables.get("onion")
        cart_price.append(price)
        cost+=price*q
        cn=input("Do you wish to continue to browse vegetables (y/n): ")
        print("\n")
        if(cn=="n"):
            break
        elif(cn=='y'):
          v=int(input("What do you want to add to cart(in int) :"))        
          
      
      if(v==3):
        cart_items.append("potato")
        q=int(input("How many do you want"))
        cart_quantity.append(q)
        price=vegetables.get("potato")
        cart_price.append(price)
        cost+=price*q
        cn=input("Do you wish to continue to browse vegetables (y/n): ")
        print("\n")
        if(cn=="n"):
          break
        elif(cn=='y'):
          v=int(input("What do you want to add to cart(in int) :"))        
          
      


      if(v==4):
        cart_items.append("tomato")
        q=int(input("How many do you want"))
        cart_quantity.append(q)
        price=vegetables.get("tomato")
        cart_price.append(price)
        cost+=price*q
        cn=input("Do you wish to continue to browse vegetables (y/n): ")
        print("\n")
        if(cn=="n"):
          break
        elif(cn=='y'):
          v=int(input("What do you want to add to cart(in int) :"))
          
  if (o==2) :
    print("Available Chips : ")
    for i in (chips):
      print(i,"price ",chips[i])
   
    while True:
      v=int(input("What do you want to add to cart(in int) :"))
      if(v==1):
        cart_items.append("kurkure")
        q=int(input("How many do you want"))
        cart_quantity.append(q)
        price=chips.get("kurkure")
        cart_price.append(price)
        cost+=price*q          
        cn=input("Do you wish to continue to browse Chips (y/n): ")
        print("\n")
        if(cn=="n"):
          break
        elif(cn=='y'):
          v=int(input("What do you want to add to cart(in int) :"))        
          
      if(v==2):
        cart_items.append("lays")
        q=int(input("How many do you want"))
        cart_quantity.append(q)
        price=chips.get("lays")
        cart_price.append(price)
        cost+=price*q
        cn=input("Do you wish to continue to browse Chips (y/n): ")
        print("\n")
        if(cn=="n"):
            break
        elif(cn=='y'):
          v=int(input("What do you want to add to cart(in int) :"))        
          
      
      if(v==3):
        cart_items.append("cheetos")
        q=int(input("How many do you want"))
        cart_quantity.append(q)
        price=chips.get("cheetos")
        cart_price.append(price)
        cost+=price*q
        cn=input("Do you wish to continue to browse Chips (y/n): ")
        print("\n")
        if(cn=="n"):
          break
        elif(cn=='y'):
          v=int(input("What do you want to add to cart(in int) :"))        
          
      


      if(v==4):
        cart_items.append("doritos")
        q=int(input("How many do you want"))
        cart_quantity.append(q)
        price=chips.get("doritos")
        cart_price.append(price)
        cost+=price*q
        cn=input("Do you wish to continue to browse vegetables (y/n): ")
        print("\n")
        if(cn=="n"):
          break
        elif(cn=='y'):
          v=int(input("What do you want to add to cart(in int) :"))                
        
  
  
  if (o==3) :
    print("Available Sweets : ")
    for i in (Sweets):
      print(i,"price ",Sweets[i])
   
    while True: 
      v=int(input("What do you want to add to cart(in int) :"))
      if(v==1):
        cart_items.append("Kit Kat")
        q=int(input("How many do you want"))
        cart_quantity.append(q)
        price=vegetables.get(Kit-Kat)
        cart_price.append("price")
        cost+=price*q          
        cn=input("Do you wish to continue to browse Sweets (y/n): ")
        print("\n")
        if(cn=="n"):
          break
        elif(cn=='y'):
          v=int(input("What do you want to add to cart(in int) :"))        
          
      if(v==2):
        cart_items.append("onion")
        q=int(input("How many do you want"))
        cart_quantity.append(q)
        price=vegetables.get("onion")
        cart_price.append(price)
        cost+=price*q
        cn=input("Do you wish to continue to browse vegetables (y/n): ")
        print("\n")
        if(cn=="n"):
            break
        elif(cn=='y'):
          v=int(input("What do you want to add to cart(in int) :"))        
          
      
      if(v==3):
        cart_items.append("potato")
        q=int(input("How many do you want"))
        cart_quantity.append(q)
        price=vegetables.get("potato")
        cart_price.append(price)
        cost+=price*q
        cn=input("Do you wish to continue to browse vegetables (y/n): ")
        print("\n")
        if(cn=="n"):
          break
        elif(cn=='y'):
          v=int(input("What do you want to add to cart(in int) :"))        
          
      


      if(v==4):
        cart_items.append("tomato")
        q=int(input("How many do you want"))
        cart_quantity.append(q)
        price=vegetables.get("tomato")
        cart_price.append(price)
        cost+=price*q
        cn=input("Do you wish to continue to browse vegetables (y/n): ")
        print("\n")
        if(cn=="n"):
          break
        elif(cn=='y'):
          v=int(input("What do you want to add to cart(in int) :"))        


  if (o==4) :
    print("Available Biscuits : ")
    for i in (Biscuits):
      print(i,"price ",Biscuits[i])
   
    while True:
      v=int(input("What do you want to add to cart(in int) :"))
      if(v==1):
        cart_items.append("oreo")
        q=int(input("How many do you want"))
        cart_quantity.append(q)
        price=chips.get(oreo)
        cart_price.append(price)
        cost+=price*q          
        cn=input("Do you wish to continue to browse Biscuits (y/n): ")
        print("\n")
        if(cn=="n"):
          break
        elif(cn=='y'):
          v=int(input("What do you want to add to cart(in int) :"))        
          
      if(v==2):
        cart_items.append("hide and seek")
        q=int(input("How many do you want"))
        cart_quantity.append(q)
        price=chips.get("hide and seek")
        cart_price.append(price)
        cost+=price*q
        cn=input("Do you wish to continue to browse Biscuits (y/n): ")
        print("\n")
        if(cn=="n"):
            break
        elif(cn=='y'):
            v=int(input("What do you want to add to cart(in int) :"))        
          
      
      if(v==3):
        cart_items.append("parle-g")
        q=int(input("How many do you want"))
        cart_quantity.append(q)
        price=chips.get("parle-g")
        cart_items_price.append(price)
        cost+=price*q
        cn=input("Do you wish to continue to browse parle-g (y/n): ")
        print("\n")
        if(cn=="n"):
          break
        elif(cn=='y'):
          v=int(input("What do you want to add to cart(in int) :"))        
          
      


      if(v==4):
        cart_items.append("bourbon")
        q=int(input("How many do you want"))
        cart_quantity.append(q)
        price=chips.get("bourbon")
        cart_price.append(price)
        cost+=price*q
        cn=input("Do you wish to continue to browse Biscuits (y/n): ")
        print("\n")
        if(cn=="n"):
          break
        elif(cn=='y'):
            v=int(input("What do you want to add to cart(in int) :"))
  if(o==5):
    print("Bill is")
    print("Items \t Quantity \t Price")
    for i in range(len(cart_items)):
      print(cart_items[i]," \t",cart_quantity[i],"\t\t",cart_price[i])
      c+=cart_quantity[i]*cart_price[i]
    print("Total cost",c)
    break