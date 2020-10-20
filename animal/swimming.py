class Swimming(object):
    """
    Properties and methods for swimming animals
    """
    def __init__(self, swimming_speed):
        self.swimming = True
        self.swimming_speed = swimming_speed

    def swim(self):
        print(f"This animal swims at {self.swimming_speed} meters per second")
