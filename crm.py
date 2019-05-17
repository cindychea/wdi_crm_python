from contact import Contact

class CRM:

  def main_menu(self):
    while True: 
      self.print_main_menu()
      user_selected = int(input())
      self.call_option(user_selected)

  def print_main_menu(self):
    print('[1] Add a new contact')
    print('[2] Modify an existing contact')
    print('[3] Delete a contact')
    print('[4] Display all the contacts')
    print('[5] Search by attribute')
    print('[6] Exit')
    print('Enter a number: ')


  def call_option(self, user_selected):
    if user_selected == 1:
      self.add_new_contact()
    elif user_selected == 2:
      self.modify_existing_contact()
    elif user_selected == 3:
      self.delete_contact()
    elif user_selected == 4:
      self.display_all_contacts()
    elif user_selected == 5:
      self.search_by_attribute()
    elif user_selected == 6:
      exit()
    
  def add_new_contact(self):
    print('Enter First Name: ')
    first_name = input()
    print('Enter Last Name: ')
    last_name = input()
    print('Enter Email Address: ')
    email = input()
    print('Enter a Note: ')
    note = input()
    Contact.create(first_name, last_name, email, note)
  
  def modify_existing_contact(self):
    print('Please enter an id for the contact to be modified.')
    id = input()
    Contact.find(id)
    print('Please enter the attribute to be changed.')
    update_attribute = input()
    print('Please enter the new value for the attribute.')
    update_value = input()
    Contact.update(self, update_attribute, update_value)
  
  def delete_contact(self):
    print('Please enter an id for the contact to be deleted.')
    id = input()
    Contact.find(id)
    Contact.delete(self)
  
  def display_all_contacts(self):
    Contact.all()
  
  def search_by_attribute(self):
    print('Please enter the attribute you want to search by.')
    attribute = input()
    print('Please enter the search term.')
    value = input()
    Contact.find_by(attribute, value)

a_crm_app = CRM()
a_crm_app.main_menu()