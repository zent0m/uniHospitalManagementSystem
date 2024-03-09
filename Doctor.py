class Doctor:
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """

        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []
        self.__months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.__monthlyApp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    
    def full_name(self) :
        return self.__first_name + " " + self.__surname

    def get_first_name(self) :
        return self.__first_name

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def get_surname(self) :
        return self.__surname

    def set_surname(self, new_surname):
        self.__surname = new_surname

    def get_speciality(self) :
        return self.__speciality

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality

    def add_patient(self, patient):
        self.__patients.append(patient)

    def get_patient(self, index):
        return self.__patients[index]

    def remove_patient(self, index):
        del self.__patients[index]

    def set_appointment(self, day, month, patient):
        self.add_patient(patient)
        self.__appointments.append(f"{day} of {self.__months[month]} with {patient.full_name()}")
        self.appointmentsMonthAdd(month)

    def appointmentsMonthAdd(self, month):
        self.__monthlyApp[month - 1] += 1

    def getAppointmentsMonth(self, month):
        return self.__monthlyApp[month]
        
    def get_appointments(self):
        return self.__appointments

    def get_patients(self):
        return self.__patients

    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'
