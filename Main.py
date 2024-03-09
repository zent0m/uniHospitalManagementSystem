# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Will','Smith','Pediatrics'), Doctor('Dave','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Henry','Smith', 15, '07123456789','C1 ABC')]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            print("\nLogged in successfully.")
            break
        else:
            continue

    while running:
        # print the menu
        print('\n----------Hospital Management System----------')
        print('\nChoose the operation:\n')
        print(' 1- Manage doctors\n')
        print(' 2- View patients')
        print(' 3- View/Add patient appointments')
        print(' 4- View/Set patient symptoms')
        print(' 5- View patients in a family')
        print(' 6- Discharge patients')
        print(' 7- View discharged patients')
        print(' 8- Assign doctor to a patient')
        print('\n 9- Patient File Management')
        print('\n 10- Management Report Generator')
        print('\n 11- Update admin details')
        print('\n 12- Quit\n')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Manage doctors
         #ToDo1
          admin.doctor_management(doctors, patients)

        elif op == '2':
            # 2 - View patients
            admin.view_patient(patients)

        elif op == '3':
            # 3 - View/Add patient appointments
            admin.patient_appointments(patients, doctors)

        elif op == '4':
            # 4 - View/Set patient symptoms
            admin.patient_symptoms(patients)

        elif op == '5':
            # 5 - View patients in a family
            admin.view_family(patients)

        elif op == '6':
            # 6- Discharge patients
            #ToDo2

            while True:
                op = input('\nDo you want to discharge a patient (Y/N):').lower()

                if op == 'yes' or op == 'y':
                    #ToDo3
                    admin.discharge(patients, discharged_patients, doctors)

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('\nPlease choose a valid option:')
        
        elif op == '7':
            # 7 - View discharged patients
            #ToDo4
            admin.view_discharge(discharged_patients)

        elif op == '8':
            # 8- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '9':
            # 9- Patient File management
            patients = admin.patient_file(patients)

        elif op == '10':
            # 10- Management Report
            admin.management_report(patients, doctors)


        elif op == '11':
            # 11- Update admin detais
            admin.update_details()

        elif op == '12':
            # 12 - Quit
            #ToDo5
            break

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
