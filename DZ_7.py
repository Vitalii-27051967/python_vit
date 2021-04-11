import uuid
from copy import deepcopy


class Person:
    def __init__(self, **kwargs):
        for value in kwargs:
            setattr(self, value, kwargs[value])

    def __repr__(self):
        print("---------------------------------------------")
        return f'{self.__dict__}'

    def creating_new_object(self, **kwargs):
        self_copy = deepcopy(self)
        print('сopy', self_copy)       # Для наглядности проверки работы
        for value in kwargs:
            setattr(self_copy, value, kwargs[value])
        return self_copy


''' Input of primary data '''
person = Person()
person.__init__(name='Vitalii', last_name='Kolobok', uuid=uuid.uuid4().hex)

''' Сopying primary data and adding data '''
person_objects = person.creating_new_object(firm_car='Renault', model_car='Koleos',
                                            color_car="Grey", government_number='AX2578EM')
print(person_objects)
print(person)
