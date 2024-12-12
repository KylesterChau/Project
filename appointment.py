class Appointment:
    def __init__(self, day_of_week, start_time_hour):
        self.__client_name = ""
        self.__client_phone = ""  # Changed to string
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