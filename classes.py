"""
    Create a class named person.
    Declair  brand name and module number of the person class.
    Display properties of the inputed person brand and modle.
    Allow the user to input various enter infromation for a new person.
    Allow the user to rmeove input various enter infromation for a new person.
"""
# person class will collect and store properties inside a phone.
class Person:
    def __init__(self, name, sex, nationality, age=18):
        self.name = name
        self.age = age
        self.sex = sex
        self.nationality = nationality
    def get_name(self):
        return self.name 
    def get_age(self):
        return self.age 
    def get_gender(self):
        return self.sex 
    def get_nationality(self):
        return self.nationality 
        
active_users = Person("Lucy Stephens", "woman", "Canadian", 24)

name = active_users.get_name()
age = active_users.get_age()
gender = active_users.get_gender()
nationality = active_users.get_nationality()

print(f"Hi, my name is {name}. I am a {age} year old {nationality}. My sex is a {gender}. ")