import os
from appointment import Appointment  

def create_weekly_calendar():
    """Create a weekly calendar with available appointments."""
    appointments = []
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for day in days_of_week:
        for hour in range(9, 17):  # Appointments from 9 AM to 4 PM
            appointments.append(Appointment(day_of_week=day, start_time_hour=hour))
    return appointments

def load_scheduled_appointments(appointments):
    """Load appointments from a file and schedule them in the calendar."""
    filename = input("Enter the filename to load appointments: ")

    if not os.path.exists(filename):
        print("File not found.")
        return 0

    with open(filename, 'r') as file:
        count = 0
        for line in file:
            client_name, client_phone, appt_type, day, hour = line.strip().split(',')
            appt_type, hour = int(appt_type), int(hour)

            appointment = find_appointment(appointments, day, hour)
            if appointment:
                appointment.schedule(client_name, client_phone, appt_type)
                count += 1
    print(f"{count} appointments loaded from {filename}.")
    return count

def print_menu():
    """Display the menu and return the user's selection."""
    print("\nAppointment Management System")
    print("1) Schedule an appointment")
    print("2) Find appointments by name")
    print("3) Show calendar for a specific day")
    print("4) Cancel an appointment")
    print("5) Reschedule an appointment")
    print("6) Calculate daily fees")
    print("7) Calculate weekly fees")
    print("9) Exit")

    choice = input("Choose an option: ")
    return int(choice) if choice.isdigit() and choice in '12345679' else None

def find_appointment(appointments, day, hour):
    """Find an appointment by day and hour."""
    for appt in appointments:
        if appt.get_day_of_week() == day and appt.get_start_time_hour() == hour:
            return appt
    return None

def show_appointments_by_name(appointments, name):
    """Display all appointments for a given client name."""
    print(f"\nAppointments for {name}:")
    for appt in appointments:
        if name.lower() in appt.get_client_name().lower():
            print(appt)

def show_appointments_by_day(appointments, day):
    """Display all appointments for a given day."""
    print(f"\nAppointments on {day}:")
    for appt in appointments:
        if appt.get_day_of_week() == day:
            print(appt)

def reschedule_appointment(appointments):
    """Change an existing appointment to a new time."""
    day = input("Enter the current appointment day: ")
    hour = int(input("Enter the current appointment start hour: "))

    current_appt = find_appointment(appointments, day, hour)
    if current_appt and current_appt.get_appt_type() != 0:
        print(f"Current appointment: {current_appt}")

        new_day = input("Enter the new day: ")
        new_hour = int(input("Enter the new hour: "))
        new_appt = find_appointment(appointments, new_day, new_hour)

        if new_appt and new_appt.get_appt_type() == 0:
            new_appt.schedule(
                current_appt.get_client_name(),
                current_appt.get_client_phone(),
                current_appt.get_appt_type()
            )
            current_appt.cancel()
            print(f"Appointment rescheduled to {new_day} at {new_hour}:00.")
        else:
            print("The new time slot is unavailable.")
    else:
        print("No appointment found at the specified time.")

def calculate_daily_fees(appointments):
    """Calculate the total fees for a specific day."""
    day = input("Enter the day to calculate fees for: ")
    total = sum(get_fee(appt.get_appt_type()) for appt in appointments if appt.get_day_of_week() == day)
    print(f"Total fees for {day}: ${total}")

def calculate_weekly_fees(appointments):
    """Calculate the total fees for the entire week."""
    total = sum(get_fee(appt.get_appt_type()) for appt in appointments)
    print(f"Total weekly fees: ${total}")

def get_fee(appt_type):
    """Return the fee for a given appointment type."""
    fees = {1: 40, 2: 60, 3: 40, 4: 80}
    return fees.get(appt_type, 0)

def save_appointments(appointments):
    """Save scheduled appointments to a file."""
    filename = input("Enter the filename to save appointments: ")
    
    if os.path.exists(filename):
        if input(f"{filename} exists. Overwrite? (y/n): ").lower() != 'y':
            print("Save canceled.")
            return 0

    with open(filename, 'w') as file:
        count = 0
        for appt in appointments:
            if appt.get_appt_type() != 0:
                file.write(appt.format_record() + '\n')
                count += 1
    print(f"{count} appointments saved to {filename}.")
    return count

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

if __name__ == "__main__":
    main()
