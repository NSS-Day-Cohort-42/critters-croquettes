class Walking(object):
    """
    Properties and methods for walking animals
    """
    def __init__(self, walking_speed):
        self.walking = True
        self.walking_speed = walking_speed

    def walk(self):
        print(f"This animal walks at {self.walking_speed} meters per second")
