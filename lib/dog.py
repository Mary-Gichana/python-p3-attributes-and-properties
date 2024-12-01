#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    APPROVED_BREEDS_LIST = ["Pug", "Dalmatian", "Labrador", "Golden Retriever", "Bulldog"]

    def __init__(self, name=None, breed="Mutt"):
        # Validate the breed first
        if breed not in self.APPROVED_BREEDS_LIST and breed != "Mutt":
            print("Breed must be in list of approved breeds.")
            return  # Stop further execution if breed validation fails

        self.breed = breed

        # Now validate the name
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            return  # Stop further execution if name validation fails

        self.name = name
pass