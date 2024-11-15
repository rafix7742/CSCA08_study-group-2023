import random

from constants import *

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

addresses_with_locations = [('1415 W 24TH ST UNIT B', '-95.41766', '29.79856'),
                            ('5101 SOUTHERN PKWY', '-85.78285', '38.15141'),
                            ('514 CRESTWATER CT', '-95.6414', '29.72383'),
                            ('4849 SE ANDEREGG LOOP', '-122.51055', '45.48474'),
                            ('17548 WARRINGTON DR', '-83.14949', '42.4272'), (
                                '3114 S CONGRESS AVE UNIT 210', '-97.76537',
                                '30.24298'),
                            ('4387 ALDERSON CT', '-83.12478', '39.96367'),
                            ('1328 S JAMESTOWN AVE', '-95.90437', '36.14696'),
                            ('3007 BENJAMIN ST NE', '-93.24244', '45.0208'),
                            ('251 GEORGIA AVE SE', '-84.37577', '33.74463'),
                            ('2325 S GRAND AVE', '-118.27398', '33.7334'),
                            ('19611 GARY LEE', '-106.03895', '31.85764'),
                            ('1400 EDGEMONT AVE', '-96.78256', '32.71158'),
                            ('9637 S PEORIA ST', '-87.663', '41.70026'),
                            ('5730 HILLTOP RD', '-89.8497', '35.23876'),
                            ('7231 SUMMIT WATERS LN', '-78.71183', '35.92633'),
                            ('6129 ELTON AVE', '-115.209', '36.17049'),
                            ('3105 18TH ST NE', '-76.97281', '38.92596'),
                            ('5100 SHADY OAK DR', '-83.18472', '40.02197'),
                            ('18705 ASBURY PARK', '-83.1947', '42.42702'),
                            ('3117 CHURCHILL RD', '-121.37655', '38.58512'), (
                                '5535 ACKERFIELD AVE UNIT 26', '-118.18051',
                                '33.86494'),
                            ('7600 KELMSCOT WAY', '-78.636', '35.89772'),
                            ('8611 ROSCOE PL', '-83.15535', '40.09732'),
                            ('4445 40TH AVE S', '-93.22071', '44.93932'),
                            ('1190 SW 16TH AVE', '-80.23495', '25.76657'),
                            ('1350 S WEYANT AVE', '-82.88858', '39.94511'),
                            ('2225 CANTON ST APT 133', '-96.79953', '32.78826'),
                            ('1665 PRINCESS ANNE RD', '-76.03492', '36.73435'),
                            ('8888 S BRYAN AVE', '-119.90216', '36.65344'),
                            ('4682 W JOLINE DR', '-119.87791', '36.80003'),
                            ('2905 W CAMPO BELLO DR', '-112.13184', '33.6296'),
                            ('4517 S PEORIA AVE APT 8', '-95.9641', '36.0975'),
                            ('6830 LIME ROCK BLF', '-98.78885', '29.46899'),
                            ('919 E PASEO WAY', '-112.04949', '33.35911'), (
                                '1620 S MICHIGAN AVE UNIT 1009', '-87.62745',
                                '41.84502'),
                            ('6043 N RIVER TRAIL DR', '-88.042', '43.11443'), (
                                '150 PORTLAND AVE UNIT 500', '-93.26984',
                                '44.98526'), (
                                '424 MISSOURI AVE NW # C', '-77.02323',
                                '38.95295'),
                            ('3368 WEBER ST', '-95.95804', '41.38183'),
                            ('2736 E SCHILLER ST', '-75.10838', '39.98953'),
                            ('527 3RD AVE', '-122.46185', '37.7801'), (
                                '5412 LINDLEY AVE UNIT 204', '-118.51658',
                                '34.15836'), (
                                '4101 CATHEDRAL AVE NW APT 1207', '-77.09139',
                                '38.93822'),
                            ('103 S PARKRIDGE ST', '-97.43463', '37.6639'), (
                                '4833 E JULIAN WASH DRIVE', '-110.93541',
                                '32.14783'),
                            ('4560 S MCDOWELL AVE', '-87.65559', '41.81263'), (
                                '10217 S 183RD AVENUE CIR', '-96.18783',
                                '41.16932'),
                            ('2741 ATWOOD RD NE', '-84.38931', '33.83518'),
                            ('6328 S 73RD EAST AVE', '-95.87955', '36.04113'),
                            ('706 SUMMERWOOD DR', '-97.16237', '32.66223'), (
                                '12236 BEAR VALLEY LN NW', '-106.76522',
                                '35.14097'),
                            ('3323 BLACK FOREST LN', '-86.0004', '39.72311'),
                            ('8607 GILLESPIE ST', '-75.01932', '40.03973'), (
                                '14023 GREENWOOD AVE N # E', '-122.34432',
                                '47.7399'),
                            ('9906 NW LEAHY RD', '-122.81026', '45.55032'),
                            ('5304 ELMWOOD PLZ', '-96.00244', '41.23885'),
                            ('5230 CRIBARI LN', '-121.55913', '37.22285'),
                            ('4744 S RUTLAND AVE', '-85.78555', '38.19052'),
                            ('2715 LYNDALE AVE N', '-93.2979', '44.9993'),
                            ('15301 RINGNECK ST', '-97.22101', '33.01137'),
                            ('6520 E 56TH PL', '-95.88731', '36.09728'),
                            ('2316 NASHBORO BLVD', '-86.66178', '36.10836'), (
                                '275 NE 18TH ST APT 1002', '-80.17395',
                                '25.77719'),
                            ('15467 HARNEY ST', '-96.11665', '41.26408'),
                            ('6950 CHAMBERS DR', '-122.21592', '37.83191'), (
                                '666 OAKLAND AVE APT 105', '-122.21592',
                                '37.83191'),
                            ('1960 PANAY CT', '-117.09193', '32.73756'),
                            ('3406 GREEN HILL DR', '-97.08814', '32.69201'),
                            ('2789 TOMS TRACE CT', '-83.18472', '40.02197'), (
                                '6003 LAKEHURST DR APT 4', '-76.63521',
                                '39.35878'),
                            ('225 74TH ST', '-76.00689', '36.87175'),
                            ('2035 REED GRASS WAY', '-104.71652', '38.85271'),
                            ('5907 S KNOXVILLE AVE', '-95.92315', '36.09725'),
                            ('920 S BOYD AVE # A-B', '-119.75422', '36.73942'),
                            ('3470 E COAST AVE APT H1012', '-80.17798',
                             '25.81538'),
                            ('850 KEARNEY ST', '-104.91648', '39.73375'),
                            ('1348 CYPRESS ST', '-85.82147', '38.23425'),
                            ('2825 PLEASANT AVE', '-93.2937', '44.94364'),
                            ('10175 EDEN MOUNTAIN ST', '-115.2074', '35.98813'),
                            ('2702 S CYPRESS ST', '-97.24604', '37.62944'),
                            ('9775 WALKER RD', '-104.69094', '39.0463'), (
                                '898 OAK ST SW UNIT 3207', '-84.42726',
                                '33.72695'),
                            ('1495 LAFAYETTE DR', '-83.07161', '40.04847'),
                            ('6503 E ONEIDA ST', '-97.22461', '37.70363'),
                            ('1150 FOLSOM ST UNIT 2', '-122.41136', '37.77299'),
                            ('4741 AVENIDA DEL DIABLO', '-115.09135',
                             '36.12141'),
                            ('3629 S MAIN ST', '-97.33843', '32.70678'),
                            ('8034 S CALIFORNIA AVE', '-87.71445', '41.74744'),
                            ('21 N WYNDEN DR UNIT 4', '-95.46806', '29.74849'),
                            ('4 N MOUNT OLIVET LN', '-76.69083', '39.28509'),
                            ('6918 MARINA SHORES CT', '-97.18868', '32.68907'),
                            (
                                '821 DOUGLAS AVE APT 207', '-93.28588',
                                '44.97023'),
                            ('195 CATHCART AVE', '-121.44312', '38.64708'),
                            ('3414 TRAFALGAR PL', '-121.79059', '37.41994'),
                            ('22 PADDLE CT', '-121.51558', '38.61529'),
                            ('11448 WILLET CT S', '-81.50592', '30.35768'),
                            ('38 JONES ST', '-74.00601', '40.73407'),
                            ('5351 ARKOSE DR # 393', '-78.54644', '35.7435'), (
                                '221 W HERNDON AVE SPC 73', '-119.80038',
                                '36.84026'),
                            ('3500 S KING ST', '-105.03966', '39.65169'),
                            ('8180 AYDON DR', '-81.81367', '30.41815'),
                            ('2283 W 25TH ST', '-118.31737', '34.0286'), (
                                '637 DAUPHINE ST APT 639', '-90.07733',
                                '29.95608'),
                            ('6321 BROWN AVE', '-76.54088', '39.28309'),
                            ('8448 JACKIE DR', '-117.03232', '32.80896'),
                            ('5847 CATOMA ST', '-81.75384', '30.2171'), (
                                '1212 DEMONBREUN ST # B2A', '-86.78986',
                                '36.14937'),
                            ('5306 S MEADE AVE', '-87.77057', '41.78175'),
                            ('502 26TH AVE', '-122.29569', '47.60985'),
                            ('4752 SHALIMAR DR', '-90.01739', '30.01948'),
                            ('4167 N 47TH ST', '-87.97636', '43.08634'), (
                                '898 OAK ST SW UNIT 3207', '-84.42726',
                                '33.72695'),
                            ('16702 L ST', '-96.19576', '41.2052'),
                            ('1863 LUCRETIA AVE', '-118.2637', '34.07883'),
                            ('597 KNICKERBOCKER AVE', '-73.92764', '40.6914'),
                            ('4815 FAUNA LN', '-86.32665', '39.81077'), (
                                '1850 COLDWATER CANYON DR', '-118.41505',
                                '34.10251'),
                            ('3415 SIMMONS ST', '-122.16001', '37.79262'),
                            ('44 EAST AVE UNIT 3307', '-97.74248', '30.27022'),
                            ('4017 WOODHAVEN AVE', '-76.67145', '39.3108'),
                            ('4302 CRITES ST', '-95.34521', '29.74961'),
                            ('1623 NW 39TH ST', '-97.53007', '35.51788'),
                            ('7513 SUMMER MEADOWS DR', '-97.40262', '32.62298'),
                            ('1113 TUCKAHOE DR', '-86.77765', '36.23278'),
                            ('6012 TOSCANA AVE', '-97.61439', '30.29474'),
                            ('9100 WESTERN HILLS DR', '-94.59715', '38.9581'),
                            ('3936 COPPER GLEN ST', '-115.29025', '36.23325'),
                            ('140-33 34TH AVE # 1D', '-73.82743', '40.7686'),
                            ('3914 WOODLEAF RD', '-80.78737', '35.22019'),
                            ('1530 MATLOCK DR', '-97.27928', '37.70449'), (
                                '222 N COLUMBUS DR APT 2008', '-87.62197',
                                '41.88527'),
                            ('405 W 7TH ST APT 305', '-80.8447', '35.22773'),
                            ('5647 CANIFF ST', '-83.05601', '42.41003'),
                            ('5028 NE 57TH TER', '-94.5186', '39.21137'), (
                                '4846 BEVENDEAN DR UNIT C9', '-86.72345',
                                '36.06704'), (
                                '1011 AUSTIN HIGHLANDS BLVD', '-97.79822',
                                '30.20743'),
                            ('5135 NORTHCLIFF LOOP E', '-82.97636', '40.08569'),
                            ('3016 SKYLINE MESA DR', '-95.38662', '29.60843'),
                            ('3505 CABOTWOOD CT', '-97.13341', '32.69204'),
                            ('1010 W 13TH ST', '-118.27398', '33.7334'),
                            ('1419 HURLINGHAM WAY', '-121.78733', '37.37453'),
                            ('764 SANTIAGO AVE', '-118.14917', '33.78223'), (
                                '801 NW 47TH AVE APT 114W', '-80.30054',
                                '25.78061'), (
                                '801 S MIAMI AVE UNIT 1208', '-80.20291',
                                '25.76805'),
                            ('2681 CRAZYHORSE PASS', '-97.94676', '30.38079'),
                            ('116 SE 90TH AVE', '-122.5585', '45.51393'),
                            ('1713 NW 9TH ST', '-97.53662', '35.4823'),
                            ('5434 S MONROVIA AVE', '-110.93541', '32.14783'),
                            ('4509 E CALLE TUBERIA', '-111.99309', '33.5194'), (
                                '12606 NW BARNES RD APT 5', '-122.81026',
                                '45.55032'),
                            ('2214 E 27TH ST', '-122.24455', '37.79179'),
                            ('1623 S BEULAH ST', '-75.1514', '39.91175'),
                            ('14066 RED ROCK LAKE DR', '-81.50999', '30.46444'),
                            ('259 VANNOY PARK LANE DR SE', '-84.33218',
                             '33.71277'),
                            ('690 SW 1ST CT APT 2127', '-80.20291', '25.76805'),
                            ('20 W RUSSELL ST', '-83.01262', '39.96633'),
                            ('20141 PARTHENIA ST', '-118.5755', '34.20926'),
                            ('1501 W 19TH ST', '-118.22096', '33.81912'),
                            ('10123 ORCAS AVE', '-118.33468', '34.25861'),
                            ('5768 BERKSHIRE ST', '-82.94147', '42.41074'), (
                                '4975 E BUTLER AVE APT 117', '-119.69736',
                                '36.75119'),
                            ('6400 66TH AVE APT 13', '-121.44266', '38.47473'),
                            ('2589 PARK ST', '-81.68095', '30.31636'),
                            ('7200 MARIGOT RD NW', '-106.76522', '35.14097'),
                            ('312 S 16TH ST # 31', '-95.93224', '41.26231'),
                            ('5760 N ATHENIAN AVE', '-97.36341', '37.77167'),
                            ('2295 SHENANDOAH AVE NE', '-84.38931', '33.83518'),
                            ('11135 PIGEON BLUFF DR', '-95.60324', '29.92673'),
                            ('3207 APOGEE VW', '-104.87023', '38.76744'),
                            ('201 N UNION AVE', '-96.04511', '36.17462'),
                            ('717 MARIGNY ST', '-90.03004', '29.9685'),
                            ('1001 E FORT ST', '-95.91143', '41.29867'),
                            ('3616 COWBOY LN', '-80.8883', '35.31039'),
                            ('12608 SW 26TH ST', '-97.76343', '35.52583'),
                            ('967 DRAUGHON AVE', '-86.77463', '36.10669'),
                            ('9040 NE 139TH ST', '-97.29695', '35.58617'), (
                                '925 GENERAL GEORGE PATTON RD', '-86.97189',
                                '36.05991'),
                            ('2367 STUART ST', '-86.09958', '39.80713'),
                            ('919 PORPOISE ST', '-97.94676', '30.38079'),
                            ('8069 KETTLE DRUM ST', '-104.70084', '38.88996'),
                            ('321 IMLA ST', '-76.54088', '39.28309'),
                            ('4716 BRACKEN DR', '-97.29137', '32.85864'),
                            ('11221 BRISTOL TER', '-94.48667', '38.9308'),
                            ('6205 S 165TH AVE', '-96.19576', '41.2052'),
                            ('221 SW 167TH TER', '-97.55068', '35.32743'),
                            ('2221 RAVEN RD UNIT 103', '-78.62059', '35.94739'),
                            ('3152 HEATHER RIDGE DR', '-121.85237', '37.27192'),
                            ('564 FELL ST', '-122.41931', '37.77956'),
                            ('309 MAXWELL RD', '-86.19338', '39.67254'),
                            ('555 FRONT ST UNIT 903', '-117.18589', '32.7162'),
                            ('7344 FLORAL RIDGE DR', '-81.59465', '30.3728'),
                            ('340 TAMIAMI BLVD', '-80.31228', '25.76335'),
                            ('622 CROWLEY RD', '-97.13901', '32.75459'),
                            ('9252 GILMORE GROVE WAY', '-81.58428', '30.33276'),
                            ('667 SOMERSET TER NE', '-84.35136', '33.78867'),
                            ('986 E DESERT GLEN DR', '-110.98152', '32.46836'),
                            ('2708 22ND AVE', '-122.24455', '37.79179'), (
                                '2742 SE 138TH AVE APT 123', '-122.51055',
                                '45.48474'),
                            ('1168 LEISURE WORLD', '-111.71758', '33.39685')]

postal_codes = []
for i in range(200):
    postal_code_p1 = (random.choice(LETTERS) +
                      str(random.randint(0, 9)) + random.choice(LETTERS))
    postal_code_p2 = (str(random.randint(0, 9)) + random.choice(LETTERS) +
                      str(random.randint(0, 9)))
    postal_codes.append(f"{postal_code_p1} {postal_code_p2}")

room_types = ["living", "bedroom", "bathroom", "kitchen", "garage", "basement"]
cities = ["Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa", "Edmonton",
          "Mississauga", "Winnipeg", "Quebec City", "Hamilton", "Brampton",
          "Surrey", "Laval", "Halifax", "London", "Markham", "Vaughan",
          "Gatineau", "Longueuil", "Burnaby", "Saskatoon", "Kitchener",
          "Windsor", "Regina", "Richmond", "Richmond Hill", "Oakville"]


def record_gen(num_rooms_per_type: int) -> str:
    """ Returns a string representing a record in the data file.

    :param num_rooms_per_type: maximum number of rooms per room type
    """
    address = random.choice(addresses_with_locations)
    postal_code = random.choice(postal_codes)
    rooms = {}
    r_types = random.choices(room_types, k=random.randint(1, 5))

    for r in r_types:
        rooms[r] = []
        for j in range(random.randint(1, num_rooms_per_type)):
            rooms[r].append(
                (random.randint(0, 100) + round(random.random(), 2),
                 random.randint(0, 100) + round(random.random(), 2)))

    # bidding_history = []
    # for j in range(random.randint(0, num_bids)):
    #     if random.randint(1, prob_scientific_bid) == 1:
    #         ten_pow = random.randint(5, 20)
    #         if ten_pow < 10:
    #             ten_pow = f"0{ten_pow}"
    #         else:
    #             ten_pow = str(ten_pow)
    #
    #         dec = str(random.randint(1, 9) + round(random.random(), 2))
    #         if len(dec) < 4:
    #             dec += "0" * (4 - len(dec))
    #
    #         if len(dec) > 4:
    #             dec = dec[:4]
    #
    #         bidding_history.append(f"{dec}E+{ten_pow}")
    #     else:
    #         bidding_history.append(str(random.randint(500000, 10000000)))

    location_data = {"city": random.choice(cities),
                     "longitude": address[1],
                     "latitude": address[2]}

    rooms_str = ""
    for key, value in rooms.items():
        sqrf_str = ""

        for sqrf in value:
            sqrf_str += f"{sqrf[0]} {SQRF_SEP} {sqrf[1]} {SPACE_SEP} "

        sqrf_str = sqrf_str[:-3]

        rooms_str += f"{key}{ROOM_TYPE_DATA_SEP} {sqrf_str}{ROOM_TYPE_SEP} "

    if rooms_str == "":
        rooms_str = f"{ROOM_TYPE_SEP} "

    rooms_str = rooms_str[:-2]

    line_list = [0] * 6
    line_list[ADDRESS_RW] = str(address[0])
    line_list[POSTAL_CODE_RW] = postal_code
    line_list[ROOM_RW] = rooms_str
    # line_list[BIDDING_RW] = (str(bidding_history).replace("[", "")
    #                          .replace("]", "").replace("'", "")
    #                          .replace("\"", ""))

    line_list[CITY_RW] = location_data['city']
    line_list[LONGITUDE_RW] = location_data['longitude']
    line_list[LATITUDE_RW] = location_data['latitude']

    line = DATA_SEP.join(line_list)

    return line


def bidding_gen(record_id: str, num_bids: int, prob_scientific_bid: int) -> str:
    """ Returns a string representing a record bidding in the data file.

    :param record_id: id for this specific bidding record
    :param num_bids: maximum number of bidding history per record
    :param prob_scientific_bid: probability of a scientific bid.
                                1/prob_scientific_bid is the probability of a
                                scientific bid
    """

    bidding_history = []
    for j in range(random.randint(0, num_bids)):
        if random.randint(1, prob_scientific_bid) == 1:
            ten_pow = random.randint(5, 20)
            if ten_pow < 10:
                ten_pow = f"0{ten_pow}"
            else:
                ten_pow = str(ten_pow)

            dec = str(random.randint(1, 9) + round(random.random(), 2))
            if len(dec) < 4:
                dec += "0" * (4 - len(dec))

            if len(dec) > 4:
                dec = dec[:4]

            bidding_history.append(f"{dec}E+{ten_pow}")
        else:
            bidding_history.append(str(random.randint(500000, 10000000)))

    line_tmp = (str(bidding_history).replace("[", "")
                .replace("]", "").replace("'", "")
                .replace("\"", ""))

    line = DATA_SEP.join([str(record_id), line_tmp])
    return line


if __name__ == '__main__':
    with open('sample_example.txt', 'w') as file:
        for i in range(20):
            file.write(record_gen(10) + '\n')

    with open('sample_example_bidding.txt', 'w') as file:
        for i in range(20):
            file.write(bidding_gen(str(i), 10, 10) + '\n')

    with open('long_example.txt', 'w') as file:
        for i in range(200):
            file.write(record_gen(10) + '\n')

    with open('long_example_bidding.txt', 'w') as file:
        for i in range(200):
            file.write(bidding_gen(str(i), 10, 6) + '\n')

    with open('full_example.txt', 'w') as file:
        for i in range(1000):
            file.write(record_gen(random.choice([5, 10, 20, 50, 100])) + '\n')

    with open('full_example_bidding.txt', 'w') as file:
        for i in range(1000):
            file.write(bidding_gen(str(i), random.choice([5, 10, 20, 50, 100]),
                                   10) + '\n')
