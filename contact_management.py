print("Welcome to the Contact Management System! Menu:\n")
print(" 1. Add a new contact\n 2. Edit an existing contact\n 3, Delete a contact\n 4. Search for a contact\n 5. Display all contacts\n 6. Export contacts to a text file\n 7. Import contacts from a text file\n 8. Quit")  


# ===============//  Functions ====================
import uuid, json, ast, re

all_contacts = {}

def add_contact(contacts):
# Unique ID would be used as a unique identifier
  contact = {}

  name = input("What is the name of contact? ").strip()
  phone_number = input("What is the phone number of contact? ").strip()
  email = input("What is the email address of contact ").strip()
  additional_info = input("What is the additional information you want to add? ").strip()
  category = input("What is the category of contact? ").strip()
  
  name_regex = r"[a-zA-Z]{3,}"
  phone_number_regex = r"\d{3}-\d{3}-\d{4}"
  email_regex = r"\b[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}\b"
  
  # Additional info is an optional field
  # Field validations can be done one by one. In this case, it was done for all fields after adding contact
  if re.match(name_regex, name) and re.match(phone_number_regex, phone_number) and re.match(email_regex, email):
      id = str(uuid.uuid4())
    
      contact[id] = {}
      contact[id]["name"] = name 
      contact[id]["phone_number"] = phone_number
      contact[id]["email_address"] = email 
      contact[id]["additional_info"] = additional_info
      contact[id]["category"] = []
      contact[id]["category"].append(category)
      
      custom_field = input("Do you want to add custom field? (yes/no) ")
      if custom_field == "yes":
        key = input("Enter the custom field name: ")
        value = input(f"Enter the value for {key}: ")
        contact[id][key] = value
       
      all_contacts.update(contact)
      print("\033[92m", "=========== Contact added successfully! =============" , "\033[0m")
      
  else:  
      print("\033[31m", "=========== Contact was not added =============" , "\033[0m")
      print("\033[31m", "Name has to be at least 3 characters", "\033[0m")
      print("\033[31m", "Phone number has to be in the format of 111-222-3333", "\033[0m")
      print("\033[31m", "Email has to be in this format: example@domain.com, only dash and dot are allowed", "\033[0m")
    
      print("\033[96m", contacts, "\033[0m")
  
  
 # Contact can be found by any proeprty. In below functions edit and delete, it is bases on ID, and search contact function finds match contact based on email 
def edit_contact(contacts):
   id = input('Enter the id of contact you want to edit: ')
   field = input('Which field do you want to edit? Enter name, phone_number, email_address, additional_info, or category: ')
   if field != "category":
      try:
        print(f"\nYou are about to edit {field} of contact with email address of {contacts[id]["email_address"]}")
        new_val = input("What is the new value? ")
        contacts[id][field] = new_val 
        print("\033[93m", contacts, "\033[0m")  
      except:
        print("\033[31m", "Failed to edit: Make sure you have entered the valid information", "\033[0m") 
    
   elif field == "category":
     action = input("Do you want to add new category or delete existing one? (add/delete): ")
     if action == "add":
       new_val = input("What is the new category you want to add? ")
       if new_val not in contacts[id][field]:
         contacts[id][field].append(new_val)
         
     elif action == "delete":
       new_val = input("What is the category you want to delete? ")
       contacts[id][field].remove(new_val)
         

def delete_contact(contacts):
   id = input('Enter the id of contact you want to delete: ')
   email_copy = contacts[id]["email_address"]
   try:
      contacts.pop(id)
      print('\033[92m',f'Contact with email of {email_copy} removed from the contacts', "\033[0m")
   except:
      print("\033[31m", "Failed to delete: Make sure you have entered the valid information", "\033[0m") 
  
  
  
def search_contact(contacts):
    
    found_contact = {}
    contact_found = False
    
    # Define function for usability and follow DRY principle 
    def loop_find_contact(field, criteria):
     nonlocal contact_found
     for contact in contacts.values():
        if contact[field] == criteria:
          contact_found = True
          found_contact.update(contact)
          print("\033[93m", found_contact, "\033[0m") 
    
    search_criteria = input("Enter your search criteria: Ex. name, phone, email, or additional_info ")
    if search_criteria == "name":
      name = input("Enter the name of contact you want to view: ")
      loop_find_contact("name", name)
      
    if search_criteria == "email":
      email = input('Enter the email of contact you want to view: ')
      loop_find_contact("email", email) 
          
    if search_criteria == "phone":
      phone = input('Enter the phone number (ex. ###-###-####) of contact you want to view: ')
      loop_find_contact("phone_number", phone)    
          
    if search_criteria == "additional_info":
      additional_info = input('Enter the additional info related to the contact that you want to view: ')
      loop_find_contact("additional_info", additional_info)         
        
    if not contact_found:
        print("\033[31m", "Failed to find contact: Make sure you have entered the valid email address", "\033[0m") 
    

def display_contacts(contacts):
  sort_status = input("Enter 'or', 'asc', 'desc' to view contacts in original, ascending, or descending order respectively: ")
  if sort_status == 'or':
    print("\033[93m", contacts, "\033[0m")
    
  elif sort_status == 'asc':
    sort_criteria = input("Enter sort criteria. Ex. name, email_address, or phone_number: ")
    print("\033[93m", {k: v for k, v in sorted(contacts.items(), key=lambda item: item[1][sort_criteria])}, "\033[0m")   

  elif sort_status == 'desc':
    sort_criteria = input("Enter sort criteria. Ex. name, email_address, or phone_number: ")
    print("\033[93m",  {k: v for k, v in sorted(contacts.items(), key=lambda item: item[1][sort_criteria], reverse=True)},  "\033[0m" ) 


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
    my_dict = ast.literal_eval(data)
    contacts.update(my_dict)


# =========================|| Run App ||========================== 
  
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
        print("\033[31m",'Invalid Number',"\033[0m")


run_app()