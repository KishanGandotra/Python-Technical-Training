class Customers:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__address = address

    # Properties for customer attributes
    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    @property
    def address(self):
        return self.__address

    # Setter methods with data validation
    @first_name.setter
    def first_name(self, new_first_name):
        if isinstance(new_first_name, str):
            self.__first_name = new_first_name
        else:
            raise ValueError("First name must be a string.")

    @last_name.setter
    def last_name(self, new_last_name):
        if isinstance(new_last_name, str):
            self.__last_name = new_last_name
        else:
            raise ValueError("Last name must be a string.")

    @email.setter
    def email(self, new_email):
        if '@' in new_email:
            self.__email = new_email
        else:
            raise ValueError("Invalid email format.")

    @phone.setter
    def phone(self, new_phone):
        if isinstance(new_phone, str):
            self.__phone = new_phone
        else:
            raise ValueError("Phone number must be a string.")

    @address.setter
    def address(self, new_address):
        if isinstance(new_address, str):
            self.__address = new_address
        else:
            raise ValueError("Address must be a string.")
