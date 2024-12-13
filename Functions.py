import os

appointments = []
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

class Appointment:
    def __init__(self, day_of_week, start_time_hour):
        self.__client_name = ""
        self.__client_phone = ""
        self.__appt_type = 0
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour

    def get_client_name(self):
        return self.__client_name

    def set_client_name(self, value):
        self.__client_name = value

    def get_client_phone(self):
        return self.__client_phone

    def set_client_phone(self, value):
        self.__client_phone = value

    def get_appt_type(self):
        return self.__appt_type

    def set_appt_type(self, value):
        self.__appt_type = value

    def get_day_of_week(self):
        return self.__day_of_week

    def set_day_of_week(self, value):
        self.__day_of_week = value

    def get_start_time_hour(self):
        return self.__start_time_hour

    def set_start_time_hour(self, value):
        self.__start_time_hour = value

    def get_appt_type_desc(self):
        match self.__appt_type:
            case 0:
                return "Available"
            case 1:
                return "Mens Cut"
            case 2:
                return "Ladies Cut"
            case 3:
                return "Mens Colouring"
            case 4:
                return "Ladies Colouring"

    def get_end_time_hour(self):
        return self.__start_time_hour + 1

    def schedule(self, client_name, client_phone, appt_type):
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = appt_type

    def cancel(self):
        self.__client_name = ""
        self.__client_phone = ""
        self.__appt_type = 0

    def format_record(self):
        return f"{self.__client_name},{self.__client_phone},{self.__appt_type},{self.__day_of_week},{self.__start_time_hour}"

    def __str__(self):
        return f"{self.__client_name:20s}{self.__client_phone:15s}{self.__day_of_week:10s}{self.get_end_time_hour():10d}{self.get_appt_type_desc():20s}"

def create_weekly_calendar(appointments):
    appointments.clear() 
    for day in days_of_week:
        for hour in range(9, 17):
            new_Appointment = Appointment(day, hour)
            appointments.append(new_Appointment)

def load_scheduled_appointments(appointments):
    """Load appointments from a file and schedule them in the calendar."""
    fileName = input("Enter the filename to load appointments: ")

    if not os.path.exists(fileName):
        print("File not found.")
        return 0

    with open(fileName, 'r') as file:
        count = 0
        for line in file:
            client_name, client_phone, appt_type, day, hour = line.strip().split(',')
            appt_type, hour = int(appt_type), int(hour)

            appointment = find_appointment(appointments, day, hour)
            if appointment:
                appointment.schedule(client_name, client_phone, appt_type)
                count += 1
    print(f"{count} appointments loaded from {fileName}.")
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
    if choice.isdigit() and choice in '12345679':
        choice = int(choice)
    else:
        choice = None
    return choice

def find_appointment(appointments, day, hour):
    """Find an appointment by day and hour."""
    for apt in appointments:
        if apt.get_day_of_week() == day and apt.get_start_time_hour() == hour:
            return apt
    return None

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

