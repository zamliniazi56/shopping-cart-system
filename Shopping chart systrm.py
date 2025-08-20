
# Ek shopping cart system banao jahan user items add/remove/update kar sake list me.

Cart = []
print(Cart)

while True:
    choice = input(f"You want to Add,Remove,Update or Exit:")

    if choice == "Add":
        item = input("Enter an item u want to add in your chart:")
        Cart.append(item)
        print(f"you added {item} in ur chart")
        print(Cart)
    elif choice == "Remove":
        item = input("Enter an item u want to remove in your chart:")
        if item in Cart:
            Cart.remove(item)
            print(f"you removed {item} from ur chart")
        else:
            print("This item is not present in ur cart")
        print(Cart)

    elif choice == "Update":
        item = input("Enter an item u want to update in your chart:")
        if item in Cart:
            new_item = input("Enter an updated item:")
            Cart.remove(item)
            Cart.append(new_item)
            print(f"you update {new_item} in ur chart to {item}")
        else:
            print("This item is not present in ur cart")
        print(Cart)

    elif choice == "Exit":
        print("exiting.........!!!!!")
        break

    else:
        print("invalid choice")
