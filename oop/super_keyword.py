# The super key is used to access the variable of parent class by child classes, one way of doing it is commented
# at line number 13, but for clean code super keyword was introduced.
class User:
    def __init__(self, email):
        self.email = email

    def attack_parent(self):
        print(f'Check me, I am attacked by {self.email}')


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        User.attack_parent(self)
        print(f'Attack with power of {self.power}')


class Elf(User):
    def __init__(self, name, arrow, email):
        super().__init__(email)
        self.name = name
        self.arrow = arrow

    def attack(self):
        print(f'Attack with left arrows count of {self.arrow}')


wizard = Wizard('Rup', 100, 'rupaligwen@gmail.com')
elf = Elf('Ali', 50, 'rupaligwen@gmail.com')
print(wizard.attack())
print(elf.attack())
