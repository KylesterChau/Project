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


def main():
    # Here are the types of appointments:
    # 0 - Available, 1 = Mens cut $50, 2= Ladies cut $80, 3= Mens Colouring $50, 4= Ladies Colouring $120
    # create a list of 7 appointments for Saturday (between 9:00 and 15:00 start time)
    appt_list = []
    day = "Saturday"
    for time in range(9, 16):
        appt_list.append(Appointment(day, time))

    # Book the first appointment slot (9 AM) for Harvey Wallbanger for a Men's Cut (appt_type = 1)
    current_appt = appt_list[0]
    current_appt.schedule("Harvey", "403-233-3944", 1)

    # Book the second appointment slot (10 AM) for Sara for a Ladies Colouring
    current_appt = appt_list[1]
    current_appt.schedule("Sara", "403-233-3945", 4)

    # Go through all the appointments and find the noon hour slot and book Jenny for a cut
    found = False
    index = 0
    while index < len(appt_list) and not found:
        current_appt = appt_list[index]
        # is this appointment the noon hour appointment for Saturday available?
        if current_appt.get_day_of_week() == "Saturday" and \
           current_appt.get_start_time_hour() == 12 and \
           current_appt.get_appt_type() == 0:
            found = True
        index += 1
    if found:
        # book it!
        current_appt.set_client_name("Jenny")
        current_appt.set_client_phone("403-867-5309")
        current_appt.set_appt_type(2)  # 2 - Ladies Cut
    else:
        print("Appointment entry not found")

    # Print only scheduled appointments using format_record()
    print("Scheduled appointment records:")
    for appt in appt_list:
        if appt.get_appt_type() != 0:
            print(appt.format_record())

    # Cancel Sara's appointment
    current_appt = appt_list[1]
    current_appt.cancel()

    # Print report of all appointment times using string method
    print("\n\n{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name",
        "Phone", "Day", "Start", "End", "Type"))
    for appt in appt_list:
        print(appt)
        
if __name__ == "__main__":
    main()


    

