from Doctor import Doctor
from Patient import Patient

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address
        self.__months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """

        if a_list:
            for index, item in enumerate(a_list):
                print(f'{index+1:3}|{item}')
        else:
            print("\nThere are no entries in this list.\n")


    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("\n-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        #ToDo1
        
        if username != self.__username or password != self.__password:
            print("\nThe login details are incorrect!")
        else:
            return self.__username



    def find_index(self,index,list):     
            # check that the id exists          
        if index in range(0,len(list)):   
            return True

        # if the id is not in the list
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        print("Enter the doctor's details:\n")

        fname = input("Enter the doctor's first name: ")
        sname = input("Enter the doctor's surname: ")
        spec = input("Enter the doctor's speciality: ")

        tempDoc = Doctor(fname, sname, spec)

        return tempDoc

    def doctor_management(self, doctors, patients):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """
        while True:
            print("\n-----Doctor Management-----")

            # menu
            print('\nChoose the operation:\n')
            print(' 1 - REGISTER new doctor')
            print(' 2 - VIEW list of doctors')
            print(' 3 - MANAGE doctor\'s patients')
            print(' 4 - VIEW doctor\'s appointments')
            print(' 5 - UPDATE doctor details')
            print(' 6 - DELETE doctor from system')
            print('\n 7 - EXIT Doctor Management')

            #ToDo3
            op = input("\nOption: ")

            # register
            if op == '1':
                print("-----Register-----")

                # get the doctor details
                #ToDo4
                tempDoc = self.get_doctor_details()

                # check if the name is already registered
                name_exists = False
                for doctor in doctors:
                    if tempDoc.get_first_name() == doctor.get_first_name() and tempDoc.get_surname() == doctor.get_surname():
                        print('\nName already exists. Cannot register a doctor with the same name.')
                        #ToDo5
                        break # save time and end the loop

                #ToDo6
                # add the doctor ...
                doctors.append(tempDoc)# ... to the list of doctors
                print('\nDoctor registered.')

            # View
            elif op == '2':
                print("-----List of Doctors-----")
                #ToDo7
                self.view_doctors(doctors)

            # View Patients
            elif op == '3':
                print("\n-----Doctor's Patient Management-----")

                # menu
                print('\nChoose the operation:\n')
                print(' 1 - VIEW doctor\'s patients\' details')
                print(' 2 - RELOCATE patient')

                #ToDo3
                op = input("\nOption: ")

                if op == '1':
                    while True:
                        print("-----View Doctor's Patients-----")
                        self.view_doctors(doctors)
                        try:
                            index = int(input('\nEnter the ID of the doctor: ')) - 1
                            doctor_index=self.find_index(index,doctors)
                            if doctor_index != False:
                                break         
                            else:
                                print("\nDoctor not found. Try again.")
                                # doctor_index is the ID minus one (-1)
                        

                        except ValueError: # the entered id could not be changed into an int
                            print('\nThe ID entered is invalid.')

                    self.view_patient(doctors[index].get_patients())

                    tempPat = doctors[index].get_patients()

                    for i in range(len(tempPat)):
                        print(f'\nPatient {i+1} Symptoms: {tempPat[i].get_symptoms()}')

                elif op == '2':
                    print("-----Relocate Patients-----")
                    self.view_doctors(doctors)

                    while True:
                        try:
                            index = int(input('\nEnter the ID of the doctor with the patient:')) - 1
                            doctor_index=self.find_index(index,doctors)
                            if doctor_index != False:
                                break         
                            else:
                                print("\nDoctor not found. Try again.")
                                # doctor_index is the ID minus one (-1)

                        except ValueError: # the entered id could not be changed into an int
                            print('\nThe ID entered is invalid.')

                    self.view_patient(doctors[index].get_patients())

                    while True:
                        try:
                            index1 = int(input('\nEnter the ID of patient to be relocated:')) - 1
                            patient_index=self.find_index(index1,doctors[index].get_patients())
                            if patient_index != False:
                                break         
                            else:
                                print("\nPatient not found. Try again.")

                        except ValueError: # the entered id could not be changed into an int
                            print('\nThe ID entered is invalid.')

                    self.view_doctors(doctors)

                    while True:
                        try:
                            index2 = int(input('\nEnter the ID of the doctor to whom the patient will be relocated to:')) - 1
                            doctor_index1=self.find_index(index2,doctors)
                            if doctor_index1 != False:
                                break         
                            else:
                                print("\nDoctor not found. Try again.")
                                # doctor_index is the ID minus one (-1)

                        except ValueError: # the entered id could not be changed into an int
                            print('\nThe ID entered is invalid.')

                    doctors[index2].add_patient(doctors[index].get_patient(index1))

                    for patient in patients:
                        if doctors[index].get_patient(index1).full_name() == patient.full_name():
                            patient.link(doctors[index2])
                            break # save time and end the loop

                    doctors[index].remove_patient(index1)

                    print('\nThe patient has been relocated.')

                else:
                    print('\nInvalid operation chosen.')

            elif op == '4':
                while True:
                    print("-----View Doctor Appointments-----")
                    self.view_doctors(doctors)
                    try:
                        index = int(input('\nEnter the ID of the doctor: ')) - 1
                        doctor_index=self.find_index(index,doctors)
                        if doctor_index != False:
                            break         
                        else:
                            print("\nDoctor not found. Try again.")
                            # doctor_index is the ID minus one (-1)
                        

                    except ValueError: # the entered id could not be changed into an int
                        print('\nThe ID entered is invalid.')

                print('\nAppointments of the doctor: ')
                self.view(doctors[index].get_appointments())
                

            # Update
            elif op == '5':
                while True:
                    print("-----Update Doctor`s Details-----")
                    self.view_doctors(doctors)
                    try:
                        index = int(input('\nEnter the ID of the doctor: ')) - 1
                        doctor_index=self.find_index(index,doctors)
                        if doctor_index != False:
                            break         
                        else:
                            print("\nDoctor not found. Try again.")
                            # doctor_index is the ID minus one (-1)
                        

                    except ValueError: # the entered id could not be changed into an int
                        print('\nThe ID entered is invalid.')

                # menu
                print('\nChoose the field to be updated:')
                print(' 1 - First name')
                print(' 2 - Surname')
                print(' 3 - Speciality')
                op = int(input('\nInput: ')) # make the user input lowercase

                #ToDo8
                try:
                    if op == 1:
                        newFname = input("Enter the new first name: ")
                        doctors[index].set_first_name(newFname)
                        print("\nThe doctor's first name was updated!\n")
                    elif op == 2:
                        newSname = input("Enter the new surname: ")
                        doctors[index].set_surname(newSname)
                        print("\nThe doctor's surname was updated!\n")
                    elif op == 3:
                        newSpec = input("Enter the doctor's updated speciality: ")
                        doctors[index].set_speciality(newSpec)
                        print("\nThe doctor's speciality was updated!\n")
                    else:
                        print("\nInput was out of range.")
                except:
                    print("\nInvalid input.")


            # Delete
            elif op == '6':
                while True:
                    print("-----Delete Doctor-----")
                    self.view_doctors(doctors)

                    #ToDo9
                    try:
                        index = int(input('\nEnter the ID of the doctor to be deleted: ')) - 1
                        doctor_index=self.find_index(index,doctors)
                        if doctor_index != False:
                            break         
                        else:
                            print("\nDoctor not found. Try again.")
                            # doctor_index is the ID minus one (-1)

                    except ValueError: # the entered id could not be changed into an int
                        print('\nThe ID entered is invalid.')

                del doctors[index]
                print("\nThe doctor was successfully removed!")

            elif op == '7':
                break

            else:
                print('\nInvalid operation chosen.')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode \n')
        #ToDo10
        self.view(patients)

    def patient_appointments(self, patients, doctors):
        while True:
            print("\n-----View/Add Patient Appointments-----")

            # menu
            print('\nChoose the operation:\n')
            print(' 1 - ADD patient appointments')
            print(' 2 - VIEW patient appointments')
            print('\n 3 - RETURN')

            #ToDo3
            op = input("\nOption: ")

            # register
            if op == '1':
                print("\n-----Add patient appointments-----")
                self.view_patient(patients)

                patient_index = input('Please enter the patient ID: ')

                try:
                    # patient_index is the patient ID mines one (-1)
                    patient_index = int(patient_index) -1

                   # check if the id is not in the list of patients
                    if self.find_index(patient_index,patients) != False:
                        try:
                            day = int(input("\nPlease input the day of the appointment:"))
                            while day > 31 or day < 1:
                                day = int(input("\nInvalid day entered. Please try again: :"))

                            month = int(input("\nPlease input the month of the appointment (in numbers):"))
                            while month > 12 or month < 1:
                                month = int(input("\nInvalid month entered. Try again:"))
                            print("\n")
                            self.view_doctors(doctors)
                            doctor_index = input('\nPlease enter the doctor ID to allocate to the patient: ')

                            try:
                                # doctor_index is the patient ID mines one (-1)
                                doctor_index = int(doctor_index) -1

                                # check if the id is in the list of doctors
                                if self.find_index(doctor_index,doctors)!=False:

                                    approval = input('\n\nDo you want to approve this appointment? (y/n)').lower()

                                    if approval == 'y':
                                        patients[patient_index].set_appointment(day, month - 1, doctors[doctor_index])
                                        doctors[doctor_index].set_appointment(day, month - 1, patients[patient_index])

                                        print("\nThe appointment was approved and added to both patient and doctor profiles.")
                                    else:
                                        break

                                # if the id is not in the list of doctors
                                else:
                                    print('The id entered was not found.')

                            except ValueError: # the entered id could not be changed into an in
                                print('The id entered is incorrect')
                        except:
                            print("\nInvalid ID entered.")
                    else:
                        print('The id entered was not found.')
                        return # stop the procedures

                except ValueError: # the entered id could not be changed into an int
                    print('The id entered is incorrect')
                    return # stop the procedures
            
            elif op == '2':
                print("\n-----View patient appointments-----")
                self.view_patient(patients)

                patient_index = input('Please enter the patient ID: ')

                try:
                    # patient_index is the patient ID mines one (-1)
                    patient_index = int(patient_index) -1

                   # check if the id is not in the list of patients
                    if self.find_index(patient_index,patients) != False:
                        print('\nAppointments of the patient: ')
                        self.view(patients[patient_index].get_appointments())

                    else:
                        print('The id entered was not found.')
                        return # stop the procedures

                except ValueError: # the entered id could not be changed into an int
                    print('The id entered is incorrect')
                    return # stop the procedures

            elif op == '3':
                break
            
            else:
                print("Invalid operation chosen")

    def patient_symptoms(self, patients):
        """
        A method that deals with viewing and setting patient symptoms
        Args:
            patients (list<Patient>): the list of all the patients
        """
        while True:
            print("\n-----View/Set Patient Symptoms-----")

            # menu
            print('\nChoose the operation:\n')
            print(' 1 - SET patient symptoms')
            print(' 2 - VIEW patient symptoms')
            print('\n 3 - RETURN')

            #ToDo3
            op = input("\nOption: ")

            # register
            if op == '1':
                print("\n-----Set patient symptoms-----")
                self.view_patient(patients)

                patient_index = input('Please enter the patient ID: ')

                try:
                    # patient_index is the patient ID mines one (-1)
                    patient_index = int(patient_index) -1

                   # check if the id is not in the list of patients
                    if self.find_index(patient_index,patients) != False:
                        patients[patient_index].set_symptoms()

                    else:
                        print('The id entered was not found.')
                        return # stop the procedures

                except ValueError: # the entered id could not be changed into an int
                    print('The id entered is incorrect')
                    return # stop the procedures
            
            elif op == '2':
                print("\n-----View patient symptoms-----")
                self.view_patient(patients)

                patient_index = input('Please enter the patient ID: ')

                try:
                    # patient_index is the patient ID mines one (-1)
                    patient_index = int(patient_index) -1

                   # check if the id is not in the list of patients
                    if self.find_index(patient_index,patients) != False:
                        print('\nSymptoms of the patient: ' + patients[patient_index].get_symptoms())

                    else:
                        print('The id entered was not found.')
                        return # stop the procedures

                except ValueError: # the entered id could not be changed into an int
                    print('The id entered is incorrect')
                    return # stop the procedures

            elif op == '3':
                break
            
            else:
                print("Invalid operation chosen")

    def view_family(self, patients):
        lname = input("\nPlease enter the family name: ")
        count = 0

        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode \n')

        for index, item in enumerate(patients):
            if item.get_surname() == lname:
                print(f'{index+1:3}|{item}')
                count += 1
        
        if count == 0:
            print("There are no patients with that family name.")

    def view_doctors(self, doctors):
        print('ID |          Full name           |  Speciality\n')
        self.view(doctors)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        self.view_patient(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if self.find_index(patient_index,patients) == False:
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        print(patients[patient_index].get_symptoms()) # print the patient symptoms

        print('--------------------------------------------------')
        self.view_doctors(doctors)
        doctor_index = input('\nPlease enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                patients[patient_index].link(doctors[doctor_index])
                doctors[doctor_index].add_patient(patients[patient_index])
                
                print('\nThe patient is now assigned to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients, doctors):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        #ToDo12
        while True:
            print("-----Discharge Patient-----")
            self.view_patient(patients)

            patient_index = input('Please enter the patient ID to discharge. Enter \'n\' to finish:')

            if patient_index.lower() == 'n':
                break
            elif int(patient_index) - 1 not in range(len(patients)):
                print('The id entered was not found.')
            else:
                for doctor in doctors:
                    for i in range(len(doctor.get_patients())):
                        if doctor.get_patient(i).full_name() == patients[int(patient_index) - 1].full_name():
                            doctor.remove_patient(i)

                discharge_patients.append(patients.pop(int(patient_index) - 1))
                print("\nThe patient was succesfully discharged.")

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo13
        self.view(discharged_patients)

    def patient_file(self, patients):
        while True:
            print("\n-----Patient File Management-----")

            # menu
            print('\nChoose the operation:\n')
            print(' 1 - SAVE patients to file')
            print(' 2 - LOAD patients from file')
            print('\n 3 - RETURN')

            op = input("\nOption: ")

            if op == '1':
                patientFile = open("patient_list.txt", "w")
    
                try:
                    for patient in patients:
                        patientFile.write(f"{patient.get_first_name()}, {patient.get_surname()}, {patient.get_age()}, {patient.get_mobile()}, {patient.get_postcode()}")
                        patientFile.write("\n")
                except:
                    print("\n\nThe write procedure was unsuccessful")
                    break
                else:
                    print("\n\nThe write procedure was successful\n")
                    patientFile.close()
                    return patients
            
            elif op == '2':
                try:
                    patientFile = open("patient_list.txt", "r")
                    line = patientFile.readline()
                    tempPatients = []

                    while line != '':
                        line = line.replace("\n", "")
                        lineArray = line.split(", ")
                        patient = Patient(lineArray[0], lineArray[1], lineArray[2], lineArray[3], lineArray[4])
                        tempPatients.append(patient)
                        line = patientFile.readline()

                    patientFile.close()

                    self.view_patient(tempPatients)
                    opt = input("\nThis is the list of patients loaded in from the file.\nARE YOU SURE YOU WANT TO OVERWRITE THE CURRENT PATIENT LIST WITH THE NEW LIST? (y/n): ")

                    if opt.lower() == 'y':
                        print("\nThe overwrite was successful. Patient list updated.")
                        return tempPatients
                    elif opt.lower() == 'n':
                        print("\nThe new list was discarded. Nothing was updated.")
                        return patients
        
                except FileNotFoundError as err:
                    print("The file 'patient_list.txt' was not found.")

            elif op == '3':
                break
            
            else:
                print("Invalid operation chosen")

    def management_report(self, patients, doctors):
        print("\n\n-------------------------MANAGEMENT REPORT-------------------------\n\n")
        print(f"The total number of doctors registered in the hospital: {(len(doctors))}\n")
        
        print("Number of patients registered per doctor:")
        for doctor in doctors:
            print(f"Dr. {doctor.full_name()} has {len(doctor.get_patients())} patient(s).")

        print("\n")

        for doctor in doctors:
            for i in range(11):
                if doctor.getAppointmentsMonth(i) > 0:
                    print(f"Dr. {doctor.full_name()} has {doctor.getAppointmentsMonth(i)} appointment(s) in {self.__months[i + 1]}")
        
        print("\n")

        tempArr = []
        for patient in patients:
            count = 1
            for patientx in patients:
                if patient != patientx and patient.get_symptoms() == patientx.get_symptoms():
                    count += 1
            tempArr.append(f'The number of patients with symptoms "{patient.get_symptoms()}": {count}.')

        tempArr = list(dict.fromkeys(tempArr))
        
        for i in tempArr:
            print(i)
                    

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('\nChoose the field to be updated:')
        print(' 1 - Username')
        print(' 2 - Password')
        print(' 3 - Address')
        op = int(input('\nInput: '))

        if op == 1:
            #ToDo14
            username = input("\nPlease enter the new username: ")
            self.__username = username
            print("\nThe username was changed successfully!")

        elif op == 2:
            while True:
                password = input('\nEnter the new password: ')
                # validate the password
                if password == input('Enter the new password again: '):
                    self.__password = password
                    print("\nThe password was changed successfully!")
                    break
                else:
                    print("\nThe two passwords doesn't match! Try again:")

        elif op == 3:
            #ToDo15
            address = input("\nPlease enter the new address: ")
            self.__address = address
            print("\nThe address was changed successfully!")

        else:
            #ToDo16
            print("Invalid option.")

