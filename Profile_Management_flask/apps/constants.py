"""
This module defines constants used throughout the application
"""
DATA = {"records": [
    {'username': 'kumarmarshal', 'name': 'kumarm', 'dept': 'IT', 'dob': '2000-01-01', 'gender': 'M', 'isadmin': False},
    {'username': 'naveenbireddy', 'name': 'naveenb', 'dept': 'Dev', 'dob': '2000-02-02', 'gender': 'M','isadmin': False},
    {'username': 'adveshkairamkonda', 'name': 'adveshk', 'dept': 'Sales', 'dob': '2000-02-22', 'gender': 'M',  'isadmin': True}
]}
VALID_GENDER = ["MALE", "FEMALE", "OTHERS", "M", "F"]
USERS = ["kumarm", "naveenb"]
ADMINS = ["adveshk"]
ALL_USERS = ["kumarm", "naveenb", "adveshk"]
PASSWORDS = {
                "adveshk": "Advesh@0202",
                 "naveenb": "Naveen@0202",
                 "kumarm": "Kumar@0101"
            }
# create_user constant values
ADMIN = "admin"
NORMAL = "normal"
SUCCESS = "success"
FAILED = "failed"

# emails configurations
# email configurations
SMTP_PORT = 587  # For starttls
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "adveshk22@gmail.com"
RECEIVER_EMAIL = ["adveshk22@gmail.com", "adveshhh.k@gmail.com"]
PASSWORD = "uuphxybkxlowcpgp"

DELETE_MESSAGE = """
Hlo Team,\n
Admin has deleted user {} Record in DATA
Thank you 
"""
UPDATE_MESSAGE = """
Hlo Team,\n
Admin has updated user={} record.
Record = {}\n
Thank You
"""
GET_ALL_MESSAGE = """
Hlo Team,\n
User, is checking all users information from the table.\n
Thank You
"""
PARTIAL_UPDATE = """
Hlo Team\n
Admin has partially updated the user={} records in DATA.\n
Partially updated user record = {}\n
Thank you
"""
UNAUTHENTICATED_MESSAGE = """
Hlo team\n
ALERT:-Unauthenticated user={}, trying to access the application
check logs\n
Thank You
"""
UPDATE_USER_RECORD = """
Hlo team\n
''User={} has updated his profile''
Updated Record = {}
\nThank you
"""
RECORD_ADDED = """
Hlo Team,\n 
Admin={} added the user={} record = {}.\n
Thank You
"""
RESET_PASSWORD = """
Hlo Team\n
Admin has reseted the user={} password\n
Thank You
"""
CHECK_USER_INFO = """
Hlo Team,\n
Admin checking user={} information.\n
Thank You
"""
USER_INFO = """
Hlo Team,\n
User={} checking his information.\n
Thank You
"""
