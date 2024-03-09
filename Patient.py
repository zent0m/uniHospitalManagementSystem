class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        #ToDo1
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode

        self.__symptoms = 'None'
        self.__appointments = []
        self.__months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        
        self.__doctor = 'None'
       

    
    def full_name(self) :
        """full name is first_name and surname"""
        #ToDo2
        return self.__first_name + " " + self.__surname

    def get_first_name(self):
        return self.__first_name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def get_mobile(self):
        return self.__mobile

    def get_postcode(self):
        return self.__postcode

    def get_doctor(self) :
        #ToDo3
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def set_symptoms(self):
        self.__symptoms = input("\nPlease enter the symptoms of the patient (in one line): ")

    def get_symptoms(self):
        """prints all the symptoms"""
        #ToDo4
        return self.__symptoms

    def set_appointment(self, day, month, doctor):
        self.link(doctor)
        self.__appointments.append(f"{day} of {self.__months[month]} with {doctor.full_name()}")
        
    def get_appointments(self):
        return self.__appointments

    def __str__(self):
        if self.__doctor != "None":
            return f'{self.full_name():^30}|{self.__doctor.full_name():^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
        else:
            return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
