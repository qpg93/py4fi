""" object-oriented programming """


class HumanBeing():
    """ class definition """

    def __init__(self, first_name, eye_color):
        self.first_name = first_name
        self.last_name = None
        self.eye_color = eye_color
        self.position = 0

    def walk_steps(self, steps):
        """ method: an operation that human being can implement """
        self.position += steps

    def get_last_name(self, last_name):
        """ get last name """
        self.last_name = last_name


Sandra = HumanBeing('Sandra', 'blue')
print('first name:\n', Sandra.first_name)
print('position:\n', Sandra.position)
Sandra.walk_steps(3)
print('position after walking 3 steps:\n', Sandra.position)
