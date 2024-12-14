def main():
    """Main function to run the appointment management system."""
    appointments = create_weekly_calendar()
    load = input("Load existing appointments? (y/n): ")
    if load.lower() == 'y':
        load_scheduled_appointments(appointments)
    elif load.lower() != 'y' or load.lower() != 'n':
        Print('Incorrect Input')
    while True:
        print_menu()
        choice = input("Enter Your Selection: ")
        if choice == 1:
            client_name = input("Enter client name: ")
            client_phone = input("Enter client phone: ")
            appt_type = int(input("Enter appointment type (1: Mens Cut, 2: Ladies Cut, 3: Mens Colouring, 4: Ladies Colouring): "))
            day = input("Enter day of the week: ")
            hour = int(input("Enter start hour(24 hours clock): "))
            
            appt = find_appointment(appointments, day, hour)
            if appt and appt.get_appt_type() == 0:
                appt.schedule(client_name, client_phone, appt_type)
                print("Appointment scheduled.")
            else:
                print("Time slot unavailable.")

        elif choice == 2:
            name = input("Enter client name to search: ")
            show_appointments_by_name(appointments, name)

        elif choice == 3:
            day = input("Enter day to view: ")
            show_appointments_by_day(appointments, day)

        elif choice == 4:
            day = input("Enter appointment day to cancel: ")
            hour = int(input("Enter appointment hour to cancel: "))
            appt = find_appointment(appointments, day, hour)
            if appt and appt.get_appt_type() != 0:
                appt.cancel()
                print("Appointment canceled.")
            else:
                print("No appointment found.")

        elif choice == 5:
            reschedule_appointment(appointments)

        elif choice == 6:
            calculate_daily_fees(appointments)

        elif choice == 7:
            calculate_weekly_fees(appointments)

        elif choice == 9:
            if input("Save appointments before exiting? (y/n): ").lower() == 'y':
                save_appointments(appointments)
            print("Goodbye!")
            break
        else:
            print("Incorrect Input")
