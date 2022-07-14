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
        
active_users = Person("Justin", "male", "Canada", 24)

print(f"Hi, my name is {active_users.get_name()}. I am a {active_users.get_age()} {active_users.get_gender()} born in {active_users.get_nationality()}")