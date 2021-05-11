import uuid
from copy import deepcopy


class Person:
    def __init__(self):
        self.__name = "Vitalii"
        self.__last_name = 'Kolobok'
        self.__uuid = uuid.uuid4().hex

    def __repr__(self):
        return f'{self.__dict__}'

    def creating_new_object(self, **kwargs):
        self_copy = deepcopy(self)
        for value in kwargs:
            setattr(self_copy, value, kwargs[value])
        return self_copy


person = Person()

''' Сopying primary data and adding data '''
person_objects = person.creating_new_object(firm_car='Renault', model_car='Koleos',
                                            color_car="Grey", government_number='AX2578EM')
print(person_objects)
print(person)
