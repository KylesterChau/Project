class Appointment:
    def __init__(self,day,time):
        self.day=day
        self.time=time
        self.type = 0
        self.name = ""
        self.number = ""

    def schedule(self,name,number,type):
        self.type = type
        self.name = name
        self.number = number
    def get_day_of_week(self):
        self.day
        return self.day
    def get_start_time_hour(self):
        self.time
        return self.time
    def get_appt_type_desc(self):
        if self.type ==0:
            self.type_desc = "Available"
        if self.type:
             self.type_desc = "Men's Cut"
        if self.type:
             self.type_desc = "Ladies Cut"
        if self.type:
             self.type_desc = "Men's Colouring"
        if self.type:
             self.type_desc = "Ladies Colouring"
        return self.type_desc
    def get_end_time_hour(self):
        self.time_end = self.time + 1
        return self.time_end
    def set_appt_type(self,type):
        self.type = type
    def get_appt_type(self):
        self.type
        return self.type
    def set_client_name(self,name):
        self.name = name
    def set_client_phone(self,number):
        self.number = number
    def cancel(self):
        self.name =""
        self.number=""
        self.type=0
    def format_record(self):
        full = self.name,self.number,self.type,self.day,self.time
        return full
    def __str__(self):
        Appointment.get_appt_type_desc(self)
        Appointment.get_end_time_hour(self)
        Appointment.get_day_of_week(self)
        Appointment.get_start_time_hour(self)
        data = ("\n\n{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format(self.name,str(self.number), self.day, str(self.time), str(self.time_end), self.type_desc))
        return data