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
            [string]: a message: if the ratio is less than 0.5
        return "Not so stealable...", if it is greater or equal
        to 0.5 but less than 1.0 return "Kinda stealable.",
        and otherwise return "Very stealable!"
        """
        steal_ratio = self.price/self.weight
        if steal_ratio < 0.5:
            return "Not so stealable..."
        elif steal_ratio >= 1.0:
            return "Very stealable!"
        else:
            return 'Kinda stealable.'

    def explode(self):
        """
        explode Determine the explodibility of a product by
        calculating the flammability times the weight

        Returns:
            [string]: a message: if the product is less than 10 return
        "...fizzle.", if it is greater or equal to 10 but less
        than 50 return "...boom!", and otherwise
        return "...BABOOM!!"
        """
        baboom = self.flammability * self.weight
        if baboom < 10:
            return '...fizzle.'
        elif baboom >= 50:
            return '...BABOOM!!'
        else:
            return '...boom!'


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
        return "...it's a glove."

    def punch(self):
        """
        punch Determine if a glove is good to punch

        Returns:
            [string]: "That tickles." if the weight is below 5,
        "Hey that hurt!" if the weight is greater or equal to 5
        but less than 15, and "OUCH!" otherwise
        """
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 15:
            return "OUCH!"
        else:
            return "Hey that hurt!"
