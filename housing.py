"""CSCA08 Student-led study group (Dec 18th) cumulative project

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.
"""

from typing import TextIO

from constants import ADDRESS_RW, POSTAL_CODE_RW, ROOM_RW, CITY_RW, \
    LONGITUDE_RW, LATITUDE_RW, BIDDING_ID_RW, IDX, ADDRESS, POSTAL_CODE, \
    ROOMS, LOCATION, LATITUDE, LONGITUDE, CITY, BIDDING, HouseRecord, \
    RoomData, ROOM_TYPE_SEP, SQRF_SEP, DATA_SEP, ROOM_TYPE_DATA_SEP, SPACE_SEP

EXAMPLE_DATA = [
    {'id': 0, 'address': '764 SANTIAGO AVE', 'postal_code': 'M9C 9G8',
     'location': {'latitude': '33.78223', 'longitude': '-118.14917',
                  'city': 'London'},
     'rooms': {
         'bedroom': [(46.97, 93.01), (73.09, 29.68)],
         'kitchen': [(41.04, 32.48)]},
     'bidding': None
     },
    {'id': 1, 'address': '3114 S CONGRESS AVE UNIT 210',
     'postal_code': 'I4S 8U2',
     'location': {'latitude': '30.24298', 'longitude': '-97.76537',
                  'city': 'Edmonton'},
     'rooms': {'bathroom': [(67.39, 19.34)], 'bedroom': [(10.84, 1.9)],
               'kitchen': [(17.03, 47.03)]},
     'bidding': [101231, 452342, 567812, 128623, 109348]
     },
    {'id': 2, 'address': '20141 PARTHENIA ST', 'postal_code': 'N1P 4B4',
     'location': {'latitude': '34.20926', 'longitude': '-118.5755',
                  'city': 'Burnaby'},
     'rooms': {'basement': [(61.58, 92.71), (97.14, 28.49)]},
     'bidding': [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000]
     }
]


def get_house(records: list[HouseRecord],
              identifier: int) -> HouseRecord | None:
    """Returns the house record with the identifier 'identifier' from the list
    of records 'records'."""

    for house in records:
        if house[IDX] == identifier:
            return house

    return None


# Complete the code for the following function
def read_bid(file: TextIO, data: list[HouseRecord]) -> list[HouseRecord]:
    """Reads the bid data from a file 'file' and complete the list the data
    'data' with the bid data."""

    pass


def read_room(rooms: str) -> dict[str, RoomData]:
    """Reads the room data from a string 'rooms' and returns a dictionary of
    room data.

    >>> read_room("Bedroom: 10.0 AND 10.0; Living Room: 20.0 AND 20.0")
    {'Bedroom': [(10.0, 10.0)], 'Living Room': [(20.0, 20.0)]}
    """

    room_types = rooms.split(ROOM_TYPE_SEP)
    room_data = {}

    for room_type in room_types:
        room_type = room_type.strip().split(ROOM_TYPE_DATA_SEP)
        room_type_name = room_type[0]
        room_type_data = room_type[1].strip().split(SPACE_SEP)

        for i in range(len(room_type_data)):
            room_type_data[i] = room_type_data[i].strip().split(SQRF_SEP)
            room_type_data[i] = (float(room_type_data[i][0]),
                                 float(room_type_data[i][1]))

        room_data[room_type_name] = room_type_data

    return room_data


def read_data(file: TextIO, bid_file: TextIO) -> list[HouseRecord]:
    """Reads data from a file 'file' and returns a list of House records."""

    data = []
    lines = file.readlines()
    i = 0

    for line in lines:
        house = {IDX: i}
        line = line.strip().split(DATA_SEP)

        house[ADDRESS] = line[ADDRESS_RW]
        house[POSTAL_CODE] = line[POSTAL_CODE_RW]
        house[LOCATION] = {
            LATITUDE: line[LATITUDE_RW],
            LONGITUDE: line[LONGITUDE_RW],
            CITY: line[CITY_RW]
        }

        house[ROOMS] = read_room(line[ROOM_RW])

        data.append(house)
        i += 1

    # This is where the read_bid function is called (Uncomment to use)
    # data = read_bid(bid_file, data)

    return data


if __name__ == '__main__':
    with open('sample_example.txt', 'r') as f:
        d = read_data(f, f)

    print(d[:5])
