"""CSCA08 Student-led study group (Dec 18th) cumulative project solutions

For maximum learning, please try to solve the problems yourself before
looking at these solutions. These solutions are only one way to solve
the problems. There are many other ways to solve them. you may have
come up with a better solution yourself!

if there is any problem with the solutions, please let us know as soon as
possible, so we can fix it for everyone.
"""

from typing import TextIO
from constants import ADDRESS, BIDDING, BIDDING_ID_RW, DATA_SEP, NEXT_BID, \
    POSTAL_CODE, HouseRecord, ROOMS, IDX

test_data = [{'id': 1,
              'address': '4849 SE ANDEREGG LOOP',
              'postal_code': 'E0L 3B6',
              'rooms': {'garage': [(38.02, 37.46)],
                        'basement': [(11.16, 46.96)]},
              'location': {'city': 'Saskatoon',
                           'longitude': -122.51055,
                           'latitude': 45.48474},
              'bidding': [5200000000, 6997401]
              },
             {'id': 2,
              'address': '48www49 SE ANDEREGG LOOP',
              'postal_code': 'EaL 3B6',
              'rooms': {'garage': [(38.02, 37.46), (98.02, 37.46)],
                        'basement': [(21.16, 46.96), (38.02, 92.2)]},
              'location': {'city': 'Saskatoon',
                           'longitude': -122.51055,
                           'latitude': 45.48474},
              'bidding': [52000, 6901]
              }

             ]


def get_house(records: list[HouseRecord], idx: int) -> HouseRecord | None:
    # iterates through all records
    for house in records:
        # checks the ID index of each house against the idx
        if house[IDX] == idx:
            # we return the house when the house index is the same as the 
            # desired index
            return house
    # if we go through the entire list with no matches, we return None
    return None


def find_next_bid(records: list[HouseRecord], idx: int) -> int:
    # We use our helper function get_house to get the house we will use
    house = get_house(records, idx)

    # We check if the house DNE
    if house is None:
        return 0

    # If the house DNE we return immediately
    if house[BIDDING] is None:
        return 0

    # We set the highest bid to be a super low value (zero since it can't be
    # negative)
    biggest_bid = 0

    # we iterate through all the house's bids
    for bid in house[BIDDING]:

        # if the bid is bigger than the current biggest bid, that bid is now
        # the biggest
        if bid > biggest_bid:
            biggest_bid = bid

    # return the biggest bid + whatever the minimum increase is (current =
    # 10,000)
    return biggest_bid + NEXT_BID


def find_smallest_room(records: list[HouseRecord], idx: int) -> str:
    # Set the name of the smallest room to an empty string
    smallest = ''

    # Pick an extremely large number to compare against (the area of one room
    # should not be bigger than this)
    smallest_area = 9999999

    # Get the house from the records based on id
    house = get_house(records, idx)

    # check if the house DNE
    if house is None:
        return ''

    # Iterate through all the room types of the house (basement, bedroom
    # ...)
    for room_type in house[ROOMS]:
        # From that room type iterate through all the rooms of that kind
        # (all bathrooms, all bedrooms...)
        for room in house[ROOMS][room_type]:
            # We know each room is a Tuple of length and width, L*W = Area
            area = room[0] * room[1]

            # Check if the area of the room is less than the smallest (for
            # the first value this will always be met as a cond.)
            if area < smallest_area:
                # We then set the new smallest area to whatever the area of
                # the room just checked is
                # We also set the smallest room to the room type as we are
                # asked for the type, not the measurement
                smallest = room_type
                smallest_area = area

    # Return the smallest room of x kind
    return smallest


def find_largest_room(records: list[HouseRecord], idx: int) -> str:
    # Set the name of the smallest room to an empty string
    biggest = ''

    # Pick an extremely small number to compare against (a room will not have
    # a negative area)
    biggest_area = 0

    # Get the house from the records based on id
    house = get_house(records, idx)

    # check if the house DNE
    if house is None:
        return ''

    # Iterate through all the room types of the house (basement, bedroom
    # ...)
    for room_type in house[ROOMS]:

        # From that room type iterate through all the rooms of that kind
        # (all bathrooms, all bedrooms...)
        for room in house[ROOMS][room_type]:

            # We know each room is a Tuple of length and width, L*W = Area
            area = room[0] * room[1]

            # Check if the area of the room is greater than the biggest room
            # (for the first value this will always be met as a cond.)
            if area > biggest_area:
                # We then set the new biggest area to whatever the area of
                # the room just checked is
                # We also set the biggest room to the room type as we are
                # asked for the type, not the measurement
                biggest = room_type
                biggest_area = area

    # Return the biggest room of type x
    return biggest


def get_average_room_size(records: list[HouseRecord], idx: int) -> float:
    # Create a new variable for the areas of the rooms
    all_room_sizes = 0

    # Create a new variable for the count of rooms
    room_count = 0

    # Get the house from the records based on id
    house = get_house(records, idx)

    # check if the house DNE
    if house is None:
        return 0.0

    # Iterate through all the room types of the house (basement, bedroom
    # ...)
    for room_type in house[ROOMS]:

        # From that room type iterate through all the rooms of that kind
        # (all bathrooms, all bedrooms...)
        for room in house[ROOMS][room_type]:
            # Add the area of each room to the running total of the room sizes
            all_room_sizes += room[0] * room[1]

            # Add one to the total room count for each room
            room_count += 1

    # Return the average (room areas/ # of rooms)
    return all_room_sizes / room_count


def add_room(records: list[HouseRecord], idx: int, room_type: str,
             length: float, width: float) -> None:
    """
    Don't forget the precondition: there exist a house with the identifier
    """

    # Get the house from the records based on id
    house = get_house(records, idx)

    # If the room already exists then we can just add the length and width
    # Tuple into the existing room type list
    if room_type in house[ROOMS].keys():

        # We append to the existing key 'room_type' list (ie. 'basement':[
        # .....])
        house[ROOMS][room_type].append((length, width))

    # if the room type doesn't exist then we create a new key in the rooms
    # dictionary
    else:

        # Key = room_type which is a list of Tuples where each Tuple is
        # length and width
        house[ROOMS][room_type] = [(length, width)]


def change_address(records: list[HouseRecord], idx: int,
                   address: str, postal_code: str, cond: int) -> None:
    # I think you get the idea
    house = get_house(records, idx)

    # If the house DNE we return immediately since there is nothing to change
    # for a record that DNE
    if not house:
        return

    # cond == 0 means we only change address
    elif cond == 0:
        # At the address key of ADDRESS we change the value to be the new
        # address
        house[ADDRESS] = address

    # cond == 1 means we only change the postal code
    elif cond == 1:

        # At the postal_code key of POSTAL_CODE we change the value to be the
        # new postal_code
        house[POSTAL_CODE] = postal_code

    # cond == 2 means we change both address and postal code
    else:

        # We apply the processes of cond == 0 and cond == 1
        house[ADDRESS] = address
        house[POSTAL_CODE] = postal_code

        # Note: we are using else here since we are only checking valid
        # input, if cond == 3 it will produce the same output as cond == 2,
        # since input must be valid, this is not a concern


def read_bid(file: TextIO, data: list[HouseRecord]) -> list[HouseRecord]:
    """Reads the bid data from a file 'file' and complete the list the data
    'data' with the bid data."""

    # We read the file and split it into lines
    lines = file.readlines()

    # We iterate through the lines
    i = 0

    for line in lines:

        # We split the line into a list of strings
        line = line.strip().split(DATA_SEP)
        bidding = []

        # We iterate through the list of strings
        for bid in line[BIDDING_ID_RW:]:

            # We check if the bid is in scientific notation
            if "E" in bid:

                # We split the bid into the number and the exponent
                bid = bid.split("E")
                bid = int(float(bid[0]) * 10 ** int(bid[1]))
            else:

                # We convert the bid to an integer
                bid = int(bid)

            # We append the bid to the bidding list
            bidding.append(bid)

        # We add the bidding list to the data
        data[i][BIDDING] = bidding
        i += 1

    # We return the data
    return data


if __name__ == '__main__':
    pass
