import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def get_url():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def from_location():
        from_location = config.get('common info','from_location')
        return from_location

    @staticmethod
    def to_location():
        to_location = config.get('common info','to_location')
        return to_location

    @staticmethod
    def depart_date():
        depart_date = config.get('common info','depart_date')
        return depart_date

    @staticmethod
    def return_date():
        return_date = config.get('common info','return_date')
        return return_date

