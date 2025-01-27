smallPizza = 15
mediumPizza = 20
largePizza = 25

pepperoniSmall = 2
pepperoniBigorMedium = 3
extraCheesePrice = 1

totalprice = 0


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")

if(size == 's'):
    #user that wants a small pizza
    print(f"The cost of your small python pizza is $ {smallPizza}")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if (pepperoni == 'y'):
        totalprice = smallPizza + pepperoniSmall
        print(f"The cost is $: {totalprice}")
    elif(pepperoni == 'n'):
       totalprice = smallPizza
       print(f"The cost is $: {totalprice}")

    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if(extra_cheese == 'y'):
            totalprice += extraCheesePrice
            print(f"The total cost of your pizza is $: {totalprice}")
    elif(extra_cheese == 'n') :
        print(f"The total cost of your pizza is $: {totalprice}")
    else:
        print('....')
elif(size == 'm'):
    #for use that wants a medium pizza
    print(f"The cost of your Medium python pizza is $ {mediumPizza}")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if(pepperoni == 'y'):
        totalprice = mediumPizza + pepperoniSmall
        print(f"The cost is $: {totalprice}")
    elif(pepperoni != 'y'):
        totalprice = mediumPizza

    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if (extra_cheese == 'y'):
        totalprice += extraCheesePrice
        print(f"The total cost of your pizza is $: {totalprice}")
    else:
        print(f"The total cost of your pizza is $: {totalprice}")

elif(size == 'l'):
    #if user choose a large pizza
    print(f"The cost of your Large python pizza is $ {largePizza}")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if (pepperoni == 'y'):
        totalprice = largePizza + pepperoniSmall
        print(f"The cost is $: {totalprice}")
    elif (pepperoni != 'y'):
        totalprice = largePizza

    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if (extra_cheese == 'y'):
        totalprice += extraCheesePrice
        print(f"The total cost of your pizza is $: {totalprice}")
    else:
        print(f"The total cost of your pizza is $: {totalprice}")







#pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
#extra_cheese = input("Do you want extra cheese? Y or N: ")







