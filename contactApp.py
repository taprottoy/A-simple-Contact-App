import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory


class MyGrid(Widget):

    # inheriting constructor from the superClass widgets
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.contact_list = []

    # getting the size of the arrayList
    def getSize(self):
        return len(self.contact_list)

    # checking whether the list empty or not
    def isEmpty(self):
        return self.getSize() == 0

    # adding the name, number and email to the list
    def add(self, name, number, email):
        self.contact_list.append((name, number,email))

    # removing the given name from list
    def remove(self, name):
        lowercase = name.lower()
        if self.isEmpty():
            return "Oops! No contacts saved to return."

        else:
            for i in range(self.getSize()):
                # checking whether the name provided is within the list or not
                # taking lowercase to avoid any sort of case sensitivity error
                if lowercase == self.contact_list[i][0].lower():
                    self.contact_list.pop(i)
                    break
            else:
                return "Name not in the list!"

    # searches through the list for the given name and returns the info of a contact.
    # returning the info rather than printing because we want this to be printed in our app window not in console.
    def search(self, name):

        if self.isEmpty():
            return ("There is no saved contacts to show.")

        else:
            for i in range (self.getSize()):
                if name.lower() == self.contact_list[i][0].lower():
                    return ("Name: ", str(self.contact_list[i][0]) +
                            "  Phone number: ", str(self.contact_list[i][1]) +
                            "  Email address: ", str(self.contact_list[i][2]))
                    break
            else:
                return ("Name not found within contacts.")


    def addbtn(self):
        # creating button function  so that the user input in the app UI can be added to the contact_list
        name = self.ids.add_name.text
        number = self.ids.add_number.text
        email = self.ids.add_email.text
        if (name != "" and number != "") and email != "":
            self.add(name,number, email)

        # after adding the text, clearing the textinput boxes for next input
        self.ids.add_name.text = ""
        self.ids.add_number.text = ""
        self.ids.add_email.text = ""

    # remove button function to remove item from list
    def removebtn(self):
        name = self.ids.rem_name.text
        a = self.remove(name)
        # after adding the text, clearing the textinput boxes for next input
        self.ids.rem_name.text = ""

    # search button function to remove item from list
    def searchbtn(self):
        name = self.ids.search_name.text
        self.ids.search.text = str(self.search(name))
        self.ids.search_name.text = ""

    # showall contacts button function
    def showall(self):

        id = self.ids.saved.text

        if self.isEmpty():
            self.ids.saved.text = "Sorry! No contacts saved to show as of now."
        else:
            # updating the label of on the app UI so that all the contacts info are shown.
            for i in range(self.getSize()):
                self.ids.saved.text = str(self.info())

    def info(self):
        toString = ""
        info = ""
        new_list = []
        if self.isEmpty():
            info = ""
        else:
            # looping through the contact list elements
            for ele in self.contact_list:
                toString = str(ele)   # converting elements to string property.
                new_list.append(toString)  # crreating a new_list with string of Contacts objects
            for item in new_list:
                # concanating the items on new list as string to show as a single string
                # otherwise the label in app UI doesn't update properly.
                info += "\n" + item

        return info



class My_Contacts_AppApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    My_Contacts_AppApp().run()


# The layout has been styled in .kv file
# .kv file can be added in two ways. One by using a builder method and linking it with the .py file.
# and another by naming the .kv file by taking the app class name without app in it but all small letters.
# I chose the later one.