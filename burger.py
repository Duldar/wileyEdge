# mohamed duldar 26/09/2022
# implement the classes listed below
class FoodItem:
    pass


class Burger(FoodItem):
    burgers = {
        "cheeseburger": 3.75,
        "veggie": 4.75,
        "plain": 3.25,
        "fillet-o-fish": 3.50
    }
    pass


class Drink(FoodItem):
    drinks = {
        "fanta": 3.25,
        "coke": 3.25,
        "diet coke": 3.75,
        "lipton": 3.50,
        "water": 2.25
    }
    pass


class Side(FoodItem):
    sides = {
        "fries": 2.45,
        "onion rings": 2.45,
        "hash browns": 2.75,
        "salad bag": 1.50
    }
    pass


class Combo(FoodItem):
    combo = {
        "combo 1": 6.25,
        "combo 2": 6.35,
        "combo 3": 6.45,
        "combo 4": 7.25,
        "combo 5": 7.35,
        "combo 6": 7.45,
        "combo 7": 8.25,
        "combo 8": 8.35,
        "combo 9": 8.45
    }
    pass


class Order:
    order = []
    burgerOrder = ""
    drinkOrder = ""
    sideOrder = ""
    mealOrder = ""
    total = 0


def user_input_burger():
    b = Burger()
    o = Order()

    while True:
        if o.burgerOrder in b.burgers.keys():
            sauce = False
            while not sauce:
                extra = input('would you like some sauce for 75p? (Please enter yes or no)')
                if extra == "yes":
                    o.total += 0.75
                    print(" Sauce: £" + str(o.total))
                    sauce = True
                elif extra == "no":
                    print(" No sauce £" + str(o.total))
                    sauce = True
                    break
                else:
                    print("Please only enter 'yes' or 'no'")
            o.total += b.burgers[o.burgerOrder.lower()]
            print(o.burgerOrder.capitalize() + " total: £" + str(o.total))
            theBurgerOrder = o.burgerOrder, o.total
            break
        else:
            o.burgerOrder = input("Would you like cheeseburger, veggie, fillet-o-fish or plain?")

    return theBurgerOrder


def user_input_drink():
    d = Drink()
    o = Order()

    while True:
        if o.drinkOrder in d.drinks.keys():
            ice = False
            while not ice:
                extra = input('Upgrade to large or X-large? (Please enter L or XL)').capitalize()
                if extra == "L":
                    o.total += 0.75
                    print(" Large: £" + str(o.total))
                    ice = True
                elif extra == "Xl":
                    o.total += 1.25
                    print(" XLarge: £" + str(o.total))
                    ice = True
                    break
                else:
                    print("Please only enter 'L' or 'XL'")
            o.total += d.drinks[o.drinkOrder.lower()]
            print(o.drinkOrder.capitalize() + " total: £" + str(o.total))
            theDrinkOrder = o.drinkOrder, o.total
            break
        else:
            o.drinkOrder = input("Would you like a fanta, coke, diet coke,lipton or water?")

    return theDrinkOrder


def user_input_side():
    s = Side()
    o = Order()

    while True:
        if o.sideOrder in s.sides.keys():
            salt = False
            while not salt:
                extra = input('Salt on it for 5p? (Please enter yes or no)')
                if extra == "yes":
                    o.total += 0.05
                    print(" Salt: £" + str(o.total))
                    salt = True
                elif extra == "no":
                    print(" No salt: £" + str(o.total))
                    salt = True
                    break
                else:
                    print("Please only enter 'yes' or 'no'")
            o.total += s.sides[o.sideOrder.lower()]
            print(o.sideOrder.capitalize() + " total: £" + str(o.total))
            theSideOrder = o.sideOrder, o.total
            break
        else:
            o.sideOrder = input("Would you like fries, onion rings, salad bag or hash browns?")

    return theSideOrder


def user_input_combo():
    c = Combo()
    o = Order()

    comboMenu = (
        " Combo menu: (please enter 'combo' followed by the number) \n Combo 1: plain burger, fries, drink \n Combo 2: cheeseburger, fries, drink \n Combo 3: veggie burger, fries, drink \n Combo 4: plain burger, onion rings, drink \n Combo 5: cheeseburger, onion rings, drink \n Combo 6: veggie burger, onion rings, drink \n Combo 7: plain burger, hash browns, drink \n Combo 8: cheeseburger, hash browns, drink \n Combo 9: veggie burger, hash browns, drink")
    print(comboMenu)
    while True:
        if o.mealOrder in c.combo.keys():
            o.total += c.combo[o.mealOrder.lower()]
            comboMeal = o.mealOrder, o.total
            print(str(o.mealOrder).capitalize() + " comes to: £" + str(o.total))
            break
        else:
            o.mealOrder = input(comboMenu)
    return comboMeal


def take_order():
    print("Welcome to Burger Shop")
    newOrder = Order()
    cust = input("What is your name so we can add it to the order?").capitalize()
    print("Hello " + str(cust))
    orderComplete = False
    while not orderComplete:
        finished = ''
        correct = False
        while correct == False:
            nextItem = input("Would you like a burger, a side, drink or a combo meal? To cancel press c")
            nextItem = nextItem.lower()
            if nextItem == "burger":
                newOrder.order.append(user_input_burger())
                correct = True
            elif nextItem == "side":
                newOrder.order.append(user_input_side())
                correct = True
            elif nextItem == "drink":
                newOrder.order.append(user_input_drink())
                correct = True
            elif nextItem == "combo":
                newOrder.order.append(user_input_combo())
                correct = True
            elif nextItem == "c":
                print("Order cancelled. Have a nice day!")
                orderComplete = True
                finished = 'no'
                break
            else:
                print("Please only choose from burger, side, drink or combo.")
        while finished != "yes" and finished != "no":
            finished = input("Is that everything? To cancel press c")
            if finished == "yes":
                orderComplete = True

                def spliting(x):
                    theOrder = []
                    thePrice = []
                    for a, b in x:
                        theOrder.append(a)
                        thePrice.append(b)
                    return (theOrder, thePrice)

                a, b = spliting(newOrder.order)
                price = str(sum(b))
                order = ", ".join(a).capitalize()
                print(cust + ", your order is: " + order)
                print("The total price is £" + price)
                print("Have a nice day!")
            elif finished == "no":
                orderComplete = False
            elif finished == "c":
                print("Order cancelled. Have a nice day!")
                orderComplete = True
                break
            else:
                print("Please enter ""yes"", ""no"", or ""c"". ")


take_order()