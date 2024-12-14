import os


class Appointment:
    def __init__(self, day_of_week, start_time_hour):
        """
        Initialize an Appointment object with default properties.
        day_of_week: The day of the week for the appointment.
        start_time_hour: The starting hour of the appointment.
        """
        self.client_name = ""  # Placeholder for client's name.
        self.client_phone = ""  # Placeholder for client's phone number.
        self.appt_type = 0  # Default to 'Available', represented by 0.
        self.day_of_week = day_of_week  # Day of the week for the appointment.
        self.start_time_hour = start_time_hour  # Start time of the appointment (in 24-hour format).

    # Getters
    def get_client_name(self):
        """Return the client's name."""
        return self.client_name

    def get_client_phone(self):
        """Return the client's phone number."""
        return self.client_phone

    def get_appt_type(self):
        """Return the appointment type as an integer."""
        return self.appt_type

    def get_day_of_week(self):
        """Return the day of the week."""
        return self.day_of_week

    def get_start_time_hour(self):
        """Return the starting hour of the appointment."""
        return self.start_time_hour

    def get_appt_type_desc(self):
        """Return a human-readable description of the appointment type."""
        appt_descriptions = [
            "Available",  # 0: Available
            "Mens Cut",  # 1: Mens Cut
            "Ladies Cut",  # 2: Ladies Cut
            "Mens Colouring",  # 3: Mens Colouring
            "Ladies Colouring",  # 4: Ladies Colouring
        ]
        return appt_descriptions[self.appt_type]

    def get_end_time_hour(self):
        """Return the ending hour of the appointment."""
        return self.start_time_hour + 1  # End time is one hour after the start time.

    # Setters
    def set_client_name(self, name):
        """Set the client's name."""
        self.client_name = name

    def set_client_phone(self, phone):
        """Set the client's phone number."""
        self.client_phone = phone

    def set_appt_type(self, appt_type):
        """Set the appointment type."""
        self.appt_type = appt_type

    # Schedule method
    def schedule(self, client_name, client_phone, appt_type):
        """Schedule an appointment with client details and type."""
        self.client_name = client_name
        self.client_phone = client_phone
        self.appt_type = appt_type

    # Cancel method
    def cancel(self):
        """Cancel the appointment and reset its properties."""
        self.client_name = ""
        self.client_phone = ""
        self.appt_type = 0  # Reset to 'Available'.

    # Format record method
    def format_record(self):
        """Return a CSV-style string representation of the appointment."""
        return f"{self.client_name},{self.client_phone},{self.appt_type},{self.day_of_week},{self.start_time_hour}"

    # String representation method
    def __str__(self):
        """Return a user-friendly string representation of the appointment."""
        start_hour = f"{self.start_time_hour}"  # Starting time of the appointment.
        end_hour = f"{self.get_end_time_hour()}"  # Ending time of the appointment.
        return f"{self.client_name}{self.client_phone}{self.day_of_week}{start_hour} - {end_hour}{self.get_appt_type_desc()}"


def create_weekly_calendar():
    """Create a weekly calendar with available appointments."""
    appointments = []  # List to store all appointments.
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']  # Days of the week.
    for day in days_of_week:
        for hour in range(9, 17):  # Appointments are scheduled from 9 AM to 4 PM (16:00).
            appointments.append(Appointment(day_of_week=day, start_time_hour=hour))  # Add appointments.
    return appointments


def load_scheduled_appointments(appointments):
    """Load scheduled appointments from a file."""
    filename = input("Enter the filename to load appointments: ")  # Ask for file name.
    filename = filename.strip()  # Remove any leading or trailing whitespace.
    print(f"Trying to open file: {filename}")  # Debugging print statement.
    
    if not os.path.exists(filename):  # Check if the file exists.
        print("File does not exist.")  # If the file is not found.
        return 0  # Return 0, no appointments loaded.

    count = 0  # Counter to track how many appointments are loaded.
    with open(filename, "r") as file:
        for line in file:  # Read each line in the file.
            client_name, phone, appt_type, day, hour = line.strip().split(",")  # Split line into relevant details.
            appointment = find_appointment(appointments, day, int(hour))  # Find the appointment by day and hour.
            if appointment:
                appointment.schedule(client_name, phone, int(appt_type))  # Schedule the appointment.
                count += 1  # Increment the count for each successfully loaded appointment.
    return count  # Return the number of appointments loaded.


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

    choice = input("Choose an option: ")  # Get user choice.
    return int(choice) if choice.isdigit() and choice in '12345679' else None  # Return the selected option.


def find_appointment(appointments, day, hour):
    """Find an appointment by day and hour."""
    for appt in appointments:  # Iterate through the list of appointments.
        if appt.get_day_of_week() == day and appt.get_start_time_hour() == hour:  # Match day and hour.
            return appt  # Return the appointment if found.
    return None  # Return None if no matching appointment is found.


def show_appointments_by_name(appointments, name):
    """Display all appointments for a given client name."""
    print(f"\nAppointments for {name}:")
    for appt in appointments:
        if name.lower() in appt.get_client_name().lower():  # Case-insensitive search by name.
            print(appt)  # Print the appointment.


def show_appointments_by_day(appointments, day):
    """Display all appointments for a given day."""
    print(f"\nAppointments on {day}:")
    for appt in appointments:
        if appt.get_day_of_week() == day:  # Filter appointments by day of the week.
            print(appt)  # Print each appointment for the specified day.


def reschedule_appointment(appointments):
    """Change an existing appointment to a new time."""
    day = input("Enter the current appointment day: ")  # Get the current appointment day.
    hour = int(input("Enter the current appointment start hour: "))  # Get the current appointment hour.

    current_appt = find_appointment(appointments, day, hour)  # Find the current appointment.
    if current_appt and current_appt.get_appt_type() != 0:  # If appointment exists and is not available.
        print(f"Current appointment: {current_appt}")

        new_day = input("Enter the new day: ")  # Get the new day.
        new_hour = int(input("Enter the new hour: "))  # Get the new hour.
        new_appt = find_appointment(appointments, new_day, new_hour)  # Find the new appointment slot.

        if new_appt and new_appt.get_appt_type() == 0:  # If the new slot is available.
            new_appt.schedule(
                current_appt.get_client_name(),
                current_appt.get_client_phone(),
                current_appt.get_appt_type()
            )  # Schedule the appointment in the new slot.
            current_appt.cancel()  # Cancel the old appointment.
            print(f"Appointment rescheduled to {new_day} at {new_hour}:00.")
        else:
            print("The new time slot is unavailable.")
    else:
        print("No appointment found at the specified time.")


def calculate_daily_fees(appointments):
    """Calculate the total fees for a specific day."""
    day = input("Enter the day to calculate fees for: ")  # Get the day.
    total = sum(get_fee(appt.get_appt_type()) for appt in appointments if appt.get_day_of_week() == day)  # Sum the fees.
    print(f"Total fees for {day}: ${total}")


def calculate_weekly_fees(appointments):
    """Calculate the total fees for the entire week."""
    total = sum(get_fee(appt.get_appt_type()) for appt in appointments)  # Sum the fees for all appointments.
    print(f"Total weekly fees: ${total}")


def get_fee(appt_type):
    """Return the fee for a given appointment type."""
    fees = {1: 40, 2: 60, 3: 40, 4: 80}  # Fee structure for different appointment types.
    return fees.get(appt_type, 0)  # Return the fee, or 0 if the type is unavailable.


def save_appointments(appointments):
    """Save scheduled appointments to a file."""
    filename = input("Enter the filename to save appointments: ")  # Get the filename.
    
    if os.path.exists(filename):  # Check if file exists.
        if input(f"{filename} exists. Overwrite? (y/n): ").lower() != 'y':  # Confirm overwrite.
            print("Save canceled.")
            return 0  # Exit without saving.

    with open(filename, 'w') as file:
        count = 0  # Counter for number of saved appointments.
        for appt in appointments:
            if appt.get_appt_type() != 0:  # Save only scheduled appointments (not available).
                file.write(appt.format_record() + '\n')  # Write the appointment to file.
                count += 1  # Increment the count.
    print(f"{count} appointments saved to {filename}.")  # Print the count of saved appointments.
    return count


def main():
    """Main function to run the appointment management system."""
    appointments = create_weekly_calendar()  # Create the weekly calendar with available appointments.
    load = input("Load existing appointments? (y/n): ")  # Ask whether to load previous appointments.
    if load.lower() == 'y':
        load_scheduled_appointments(appointments)  # Load appointments if user chooses 'y'.
    elif load.lower() != 'y' or load.lower() != 'n':  # Validate input.
        print('Incorrect Input')

    while True:
        choice = print_menu()  # Print the menu and get the user's choice.
        if choice == 1:  # Option to schedule an appointment.
            client_name = input("Enter client name: ")
            client_phone = input("Enter client phone: ")
            appt_type = int(input("Enter appointment type (1: Mens Cut, 2: Ladies Cut, 3: Mens Colouring, 4: Ladies Colouring): "))
            day = input("Enter day of the week: ")
            hour = int(input("Enter start hour(24 hours clock): "))

            appt = find_appointment(appointments, day, hour)  # Find the appointment slot.
            if appt and appt.get_appt_type() == 0:  # If the slot is available.
                appt.schedule(client_name, client_phone, appt_type)  # Schedule the appointment.
                print("Appointment scheduled.")
            else:
                print("Time slot unavailable.")

        elif choice == 2:  # Option to find appointments by name.
            name = input("Enter client name: ")
            show_appointments_by_name(appointments, name)

        elif choice == 3:  # Option to show calendar for a specific day.
            day = input("Enter day of the week: ")
            show_appointments_by_day(appointments, day)

        elif choice == 4:  # Option to cancel an appointment.
            day = input("Enter the day of the appointment to cancel: ")
            hour = int(input("Enter the hour of the appointment to cancel: "))
            appt = find_appointment(appointments, day, hour)  # Find the appointment to cancel.
            if appt:
                appt.cancel()  # Cancel the appointment.
                print(f"Appointment for {day} at {hour}:00 canceled.")
            else:
                print("No appointment found at this time.")

        elif choice == 5:  # Option to reschedule an appointment.
            reschedule_appointment(appointments)

        elif choice == 6:  # Option to calculate daily fees.
            calculate_daily_fees(appointments)

        elif choice == 7:  # Option to calculate weekly fees.
            calculate_weekly_fees(appointments)

        elif choice == 9:  # Option to exit the system.
            save_appointments(appointments)  # Save appointments before exit.
            break


if __name__ == "__main__":
    main()

