import os
def load_scheduled_appointments(appointments):
    filename = input("Enter the filename to load appointments: ")
    filename = filename.strip()  # Remove any leading or trailing whitespace
    print(f"Trying to open file: {filename}")  # Debug print statement
    
    if not os.path.exists(filename):
        print("File does not exist.")
        return 0

    count = 0
    with open(filename, "r") as file:
        for line in file:
            client_name, phone, appt_type, day, hour = line.strip().split(",")
            appointment = find_appointment_by_time(appointments, day, int(hour))
            if appointment:
                appointment.schedule(client_name, phone, int(appt_type))
                count += 1
    return count

def change_appointment_by_day_time(appointments):
    old_day = input("Enter the day of the appointment to change: ")
    old_hour = int(input("Enter the hour of the appointment to change: "))

    old_appt = find_appointment_by_time(appointments, old_day, old_hour)

    if old_appt:
        new_day = input("Enter the new day: ")
        new_hour = int(input("Enter the new hour: "))
        new_appt = find_appointment_by_time(appointments, new_day, new_hour)
        if new_appt and new_appt.get_appt_type() == 0:
            new_appt.schedule(old_appt.get_client_name(), old_appt.get_client_phone(), old_appt.get_appt_type())
            old_appt.cancel()
            print(f"Appointment changed for {old_appt.get_client_name()} to {new_day} at {new_hour}.")
        else:
            print("New appointment time is unavailable.")
    else:
        print("Appointment not found.")

def save_scheduled_appointments(appointments):
    filename = input("Enter the filename to save appointments: ")
    filename = filename.strip()
    if os.path.exists(filename):
        confirm = input("File exists. Overwrite? (yes/no): ")
        if confirm.lower() != "yes":
            return 0

    count = 0
    with open(filename, "w") as file:
        for appt in appointments:
            if appt.get_appt_type() != 0:
                file.write(appt.format_record() + "\n")
                count += 1
    return count