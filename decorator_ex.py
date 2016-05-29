def add_salute(salute, qualification):
    def salutation(func):
        def func_wrapper(*args, **kwargs):
            return "{} {}, {} {}".format(salute, args[2], args[1], qualification)
        return func_wrapper
    return salutation

class Person(object):
    @add_salute("Dr.", "MD.")
    def present_official_name(self, name, family):
        return name + " " + family

my_person = Person()
print my_person.present_official_name('John', 'Doe')
print my_person.present_official_name('Gregory', 'House')