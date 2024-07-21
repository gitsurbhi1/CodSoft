def add():
    print("Enter the name of the contact you wanna add")
    name=input()
    print("Enter the phone number of the contact you wanna add")
    phone=int(input())
    print("Enter the email of the contact you wanna add")
    email=input()
    print("Enter the address of the contact you wanna add")
    address=input()
    contact_book.append({"NAME":name,"PHONE NUMBER":phone,"EMAIL":email,"ADDRESS":address})
    print("You have successfully added a new contact!")
    
def delete():
    while(1):
        print("Choose a number to delete contact\n1.Delete by name\n2.Delete by number\n3.Delete by mail\n4.Delete by address")
        choice=int(input())
        if choice == 1 :
            print("Enter the name you wanna remove")
            n=input()
            for element in contact_book:
                if element["NAME"]==n:
                    contact_book.remove(element)
            break
        elif choice == 2 :
            print("Enter the number you wanna remove")
            n=int(input())
            for element in contact_book:
                if element["PHONE NUMBER"]==n:
                    contact_book.remove(element)
            break
        elif choice == 3 :
            print("Enter the mail you wanna remove")
            n=input()
            for element in contact_book:
                if element["EMAIL"]==n:
                    contact_book.remove(element)
            break
        elif choice == 4 :
            print("Enter the address you wanna remove")
            n=input()
            for element in contact_book:
                if element["ADDRESS"]==n:
                    contact_book.remove(element)
            break
        else:
            print("OOPS! Invalid Choice!\nChoice must be from 1 to 4")

def update():
    while(1):
        print("Choose a number to update contact\n1.Update name\n2.Update number\n3.Update mail\n4.Update address")
        choice=int(input())
        if choice == 1 :
            print("Enter the name you wanna update")
            old=input()
            print("Enter the new name")
            new=input()
            for element in contact_book:
                if element["NAME"]==old:
                    element["NAME"]=new
            break
        elif choice == 2 :
            print("Enter the number you wanna update")
            old=int(input())
            print("Enter the new number")
            new=int(input())
            for element in contact_book:
                if element["PHONE NUMBER"]==old:
                    element["PHONE NUMBER"]=new
            break
        elif choice == 3 :
            print("Enter the mail you wanna update")
            old=input()
            print("Enter the new mail")
            new=input()
            for element in contact_book:
                if element["EMAIL"]==old:
                    element["EMAIL"]=new
            break
        elif choice == 4 :
            print("Enter the address you wanna update")
            old=input()
            print("Enter the new address")
            new=input()
            for element in contact_book:
                if element["ADDRESS"]==old:
                    element["ADDRESS"]=new
            break
        else:
            print("OOPS! Invalid Choice!\nChoice must be from 1 to 4")
    
def search():
    if(len(contact_book)==0):
        print("Your Contact Book Is Empty")
    else:
        while(1):
            print("Choose a number to search contact\n1.Search by name\n2.Search by number\n3.Search by mail\n4.Search by address")
            choice=int(input())
            contact_found = False
            if choice == 1 :
                print("Enter the name you wanna search")
                n=input()
                for contact in contact_book:
                    if contact["NAME"]==n:
                        print(f"NAME:{contact['NAME']},PHONE NUMBER:{contact['PHONE NUMBER']},EMAIL:{contact['EMAIL']},ADDRESS:{contact['ADDRESS']}")
                        contact_found = True
                if not contact_found:
                    print("Contact not found.")
                break
            elif choice == 2 :
                print("Enter the number you wanna search")
                n=int(input())
                for contact in contact_book:
                    if contact["PHONE NUMBER"]==n:
                        print(f"NAME:{contact['NAME']},PHONE NUMBER:{contact['PHONE NUMBER']},EMAIL:{contact['EMAIL']},ADDRESS:{contact['ADDRESS']}")
                        contact_found = True
                if not contact_found:
                    print("Contact not found.")
                break
            elif choice == 3 :
                print("Enter the mail you wanna search")
                n=input()
                for contact in contact_book:
                    if contact["EMAIL"]==n:
                        print(f"NAME:{contact['NAME']},PHONE NUMBER:{contact['PHONE NUMBER']},EMAIL:{contact['EMAIL']},ADDRESS:{contact['ADDRESS']}")
                        contact_found = True
                if not contact_found:
                    print("Contact not found.")
                break
            elif choice == 4 :
                print("Enter the address you wanna search")
                n=input()
                for contact in contact_book:
                    if contact["ADDRESS"]==n:
                        print(f"NAME:{contact['NAME']},PHONE NUMBER:{contact['PHONE NUMBER']},EMAIL:{contact['EMAIL']},ADDRESS:{contact['ADDRESS']}")
                        contact_found = True
                if not contact_found:
                    print("Contact not found.")
                break
            else:
                print("OOPS! Invalid Choice!\nChoice must be from 1 to 4")

def view():
    if(len(contact_book)==0):
        print("Your Contact Book Is Empty")
    else:
        for contact in contact_book:
            print(f"NAME:{contact['NAME']},PHONE NUMBER:{contact['PHONE NUMBER']},EMAIL:{contact['EMAIL']},ADDRESS:{contact['ADDRESS']}")
          
print("Enter 1 to create your contact book")
create_book=int(input())
if(create_book==1):
    contact_book=[]
    
while(True):
    print("\nWANNA UPDATE YOUR CONTACT BOOK?")
    print("Enter your choice:")
    print("1.Add Contact")
    print("2.Delete Contact")
    print("3.Update Contact")
    print("4.Search Contact")
    print("5.View Contact List")
    print("6.Exit\n")
    choice=int(input())
    if choice == 1 :
        add()
    elif choice == 2 :
        delete()
    elif choice == 3 :
        update()
    elif choice == 4 :
        search()
    elif choice == 5 :
        view()
    elif choice == 6 :
        print("THANKS FOR USING CONTACT BOOK")
        break
    else:
        print("OOPS! Invalid Choice!\nChoice must be from 1 to 6")    
         
    