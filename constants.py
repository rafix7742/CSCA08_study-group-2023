"""CSCA08 Student-led study group (Dec 18th) cumulative project constants

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.
"""

# strings
ROOM_TYPE_SEP = ";"
ROOM_TYPE_DATA_SEP = ":"
SPACE_SEP = "-"
SQRF_SEP = "AND"
DATA_SEP = ","

# index of raw data
ADDRESS_RW = 0
POSTAL_CODE_RW = 1
ROOM_RW = 2
CITY_RW = 3
LONGITUDE_RW = 4
LATITUDE_RW = 5
BIDDING_ID_RW = 0  # always at the end of the data

# index of cleaned data (dictionary)
IDX = 'id'
ADDRESS = 'address'
POSTAL_CODE = 'postal_code'
ROOMS = 'rooms'
LOCATION = 'location'
CITY = 'city'
LONGITUDE = 'longitude'
LATITUDE = 'latitude'
BIDDING = 'bidding'

# types of data
RoomData = list[tuple[float, float]]
HouseRecord = dict[str, str | RoomData | dict[str, str | float] | list[int]]

# integers
NEXT_BID = 10000
