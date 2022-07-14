"""
    Create a class named person.
    Declair  brand name and module number of the person class.
    Display properties of the inputed person brand and modle.
    Allow the user to input various enter infromation for a new person.
    Allow the user to rmeove input various enter infromation for a new person.
"""

# person class will collect and store properties inside a phone.
class person:
    def __init__(self, name, age, sex, nat):
        self.name = name
        self.age = age
        self.sex = sex
        self.nat = nat
    def collect_data(self):
        input('Enter personal infromation: ')