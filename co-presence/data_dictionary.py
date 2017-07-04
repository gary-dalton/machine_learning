
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
    '02': {'Household Activities': {
        '01': {'Housework': {
            '01': 'Interior cleaning',
            '02': 'Laundry',
            '03': 'Sewing, repairing, & maintaining textiles',
            '04': 'Storing interior hh items, inc. food',
            '99': 'NEC',
        }},
        '02': {'Food & Drink Prep., Presentation, & Clean-up': {
            '01': 'Food and drink preparation',
            '02': 'Food presentation',
            '03': 'Kitchen and food clean-up',
            '99': 'NEC',
        }},
        '03': {'Interior Maintenance, Repair, & Decoration': {
            '01': 'Interior arrangement, decoration, & repairs',
            '02': 'Building and repairing furniture',
            '03': 'Heating and cooling',
            '99': 'NEC',
        }},
        '04': {'Exterior Maintenance, Repair, & Decoration': {
            '01': 'Exterior cleaning',
            '02': 'Exterior repair, improvements, & decoration',
            '99': 'NEC',
        }},
        '05': {'Lawn, Garden, and Houseplants': {
            '01': 'Lawn, garden, and houseplant care',
            '02': 'Ponds, pools, and hot tubs',
            '99': 'NEC',
        }},
        '06': {'Animals and Pets': {
            '01': 'Care for animals and pets (not veterinary care)',
            '02': 'Walking / exercising / playing with animals',
            '99': 'NEC',
        }},
        '07': {'Vehicles': {
            '01': 'Vehicle repair and maintenance (by self)',
            '99': 'NEC',
        }},
        '08': {'Appliances, Tools, and Toys': {
            '01': 'Appliance, tool, and toy set-up, repair, & maintenance (by self)',
            '99': 'NEC',
        }},
        '09': {'Household Management': {
            '01': 'Financial management',
            '02': 'Household & personal organization and planning',
            '03': 'HH & personal mail & messages (except e-mail)',
            '04': 'HH & personal e-mail and messages',
            '05': 'Home security',
            '99': 'NEC',
        }},
        '99': {'Household Activities, NEC': {
            '99': 'NEC',
        }},
    }},
    '03': {'Caring For & Helping Household (HH) Members': {
        '01': {'Caring For & Helping HH Children': {
            '01': 'Physical care for hh children',
            '02': 'Reading to/with hh children',
            '03': 'Playing with hh children, not sports',
            '04': 'Arts and crafts with hh children',
            '05': 'Playing sports with hh children',
            '06': 'Talking with/listening to hh children',
            '08': 'Organization & planning for hh children',
            '09': 'Looking after hh children (as a primary activity)',
            '10': 'Attending hh childrens events',
            '11': 'Waiting for/with hh children',
            '12': 'Picking up/dropping off hh children',
            '99': 'NEC'
        }},
        '02': {'Activities Related to HH Childrens Education': {
            '01': 'Homework (hh children)',
            '02': 'Meetings and school conferences (hh children)',
            '03': 'Home schooling of hh children',
            '04': 'Waiting associated with hh childrens education',
            '99': 'NEC'
        }},
        '03': {'Activities Related to HH Childrens Health': {
            '01': 'Providing medical care to hh children',
            '02': 'Obtaining medical care for hh children',
            '03': 'Waiting associated with hh childrens health',
            '99': 'NEC'
        }},
        '04': {'Caring for Household Adults': {
            '01': 'Physical care for hh adults',
            '02': 'Looking after hh adult (as a primary activity)',
            '03': 'Providing medical care to hh adult',
            '04': 'Obtaining medical and care services for hh adult',
            '05': 'Waiting associated with caring for household adults',
            '99': 'NEC'
        }},
        '05': {'Helping Household Adults': {
            '01': 'Helping hh adults',
            '02': 'Organization & planning for hh adults',
            '03': 'Picking up/dropping off hh adult',
            '04': 'Waiting associated with helping hh adults',
            '99': 'NEC'
        }},
        '99': {'Caring For & Helping Household (HH) Members, NEC': {
            '99': 'NEC',
        }},
    }},
    '04': {'Caring For & Helping NonHousehold (NonHH) Members': {
        '01': {'Caring For & Helping NonHH Children': {
            '01': 'Physical care for nonhh children',
            '02': 'Reading to/with nonhh children',
            '03': 'Playing with nonhh children, not sports',
            '04': 'Arts and crafts with nonhh children',
            '05': 'Playing sports with nonhh children',
            '06': 'Talking with/listening to nonhh children',
            '08': 'Organization & planning for nonhh children',
            '09': 'Looking after nonhh children (as a primary activity)',
            '10': 'Attending nonhh childrens events',
            '11': 'Waiting for/with nonhh children',
            '12': 'Picking up/dropping off nonhh children',
            '99': 'NEC'
        }},
        '02': {'Activities Related to NonHH Childrens Education': {
            '01': 'Homework (nonhh children)',
            '02': 'Meetings and school conferences (nonhh children)',
            '03': 'Home schooling of nonhh children',
            '04': 'Waiting associated with nonhh childrens education',
            '99': 'NEC'
        }},
        '03': {'Activities Related to NonHH Childrens Health': {
            '01': 'Providing medical care to nonhh children',
            '02': 'Obtaining medical care for nonhh children',
            '03': 'Waiting associated with nonhh childrens health',
            '99': 'NEC'
        }},
        '04': {'Caring for NonHousehold Adults': {
            '01': 'Physical care for nonhh adults',
            '02': 'Looking after nonhh adult (as a primary activity)',
            '03': 'Providing medical care to nonhh adult',
            '04': 'Obtaining medical and care services for nonhh adult',
            '05': 'Waiting associated with caring for nonhh adults',
            '99': 'NEC'
        }},
        '05': {'Helping NonHousehold Adults': {
            '01': 'Housework, cooking, & shopping assistance for nonhh adults',
            '02': 'House & lawn maintenance & repair assistance for nonhh adults',
            '03': 'Animal & pet care assistance for nonhh adults',
            '04': 'Vehicle & appliance maintenance/repair assistance for nonhh adults',
            '05': 'Financial management assistance for nonhh adults',
            '06': 'Household management & paperwork assistance for nonhh adults',
            '07': 'Picking up/dropping off nonhh adult',
            '08': 'Waiting associated with helping nonhh adults',
            '99': 'NEC'
        }},
        '99': {'Caring For & Helping NonHH Members, NEC': {
            '99': 'NEC',
        }},
    }},
    '05': {'Work & Work Related Activities': {
        '01': {'Working': {
            '01': 'Work, main job',
            '02': 'Work, other job(s)',
            '03': 'Security procedures related to work',
            '04': 'Waiting associated with working',
            '99': 'NEC'
        }},
        '02': {'Work-Related Activities': {
            '01': 'Socializing, relaxing, and leisure as part of job',
            '02': 'Eating and drinking as part of job',
            '03': 'Sports and exercise as part of job',
            '04': 'Security procedures as part of job',
            '05': 'Waiting associated with work-related activities',
            '99': 'NEC'
        }},
        '03': {'Other Income-generating Activities': {
            '01': 'Income-generating hobbies, crafts, and food',
            '02': 'Income-generating performances',
            '03': 'Income-generating services',
            '04': 'Income-generating rental property activities',
            '05': 'Waiting associated with other income-generating activities',
            '99': 'NEC'
        }},
        '04': {'Job Search and Interviewing': {
            '01': 'Job search activities',
            '02': 'Job interviewing',
            '03': 'Waiting associated with job search or interview',
            '04': 'Security procedures rel. to job search/interviewing',
            '99': 'NEC'
        }},
        '99': {'Work and Work-Related Activities, NEC': {
            '99': 'NEC',
        }},
    }},
    '06': {'Education': {
        '01': {'Taking Class': {
            '01': 'Taking class for degree, certification, or licensure',
            '02': 'Taking class for personal interest',
            '03': 'Waiting associated with taking classes',
            '04': 'Security procedures rel. to taking classes',
            '99': 'NEC'
        }},
        '02': {'Extracurricular School Activities (Except Sports)': {
            '01': 'Extracurricular club activities',
            '02': 'Extracurricular music & performance activities',
            '03': 'Extracurricular student government activities',
            '04': 'Waiting associated with extracurricular activities',
            '99': 'NEC'
        }},
        '03': {'Research/Homework': {
            '01': 'Research/homework for class for degree, certification, or licensure',
            '02': 'Research/homework for class for pers. Interest',
            '03': 'Waiting associated with research/homework',
            '99': 'NEC'
        }},
        '04': {'Registration/Administrative activities': {
            '01': 'Administrative activities: class for degree, certification, or licensure',
            '02': 'Administrative activities: class for personal interest',
            '03': 'Waiting associated w/ admin. activities (education)',
            '99': 'NEC'
        }},
        '99': {'Education, NEC': {
            '99': 'NEC',
        }},
    }},
    '07': {'Consumer Purchases': {
        '01': {'Shopping (Store, Telephone, Internet)': {
            '01': 'Grocery shopping',
            '02': 'Purchasing gas',
            '03': 'Purchasing food (not groceries)',
            '04': 'Shopping, except groceries, food and gas',
            '05': 'Waiting associated with shopping',
            '99': 'NEC'
        }},
        '02': {'Researching Purchases': {
            '01': 'Comparison shopping',
            '99': 'NEC'
        }},
        '03': {'Security Procedures Rel. to Consumer Purchases': {
            '01': 'Security procedures rel. to consumer purchases',
            '99': 'NEC'
        }},
        '99': {'Consumer Purchases, NEC': {
            '99': 'NEC',
        }},
    }},
    '08': {'Professional & Personal Care Services': {
        '01': {'Childcare Services': {
            '01': 'Using paid childcare services',
            '02': 'Waiting associated w/purchasing childcare svcs',
            '99': 'NEC'
        }},
        '02': {'Financial Services and Banking': {
            '01': 'Banking',
            '02': 'Using other financial services',
            '03': 'Waiting associated w/banking/financial services',
            '99': 'NEC'
        }},
        '03': {'Legal Services': {
            '01': 'Using legal services',
            '02': 'Waiting associated with legal services',
            '99': 'NEC'
        }},
        '04': {'Medical and Care Services': {
            '01': 'Using health and care services outside the home',
            '02': 'Using in-home health and care services',
            '03': 'Waiting associated with medical services',
            '99': 'NEC'
        }},
        '05': {'Personal Care Services': {
            '01': 'Using personal care services',
            '02': 'Waiting associated w/personal care services',
            '99': 'NEC'
        }},
        '06': {'Real Estate': {
            '01': 'Activities rel. to purchasing/selling real estate',
            '02': 'Waiting associated w/purchasing/selling real estate',
            '99': 'NEC'
        }},
        '07': {'Veterinary Services (excluding grooming)': {
            '01': 'Using veterinary services',
            '02': 'Waiting associated with veterinary services',
            '99': 'NEC'
        }},
        '08': {'Security Procedures Rel. to Professional/Personal Svcs.': {
            '01': 'Security procedures rel. to professional/personal svcs.',
            '99': 'NEC'
        }},
        '99': {'Professional and Personal Services, NEC': {
            '99': 'NEC',
        }},
    }},
    '09': {'Household Services': {
        '01': {'Household Services (not done by self)': {
            '01': 'Using interior cleaning services',
            '02': 'Using meal preparation services',
            '03': 'Using clothing repair and cleaning services',
            '04': 'Waiting associated with using household services',
            '99': 'NEC'
        }},
        '02': {'Home Maint/Repair/Décor/Construction (not done by self)': {
            '01': 'Using home maint/repair/décor/construction svcs',
            '02': 'Waiting associated w/ home main/repair/décor/constr',
            '99': 'NEC'
        }},
        '03': {'Pet Services (not done by self, not vet)': {
            '01': 'Using pet services',
            '02': 'Waiting associated with pet services',
            '99': 'NEC'
        }},
        '04': {'Lawn & Garden Services (not done by self)': {
            '01': 'Using lawn and garden services',
            '02': 'Waiting associated with using lawn & garden services',
            '99': 'NEC'
        }},
        '05': {'Vehicle Maint. & Repair Services (not done by self)': {
            '01': 'Using vehicle maintenance or repair services',
            '02': 'Waiting associated with vehicle main. or repair svcs',
            '99': 'NEC'
        }},
        '99': {'Household Services, NEC': {
            '99': 'NEC',
        }},
    }},
    '10': {'Government Services & Civic Obligations': {
        '01': {'Using Government Services': {
            '01': 'Using police and fire services',
            '02': 'Using social services',
            '03': 'Obtaining licenses & paying fines, fees, taxes',
            '99': 'NEC'
        }},
        '02': {'Civic Obligations & Participation': {
            '01': 'Civic obligations & participation',
            '99': 'NEC'
        }},
        '03': {'Waiting Associated w/Govt Svcs or Civic Obligations': {
            '01': 'Waiting associated with using government services',
            '02': 'Waiting associated with civic obligations & participation',
            '99': 'NEC'
        }},
        '04': {'Security Procedures Rel. to Govt Svcs/Civic Obligations': {
            '01': 'Security procedures rel. to govt svcs/civic obligations',
            '99': 'NEC'
        }},
        '99': {'Government Services, NEC': {
            '99': 'NEC',
        }},
    }},
    '11': {'Eating and Drinking': {
        '01': {'Eating and Drinking': {
            '01': 'Eating and drinking',
            '99': 'NEC'
        }},
        '02': {'Waiting associated with eating & drinking': {
            '01': 'Waiting associated with eating & drinking',
            '99': 'NEC'
        }},
        '99': {'Eating and Drinking, NEC': {
            '99': 'NEC',
        }},
    }},
    '12': {'Socializing, Relaxing, and Leisure': {
        '01': {'Socializing and Communicating': {
            '01': 'Socializing and communicating with others',
            '99': 'NEC'
        }},
        '02': {'Attending or Hosting Social Events': {
            '01': 'Attending or hosting parties/receptions/ceremonies',
            '02': 'Attending meetings for personal interest (not volunteering)',
            '99': 'NEC'
        }},
        '03': {'Relaxing and Leisure': {
            '01': 'Relaxing, thinking',
            '02': 'Tobacco and drug use',
            '03': 'Television and movies (not religious)',
            '04': 'Television (religious)',
            '05': 'Listening to the radio',
            '06': 'Listening to/playing music (not radio)',
            '07': 'Playing games',
            '08': 'Computer use for leisure (exc. Games)',
            '09': 'Arts and crafts as a hobby',
            '10': 'Collecting as a hobby',
            '11': 'Hobbies, except arts & crafts and collecting',
            '12': 'Reading for personal interest',
            '13': 'Writing for personal interest',
            '99': 'NEC'
        }},
        '04': {'Arts and Entertainment (other than sports)': {
            '01': 'Attending performing arts',
            '02': 'Attending museums',
            '03': 'Attending movies/film',
            '04': 'Attending gambling establishments',
            '05': 'Security procedures rel. to arts & entertainment',
            '99': 'NEC'
        }},
        '05': {'Waiting Associated with Socializing, Relaxing, and Leisure': {
            '01': 'Waiting assoc. w/socializing & communicating',
            '02': 'Waiting assoc. w/attending/hosting social events',
            '03': 'Waiting associated with relaxing/leisure',
            '04': 'Waiting associated with arts & entertainment',
            '99': 'NEC'
        }},
        '99': {'Socializing, Relaxing, and Leisure, NEC': {
            '99': 'NEC',
        }},
    }},
    '13': {'Sports, Exercise, and Recreation': {
        '01': {'Participating in Sports, Exercise, or Recreation': {
            '01': 'Doing Aerobics',
            '02': 'Playing baseball',
            '03': 'Playing basketball',
            '04': 'Biking',
            '05': 'Playing billiards',
            '06': 'Boating',
            '07': 'Bowling',
            '08': 'Climbing, spelunking, caving',
            '09': 'Dancing',
            '10': 'Participating in equestrian sports',
            '11': 'Fencing',
            '12': 'Fishing',
            '13': 'Playing football',
            '14': 'Golfing',
            '15': 'Doing gymnastics',
            '16': 'Hiking',
            '17': 'Playing hockey',
            '18': 'Hunting',
            '19': 'Participating in martial arts',
            '20': 'Playing racquet sports',
            '21': 'Participating in rodeo competitions',
            '22': 'Rollerblading',
            '23': 'Playing rugby',
            '24': 'Running',
            '25': 'Skiing, ice skating, snowboarding',
            '26': 'Playing soccer',
            '27': 'Softball',
            '28': 'Using cardiovascular equipment',
            '29': 'Vehicle touring/racing',
            '30': 'Playing volleyball',
            '31': 'Walking',
            '32': 'Participating in water sports',
            '33': 'Weightlifting/strength training',
            '34': 'Working out, unspecified',
            '35': 'Wrestling',
            '36': 'Doing yoga',
            '99': 'NEC'
        }},
        '02': {'Attending Sporting/Recreational Events': {
            '01': 'Watching aerobics',
            '02': 'Watching baseball',
            '03': 'Watching basketball',
            '04': 'Watching biking',
            '05': 'Watching billiards',
            '06': 'Watching boating',
            '07': 'Watching bowling',
            '08': 'Watching climbing, spelunking, caving',
            '09': 'Watching dancing',
            '10': 'Watching equestrian sports',
            '11': 'Watching fencing',
            '12': 'Watching fishing',
            '13': 'Watching football',
            '14': 'Watching golfing',
            '15': 'Watching gymnastics',
            '16': 'Watching hockey',
            '17': 'Watching martial arts',
            '18': 'Watching racquet sports',
            '19': 'Watching rodeo competitions',
            '20': 'Watching rollerblading',
            '21': 'Watching rugby',
            '22': 'Watching running',
            '23': 'Watching skiing, ice skating, snowboarding',
            '24': 'Watching soccer',
            '25': 'Watching softball',
            '26': 'Watching vehicle touring/racing',
            '27': 'Watching volleyball',
            '28': 'Watching walking',
            '29': 'Watching water sports',
            '30': 'Watching weightlifting/strength training',
            '31': 'Watching people working out, unspecified',
            '32': 'Watching wrestling',
            '99': 'NEC'
        }},
        '03': {'Waiting Associated with Sports, Exercise, & Recreation': {
            '01': 'Waiting related to playing sports or exercising',
            '02': 'Waiting related to attending sporting events',
            '99': 'NEC'
        }},
        '04': {'Security Procedures Rel. to Sports, Exercise, & Recreation': {
            '01': 'Security related to playing sports or exercising',
            '02': 'Security related to attending sporting events',
            '99': 'NEC'
        }},
        '99': {'Sports, Exercise, & Recreation, NEC': {
            '99': 'NEC',
        }},
    }},
    '14': {'Religious and Spiritual Activities': {
        '01': {'Religious/Spiritual Practices': {
            '01': 'Attending religious services',
            '02': 'Participation in religious practices',
            '03': 'Waiting associated w/religious & spiritual activities',
            '04': 'Security procedures rel. to religious & spiritual activities',
            '05': 'Religious education activities',
        }},

        '99': {'Religious and Spiritual Activities, NEC': {
            '99': 'NEC',
        }},
    }},
    '15': {'Volunteer Activities': {
        '01': {'Administrative & Support Activities': {
            '01': 'Computer Use',
            '02': 'Organizing and preparing',
            '03': 'Reading',
            '04': 'Telephone calls (except hotline counseling)',
            '05': 'Writing',
            '06': 'Fundraising',
            '99': 'NEC'
        }},
        '02': {'Social Service & Care Activities (Except Medical)': {
            '01': 'Food preparation, presentation, clean-up',
            '02': 'Collecting & delivering clothing & other goods',
            '03': 'Providing care',
            '04': 'Teaching, leading, counseling, mentoring',
            '99': 'NEC'
        }},
        '03': {'Indoor & Outdoor Maintenance, Building, & Clean-up Activities': {
            '01': 'Building houses, wildlife sites, & other structures',
            '02': 'Indoor & outdoor maintenance, repair, & clean-up',
            '99': 'NEC'
        }},
        '04': {'Participating in Performance & Cultural Activities': {
            '01': 'Performing',
            '02': 'Serving at volunteer events & cultural activities',
            '99': 'NEC'
        }},
        '05': {'Attending Meetings, Conferences, & Training': {
            '01': 'Attending meetings, conferences, & training',
            '99': 'NEC'
        }},
        '06': {'Public Health & Safety Activities': {
            '01': 'Public health activities',
            '02': 'Public safety activities',
            '99': 'NEC'
        }},
        '07': {'Waiting Associated with Volunteer Activities': {
            '01': 'Waiting associated with volunteer activities',
            '99': 'NEC'
        }},
        '08': {'Security Procedures related to volunteer activities': {
            '01': 'Security Procedures related to volunteer activities',
            '99': 'NEC'
        }},
        '99': {'Volunteer Activities, NEC': {
            '99': 'NEC',
        }},
    }},

    '16': {'Telephone Calls': {
        '01': {'Telephone Calls (to or from)': {
            '01': 'Telephone calls to/from family members',
            '02': 'Telephone calls to/from friends, neighbors, or acquaintances',
            '03': 'Telephone calls to/from education services providers',
            '04': 'Telephone calls to/from salespeople',
            '05': 'Telephone calls to/from professional or personal care svcs providers',
            '06': 'Telephone calls to/from household services providers',
            '07': 'Telephone calls to/from paid child or adult care providers',
            '08': 'Telephone calls to/from government officials',
            '99': 'NEC'
        }},
        '02': {'Waiting Associated with Telephone Calls': {
            '01': 'Waiting associated with telephone calls',
            '99': 'NEC'
        }},
        '99': {'Telephone Calls, NEC': {
            '99': 'NEC',
        }},
    }},

    '18': {'Traveling': {
        '01': {'Travel Related to Personal Care': {
            '01': 'Travel related to personal care',
            '99': 'NEC'
        }},
        '02': {'Travel Related to Household Activities': {
            '01': 'Travel related to housework',
            '02': 'Travel related to food & drink prep., clean-up, & presentation',
            '03': 'Travel related to interior maintenance, repair, & decoration',
            '04': 'Travel related to exterior maintenance, repair, & decoration',
            '05': 'Travel related to lawn, garden, and houseplant care',
            '06': 'Travel related to care for animals and pets (not vet care)',
            '07': 'Travel related to vehicle care & maintenance (by self)',
            '08': 'Travel related to appliance, tool, and toy set-up, repair, & maintenance (by self)',
            '09': 'Travel related to household management',
            '99': 'NEC'
        }},
        '03': {'Travel Related to Caring For & Helping HH Members': {
            '01': 'Travel related to caring for & helping hh children',
            '02': 'Travel related to hh childrens education',
            '03': 'Travel related to hh childrens health',
            '04': 'Travel related to caring for hh adults',
            '05': 'Travel related to helping hh adults',
            '99': 'NEC'
        }},
        '04': {'Travel Related to Caring For & Helping Nonhh Members': {
            '01': 'Travel related to caring for and helping nonhh children',
            '02': 'Travel related to nonhh childrens education',
            '03': 'Travel related to nonhh childrens health',
            '04': 'Travel related to caring for nonhh adults',
            '05': 'Travel related to helping nonhh adults',
            '99': 'NEC'
        }},
        '05': {'Travel Related to Work': {
            '01': 'Travel related to working',
            '02': 'Travel related to work-related activities',
            '03': 'Travel related to income-generating activities',
            '04': 'Travel related to job search & interviewing',
            '99': 'NEC'
        }},
        '06': {'Travel Related to Education': {
            '01': 'Travel related to taking class',
            '02': 'Travel related to extracurricular activities (ex. Sports)',
            '03': 'Travel related to research/homework',
            '04': 'Travel related to registration/administrative activities',
            '99': 'NEC'
        }},
        '07': {'Travel Related to Consumer Purchases': {
            '01': 'Travel related to grocery shopping',
            '02': 'Travel related to purchasing gas',
            '03': 'Travel related to purchasing food (not groceries)',
            '04': 'Travel related to shopping, ex groceries, food, and gas',
            '99': 'NEC'
        }},
        '08': {'Travel Related to Using Professional and Personal Care Services': {
            '01': 'Travel related to using childcare services',
            '02': 'Travel related to using financial services and banking',
            '03': 'Travel related to using legal services',
            '04': 'Travel related to using medical services',
            '05': 'Travel related to using personal care services',
            '06': 'Travel related to using real estate services',
            '07': 'Travel related to using veterinary services',
            '99': 'NEC'
        }},
        '09': {'Travel Related to Using Household Services': {
            '01': 'Travel related to using household services',
            '02': 'Travel related to using home main./repair/décor./construction svcs',
            '03': 'Travel related to using pet services (not vet)',
            '04': 'Travel related to using lawn and garden services',
            '05': 'Travel related to using vehicle maintenance & repair services',
            '99': 'NEC'
        }},
        '10': {'Travel Related to Using Govt Services & Civic Obligations': {
            '01': 'Travel related to using government services',
            '02': 'Travel related to civic obligations & participation',
            '99': 'NEC'
        }},
        '11': {'Travel Related to Eating and Drinking': {
            '01': 'Travel related to eating and drinking',
            '99': 'NEC'
        }},
        '12': {'Travel Related to Socializing, Relaxing, and Leisure': {
            '01': 'Travel related to socializing and communicating',
            '02': 'Travel related to attending or hosting social events',
            '03': 'Travel related to relaxing and leisure',
            '04': 'Travel related to arts and entertainment',
            '05': 'Travel as a form of entertainment',
            '99': 'NEC'
        }},
        '13': {'Travel Related to Sports, Exercise, & Recreation': {
            '01': 'Travel related to participating in sports/exercise/recreation',
            '02': 'Travel related to attending sporting/recreational events',
            '99': 'NEC'
        }},
        '14': {'Travel Related to Religious/Spiritual Activities': {
            '01': 'Travel related to religious/spiritual practices',
            '99': 'NEC'
        }},
        '15': {'Travel Related to Volunteer Activities': {
            '01': 'Travel related to volunteering',
            '99': 'NEC'
        }},
        '16': {'Travel Related to Telephone Calls': {
            '01': 'Travel related to phone calls',
            '99': 'NEC'
        }},
        '01': {'Security Procedures Related to Traveling': {
            '01': 'Security procedures related to traveling',
            '99': 'NEC'
        }},
        '99': {'Traveling, NEC': {
            '99': 'NEC',
        }},
    }},
    '50': {'Data Codes': {
        '01': {'Unable to Code': {
            '01': 'Insufficient detail in verbatim',
            '03': 'Missing travel or destination',
            '05': 'Respondent refused to provide information/"none of your business"',
            '06': 'Gap/cannott remember',
            '07': 'Unable to code activity at 1st tier',
        }},
        '99': {'Data codes, NEC': {
            '99': 'NEC',
        }},
    }}
}


    # '99': {'Caring For & Helping Household (nonHH) Members': {
    #     '01': {'Sleeping': {
    #         '01': 'Sleeping',
    #         '02': 'Sleeping',
    #         '03': 'Sleeping',
    #         '04': 'Sleeping',
    #         '05': 'Sleeping',
    #         '06': 'Sleeping',
    #         '99': 'NEC'
    #     }},
    #     '02': {'Sleeping': {
    #         '01': 'Sleeping',
    #         '02': 'Sleeping',
    #         '03': 'Sleeping',
    #         '04': 'Sleeping',
    #         '05': 'Sleeping',
    #         '06': 'Sleeping',
    #         '99': 'NEC'
    #     }},
    #     '03': {'Sleeping': {
    #         '01': 'Sleeping',
    #         '02': 'Sleeping',
    #         '03': 'Sleeping',
    #         '04': 'Sleeping',
    #         '05': 'Sleeping',
    #         '06': 'Sleeping',
    #         '99': 'NEC'
    #     }},
    #     '04': {'Sleeping': {
    #         '01': 'Sleeping',
    #         '02': 'Sleeping',
    #         '03': 'Sleeping',
    #         '04': 'Sleeping',
    #         '05': 'Sleeping',
    #         '06': 'Sleeping',
    #         '99': 'NEC'
    #     }},
    #     '05': {'Sleeping': {
    #         '01': 'Sleeping',
    #         '02': 'Sleeping',
    #         '03': 'Sleeping',
    #         '04': 'Sleeping',
    #         '05': 'Sleeping',
    #         '06': 'Sleeping',
    #         '99': 'NEC'
    #     }},
    #     '06': {'Sleeping': {
    #         '01': 'Sleeping',
    #         '02': 'Sleeping',
    #         '03': 'Sleeping',
    #         '04': 'Sleeping',
    #         '05': 'Sleeping',
    #         '06': 'Sleeping',
    #         '99': 'NEC'
    #     }},
    #     '99': {'Household Activities, NEC': {
    #         '99': 'NEC',
    #     }},
    # }},


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
