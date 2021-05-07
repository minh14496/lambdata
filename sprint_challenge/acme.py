import random


class Product:
    def __init__(
        self, name, price=10, weight=20, flammability=0.5,
        identifier=random.randint(1000000, 9999999)
            ):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
        
    def stealability(self):
        """
        stealability Determine the stealability of a product by
        calculating the price divided by the weight

        Returns:
            [string]: A message whether a product stealable or not
        """
        steal_ratio = self.price/self.weight
        if steal_ratio < 0.5:
            return f"Not so stealable..."
        elif steal_ratio >= 1.0:
            return f"Very stealable!"
        else:
            return f'Kinda stealable.'

    def explode(self):
        """
        explode Determine the explodibility of a product by
        calculating the flammability times the weight

        Returns:
            [string]: A message whether a product can explode
        """
        baboom = self.flammability * self.weight
        if baboom < 10:
            return f'...fizzle.'
        elif baboom >= 50:
            return f'...BABOOM!!'
        else:
            return f'...boom!'


class BoxingGlove(Product):
    def __init__(
        self, name, price=10, weight=10, flammability=0.5,
        identifier=random.randint(1000000, 9999999)
            ):
        super().__init__(
            name, price=price, weight=weight,
            flammability=flammability, identifier=identifier
                )
                
    def explode(self):
        """Explode function only return one outcome in this class"""
        return f"...it's a glove."

    def punch(self):
        """
        punch Determine if a glove is good to punch

        Returns:
            [string]: A message whether a glove is good for boxing
        """
        if self.weight < 5:
            return f"That tickles."
        elif self.weight >= 15:
            return f"OUCH!"
        else:
            return f"Hey that hurt!"
