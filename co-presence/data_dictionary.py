
# FROM ATUS 2016
# ACTIVITY FILE
# TUACTIVITY_N: Activity line number
# TRTCCTOT_LN: Total time spent during activity providing secondary childcare for all children < 13 (in minutes)
# TRTEC_LN: Time spent providing eldercare by activity (in minutes)
# TUACTDUR: Duration of activity in minutes
# TUCC5: Was at least one of your own household children < 13 in your care during this activity?
# TUCC5B: Was at least one of your non-own household children < 13 in your care during this activity?
# TUSTARTTIM: Activity start time
# TUSTOPTIME: Activity stop time
# TUTIER1CODE: Lexicon Tier 1: 1st and 2nd digits of 6-digit activity code
# TUTIER2CODE: Lexicon Tier 2: 3rd and 4th digits of 6-digit activity code
# TUTIER3CODE: Lexicon Tier 3: 5th and 6th digits of 6-digit activity code
# TEWHERE

ACTIVITY_CODE = {
    '01': {'Personal Care': {
        '01': {'Sleeping': {
            '01': 'Sleeping',
            '02': 'Sleeplessness',
            '99': 'NEC',
        }},
        '02': {'Grooming': {
            '01': 'Washing, dressing and grooming oneself',
            '99': 'NEC',
        }},
        '03': {'Health-related Self Care': {
            '01': 'Health-related Self Care',
            '99': 'NEC',
        }},
        '04': {'Personal Activities': {
            '01': 'Personal/Private activities',
            '99': 'NEC',
        }},
        '05': {'Personal Care Emergencies': {
            '01': 'Personal Emergencies',
            '99': 'NEC',
        }},
        '99': {'Personal Care, NEC': {
            '99': 'NEC',
        }},
    }},


    
    '02': {'name': 'Household Activities', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },
    '03': {'name': 'Personal', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },'Caring For & Helping Household (HH) Members',
    '04': {'name': 'Personal', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },'Caring For & Helping Nonhousehold (NonHH) Members',
    '05': {'name': 'Personal', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },'Work & Work Related Activities',
    '06': {'name': 'Personal', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },'Education',
    '07': {'name': 'Personal', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },'Consumer Purchases',
    '08': {'name': 'Personal', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },'Professional & Personal Care Services',
    '09': {'name': 'Personal', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },'Household Services',
    '10': {'name': 'Personal', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },'Government Services & Civic Obligations',
    '11': {'name': 'Personal', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },'Eating and Drinking',
    '12': {'name': 'Personal', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },'Socializing, Relaxing, and Leisure',
    '13': {'name': 'Personal', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },'Sports, Exercise, and Recreation',
    '14': {'name': 'Personal', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },'Religious and Spiritual Activities',
    '15': {'name': 'Personal', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },'Volunteer Activities',
    '16': {'name': 'Personal', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },'Telephone Calls',
    '18': {'name': 'Personal', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },'Traveling',
    '50': {'name': 'Personal', {
        '01': {'name': 'Sleeping', {
            '01': 'Sleeping',
            '99': 'NEC'
        },'Data Codes',
}

ACTIVITY_WHERE = {1: "Respondent's home or yard",
    2: "Respondent's workplace",
    3: "Someone else's home",
    4: "Restaurant or bar",
    5: "Place of worship",
    6: "Grocery store",
    7: "Other store/mall",
    8: "School",
    9: "Outdoors away from home",
    10: "Library",
    11: "Other place",
    12: "Car, truck, or motorcycle (driver)",
    13: "Car, truck, or motorcycle (passenger)",
    14: "Walking",
    15: "Bus",
    16: "Subway/train",
    17: "Bicycle",
    18: "Boat/ferry",
    19: "Taxi/limousine service",
    20: "Airplane",
    21: "Other mode of transportation",
    30: "Bank",
    31: "Gym/health club",
    32: "Post Office",
    89: "Unspecified place",
    99: "Unspecified mode of transportation"
}


# FROM ATUS 2016
# WHO FILE
# TUACTIVITY_N: Activity line number
# TULINENO: ATUS person line number
# TUWHO_CODE: Who was in the room with you / Who accompanied you?

ACTIVITY_WHO = {18: "Alone",
            19: "Alone",
            20: "Spouse",
            21: "Unmarried partner",
            22: "Own household child",
            23: "Grandchild",
            24: "Parent",
            25: "Brother/sister",
            26: "Other related person",
            27: "Foster child",
            28: "Housemate/roommate",
            29: "Roomer/boarder",
            30: "Other nonrelative",
            40: "Own nonhousehold child < 18",
            51: "Parents (not living in household)",
            52: "Other nonhousehold family members < 18",
            53: "Other nonhousehold family members 18 and older (including parents-in-law)",
            54: "Friends",
            56: "Neighbors/acquaintances",
            57: "Other nonhousehold children < 18",
            58: "Other nonhousehold adults 18 and older",
            59: "Boss or manager",
            60: "People whom I supervise",
            61: "Co-workers",
            62: "Customers"
            }


# PERSON PROPERTIES DEVELOPED FOR LOCATION PERSON MATCHING
# # https://www.bls.gov/tus/overview.htm
# # https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=DEC_10_DP_DPDP1&src=pt

LIFECYCLES = [(0.24, 'Dependent'), # 24%
              (0.38, 'Pre-family'), # 14%
              (0.54, 'Early Family'), # 16%
              (0.70, 'Late Family'), # 16%
              (0.84, 'Post Family'), # 14%
              (1.00, 'Senior') # 16%
             ]
SOCIAL_CLASSES = [(0.01, 'Upper', 440), # 1%
                 (0.16, 'Upper Middle', 147), # 15%
                 (0.46, 'Lower Middle', 75), # 30%
                 (0.76, 'Working', 35), # 30%
                 (0.89, 'Working Poor', 20), # 12%
                 (1.00, 'Underclass', 0) # 12%
                ] # from CPS Household Income jupyter notebook
PSYCHOGRAPHICS = ['active',
                  'sedentary',
                  'healthful',
                  'apathetic',
                  'environmentalist',
                  'extractionist',
                  'introvert',
                  'extrovert',
                  'stressed',
                  'relaxed',
                  'technophile',
                  'technophobe',
                  'republican',
                  'democrat',
                  'entertainment',
                  'enrichment',
                  'status',
                  'humble',
                  'planner',
                  'impulse',
                 ]
