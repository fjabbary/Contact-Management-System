print("Welcome to the Contact Management System! Menu:\n")
print(" 1. Add a new contact\n 2. Edit an existing contact\n 3, Delete a contact\n 4. Search for a contact\n 5. Display all contacts\n 6. Export contacts to a text file 7.Import contacts from a text file\n 8. Quit")  

# Unique ID would be used as a unique identifier


# ===============//  Functions ====================
import uuid, json, ast

all_contacts = {}


def add_contact(contacts):
  id = str(uuid.uuid4())
  contact = {}

  name = input("What is the name of contact? ")
  phone_number = input("What is the phone number of contact? ")
  email = input("What is the email address of contact ")
  additional_info = input("What is the additional information you want to add? ")
  
  # Additional info is an optional field
  if name and email and phone_number:
    contact[id] = {}
    contact[id]["name"] = name
    contact[id]["phone_number"] = phone_number
    contact[id]["email_address"] = email
    contact[id]["additional_info"] = additional_info 
    
    all_contacts.update(contact)
    print("\033[96m", contacts, "\033[0m")
    
  else:
    print("\033[96m", "Name, phone number, and email address is required", "\033[0m") 
  
  
  
def edit_contact(contacts):
   id = input('Enter the id of contact you want to edit: ')
   field = input('Which field do you want to edit? Enter name, phone_number, or email_address: ')
   try:
     print(f"\nYou are about to edit {field} of contact with email address of {contacts[id]["email_address"]}")
     new_val = input("What is the new value? ")
     contacts[id][field] = new_val 
     print("\033[93m", contacts, "\033[0m")  
   except:
     print("\033[31m", "Failed to edit: Make sure you have entered the valid information", "\033[0m") 
  

def delete_contact(contacts):
   id = input('Enter the id of contact you want to delete: ')
   try:
    contacts.pop(id)
    print('\33[45m',f'Contact with email of {contacts[id]["email_address"]} removed from the contacts', "\033[0m")
   except:
     print("\033[31m", "Failed to delete: Make sure you have entered the valid information", "\033[0m") 
  
def search_contact(contacts):
    id = input('Enter the id of contact you want to view: ')
    try:
      print('\33[45m', {contacts[id]}, "\033[0m")
    except:
      print("\033[31m", "Failed to delete: Make sure you have entered the valid information", "\033[0m") 
  

def display_contacts(contacts):
  print("\033[93m", contacts, "\033[0m") 

#export data in the formats of text and JSON
def export_data(contacts):
  with open('contacts.txt', 'w') as file:
      file.write(str(contacts))
  with open('contacts.json', 'w') as file:    
      json.dump(contacts, file, indent=4)


def import_data(contacts):
  with open('contacts.txt') as file:
    data = file.read()
  # converts string to dictionary and add it to all_contacts
  contacts.update((ast.literal_eval(data)))
  


  
def run_app():
    while True:
      action = input("Please choose number associating with the action you want to implement: ")
      if action == "1":
        add_contact(all_contacts)
        
      elif action == "2":
        edit_contact(all_contacts) 
        
      elif action == "3":
        delete_contact(all_contacts)   
        
      elif action == "4":
          search_contact(all_contacts) 
          
      elif action == "5":
        display_contacts(all_contacts)
        
      elif action == "6":
        export_data(all_contacts)
        
      elif action == "7":
        import_data(all_contacts)  
      
      elif action == "8":
        print("\033[32m", all_contacts, "\033[0m")  
        break

      else:
        print('Invalid Number')




run_app()