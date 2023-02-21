
rules_dict = {

    # Split into dictionary 1st level categories, second level are what it is
    # 3rd level contains regex to check for (must be lowercase)

    "FOOD" : {
        "Costco" : ".*costco.*",
        "SNOOZE" : ".*snooze.*",
        "HEB" : "h-e-b",
        "Terry Blacks" : "terry.*black",
        "Restaurant" : ["(hamburger|hotdog|pizza|chicken|egg|ramen|taco|coffee|kitch|waffle|kebab|juice|sub|turkey|cookie|pancake|gelato|cafe|candy|food|milkshake|rotisserie|grill|burrito|panini|barbeque|barbecue|fudge|gyro)",
            "whip my soul",
            "yard house",
            "texas roadhouse",
            "frenchys",
            "baked.*bear",
            "kok.*wing",
            "nandos.*peri" , #favorite chicken place
            ],
        "Amy's Ice Cream" : "amy.*ice.*cream",
        "Little Thailand" : "little.*thai",
        "Wendy's" : "wendy",
        "Crumble Cookies" : "crumbl",
        "Veracruz Tacos" : "veracruz",
        "Jersey Mikes" : "jersey.*mikes",
        "Chick Fil A" : "chick.*fil.*a",
        "Interstellar" : "(interstellar.*bbq|noble.*pig)",
        "Tumble22" : "tumble.*22",
        "PTerrys Burgers" : "p.*terry",
        "Raising Canes" : "raising cane",
        "Uber Eats" : "uber.*eats",
        "Roaring Fork" : "roar.*fork",
        "Olive Garden" : "olive.*garden",
        "Store" : "market",
        "Humble Pie Sweets" : "humble.*pie",
        "Hotpot" : "hotpot.*alley",
        "Breakfast Klub" : "breakfast.*klub",
        "Buc-cees" : "buc-ee",
        "Mandola's" : "mandola.*italian",
        "Rouxpour" : "rouxpour",
        "Bojangles" : "bojangles",



    },

    "HOUSE" : {
        "cooper" : ".*cooper.*"
    },

    "WORK" : {
        "Work" : "(intel|verilab|payroll)"
    },
    "BILLS" : {
        "ATT" : "att",
        "Austin Electric" : "city of austin",
        "Gas" : ["(gas|exxon|texaco|pearce|shell)",
                 "7-eleven"
                 ],
        "Progressive Insurance" : "prog county mut",
        "Trash" : "wci.*progressive",
        "Homepro": "home.*pro",
        "Jiffy Lube" : "jiffy.*lube",
        "HomeTeam" : "home.*pest",
    },
    "Bank" : {
      "TransferAcct" : "branchxfr",
      "TransferSavi" : "(to|from) share",
        "BankActivity" : "banking"
    },
    "TRAVEL" : {
        "American Airlines" : "american\s*ai",
        "Hotel" : "(hotel|inn|marriot)",
        "Delta" : "delta.*air",
        "Holiday Inn" : "holiday.*inn",
        "Uber" : "uber.*(?!eat)"

    },
    "MISC" : {
        "Amazon" : "(amzn|amazon)",
        "Walmart" : "(walmart|wal-mart)",
        "YMCA" : "ymca" ,
        "House Stuff" : "(depot|lowe)",
        "Pharmacy" : "(pharmacy|walgreens)",
        "Nintendo" : "nintendo"
    },






}