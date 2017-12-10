# created by jenny trac
# created on dec 8 2017
# program puts a mailing addresses into a list

from enum import Enum

# variables and constants
Provinces = Enum('BC', 'AB', 'SK', 'MB', 'ON', 'QC', 'NB', 'NL', 'NS', 'PE', 'YT', 'NT', 'NU')
Street_types = Enum('Dr.', 'Ave.', 'Rd.', 'Cir.', 'St.')
addresses = []
counter = 0

class MailingAddress():
    def __init__(self, first_name, last_name, house_number, street_name, street_type, city_name, province, postal_code):
        self.first_name = first_name
        self.last_name = last_name
        self.house_number = house_number
        self.street_name = street_name
        self.street_type = street_type
        self.city_name = city_name
        self.province = province
        self.postal_code = postal_code

while counter == 0:
    # input
    print("Format your mailing address:")
    print("First name:")
    f_name = raw_input()
    print("Last name:")
    l_name = raw_input()
    print("House number:")
    h_number = raw_input()
    print("Street name:")
    s_name = raw_input()
    print("Street type:")
    s_type = raw_input()
    print("City:")
    city = raw_input()
    print("Province:")
    prov = raw_input()
    print("Postal code:")
    postal = raw_input()

    # process
    mailing_address = MailingAddress(f_name, l_name, h_number, s_name, s_type, city, prov, postal)
    print(" ")
    if (mailing_address.province in Provinces) and (mailing_address.street_type in Street_types):
        # add to list
        addresses.append(mailing_address)
        # output
        print("Your mailing address:")
        print(" ")
        print(str(mailing_address.first_name) + " " + str(mailing_address.last_name))
        print(str(mailing_address.house_number) + " " + str(mailing_address.street_name) + " " + str(mailing_address.street_type))
        print(str(mailing_address.city_name) + " " + str(mailing_address.province) + "  " + str(mailing_address.postal_code))
        print(" ")
        print(addresses)
        print(" ")
    else:
        if (mailing_address.province in Provinces):
            print("Not a valid street type.")
        elif (mailing_address.street_type in Street_types):
            print("Not a valid province.")
        else:
            print("Not a valid province and not a valid street type.")
