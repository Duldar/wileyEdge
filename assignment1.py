Size = {
    "small": 2,
    "medium": 3,
    "large": 4,
}
coffee_type = {
    "brewed": 0,
    "espresso": 0.5,
    "cold brew": 1,
}
flavouring = {
    "none": 0,
    "caramel": 0.5,
    "hazelnut": 0.5,
    "vanilla": 0.5,
}
order_size = input("Do you want small, medium, or large?")
if order_size == "small":
    print("one small coffee")
if order_size == "medium":
    print("one medium coffee")
if order_size == "large":
    print("one large coffee")

order_coffee_type = input("Do you want brewed, espresso, or cold brew?")
if order_coffee_type == "brewed":
    print("as a brewed coffee")
if order_coffee_type == "espresso":
    print("as an espresso coffee")
if order_coffee_type == "cold brew":
    print("as a cold brew")
order_flavouring = input("Do you want hazelnut, vanilla, caramel or none?")
if order_flavouring == "hazelnut":
    print("with hazelnut flavouring")
if order_flavouring == "vanilla":
    print("with vanilla flavouring")
if order_flavouring == "caramel":
    print("with caramel flavouring")
if order_flavouring == "none":
    print("with no flavouring")

total_order = input(
    "you asked for a {}, {}, {}!".format(order_size, order_coffee_type, order_flavouring + " yes or no?"))
if total_order == "yes":
    total = int()
    print(f"your total is :", Size[order_size]+coffee_type[order_coffee_type]+flavouring[order_flavouring])
else:
    print("can i take your order again?")
