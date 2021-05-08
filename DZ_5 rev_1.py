class BadClass:
    def __init__(self, val=1):
        self.__val = val
        self.get_val()

    def get_val(self):
        return self.__val

    def __eq__(self, other):
        return isinstance(other, BadClass) and self.get_val() == other.val

    def __hash__(self):
        return hash(self.__val)

    def __repr__(self):
        return str(self.__dict__)


print("<1>", BadClass())
new = BadClass()
print("<2>", new)

new.val = 2
print("<3>", new)

new.val = 10
print("<4>", new)

var_1 = {new}
assert (new in var_1)
print("<5>", var_1)
print("<6>", BadClass())

var_2 = {new}
print("<7>", var_1 == var_2)

var_2.add(1)
print("<8>", var_1 == var_2)

print("<9>", BadClass())
new_2 = BadClass()
print("<10>", new_2)

new_2.val = 10
var_3 = {new_2}
print("<11>", var_1 == var_3)
print("<12>", var_1, var_3)
