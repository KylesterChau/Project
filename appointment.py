

class Appointment:
    def __init__(self, day_of_week, start_time_hour):
        """
        Initialize an Appointment object with default properties.
        day_of_week: The day of the week for the appointment.
        start_time_hour: The starting hour of the appointment.
        """
        self.client_name = ""
        self.client_phone = ""
        self.appt_type = 0  # Default to 'Available'
        self.day_of_week = day_of_week
        self.start_time_hour = start_time_hour

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
            "Available",
            "Mens Cut",
            "Ladies Cut",
            "Mens Colouring",
            "Ladies Colouring",
        ]
        return appt_descriptions[self.appt_type]

    def get_end_time_hour(self):
        """Return the ending hour of the appointment."""
        return self.start_time_hour + 1

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
        self.appt_type = 0

    # Format record method
    def format_record(self):
        """Return a CSV-style string representation of the appointment."""
        return f"{self.client_name},{self.client_phone},{self.appt_type},{self.day_of_week},{self.start_time_hour}"

    # String representation method
    def __str__(self):
        """Return a user-friendly string representation of the appointment."""
        start_hour = f"{self.start_time_hour}"
        end_hour = f"{self.get_end_time_hour()}"
        return f"{self.client_name}{self.client_phone}{self.day_of_week}{start_hour} - {end_hour}{self.get_appt_type_desc()}"
