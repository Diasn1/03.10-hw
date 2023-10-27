class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def turn_on(self):
        print(f"{self.brand} {self.model} is turned on.")

    def turn_off(self):
        print(f"{self.brand} {self.model} is turned off.")


class CoffeeMachine(Device):
    def __init__(self, brand, model, water_reservoir_capacity):
        super().__init__(brand, model)
        self.water_reservoir_capacity = water_reservoir_capacity

    def brew_coffee(self):
        print(f"Brewing coffee with {self.brand} {self.model}.")

    def refill_water(self):
        print(f"Refilling water in {self.brand} {self.model}.")


class Blender(Device):
    def __init__(self, brand, model, max_speed):
        super().__init__(brand, model)
        self.max_speed = max_speed

    def blend(self):
        print(f"Blending with {self.brand} {self.model}.")

    def set_speed(self, speed):
        print(f"Setting speed to {speed} on {self.brand} {self.model}.")


class MeatGrinder(Device):
    def __init__(self, brand, model, power):
        super().__init__(brand, model)
        self.power = power

    def grind_meat(self):
        print(f"Grinding meat with {self.brand} {self.model}.")

    def clean(self):
        print(f"Cleaning {self.brand} {self.model}.")


coffee_machine = CoffeeMachine("CoffeeBrand", "ModelX", 1000)
coffee_machine.turn_on()
coffee_machine.refill_water()
coffee_machine.brew_coffee()
coffee_machine.turn_off()

blender = Blender("BlenderCo", "BlenderZ", 1500)
blender.turn_on()
blender.set_speed(3)
blender.blend()
blender.turn_off()

meat_grinder = MeatGrinder("GrinderCorp", "MeatMaster", 800)
meat_grinder.turn_on()
meat_grinder.grind_meat()
meat_grinder.clean()
meat_grinder.turn_off()
