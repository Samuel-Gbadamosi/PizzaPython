#Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
#Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

#Add pepperoni for small pizza (Y or N): +$2
#Add pepperoni for medium or large pizza (Y or N): +$3
#Add extra cheese for any size pizza (Y or N): +$1

#Example Interaction
#Welcome to Python Pizza Deliveries!
#What size pizza do you want? S, M or L: L
#Do you want pepperoni on your pizza? Y or N: Y
#Do you want extra cheese? Y or N: N
#Your final bill is: $28.
 


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











