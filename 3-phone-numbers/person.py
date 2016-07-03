class Person():
    _name = None
    _phone_number = None

    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number

    def is_phone_number_matching(self, input_phone_number):
        if self._phone_number == input_phone_number:
            return True
        return False

    def get_name(self):
            return self._name

    @staticmethod
    def normalize_phone_number(phone_number):
        for char in phone_number:
            if char in " -?.!;:":
                phone_number = phone_number.replace(char, '')
        return phone_number
