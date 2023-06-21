import lib.constants as c

###Config file to maintain the different Fee structure given in the requirement
###For now it supports - only few vehicles
###We can another config maintain different categories of vehicle and align it here
###TODO We can move this to DB if required


employee_vehicle_data = [
    ["Thiyagesh", "TN39AX4099", "CTS"],
    ["Ram", "TN39AX4100", "CTS"],
     ["Raj", "TN39AX4101", "Accenture"],
      ["Alex", "TN39AX4102", "HCL"],
       ["Kumar", "TN39AX4103", "HCL"],
        ["Raghav", "TN39AX4104", "Accenture"],
         ["Prem", "TN39AX4105", "Accenture"],
          ["Alwin", "TN39AX4106", "CTS"]
]
discount_config = {
    "Accenture": 50,
    "CTS": 75,
    "HCL": 25
}

fee_config = {
    c.SMALL_PARKING_AREA : {
        "hourly_rate": False,
        c.MOTORCYCLE: {
            "fee": 10,
            "spots": 2
        },
        c.LWM: {
            "fee": 20,
            "spots": None
        },
        c.HWM: {
            "fee": 50,
            "spots": None
        }
    },
    c.MALL : {
        "hourly_rate": False,
        c.MOTORCYCLE: {
            "fee": 10,
            "spots": 100
        },
        c.LWM: {
            "fee": 20,
            "spots": 80
        },
        c.HWM: {
            "fee": 50,
            "spots": 10
        }
    },
    c.STADIUM: {
        "hourly_rate": True,
        "summing_up": True,
        c.MOTORCYCLE: {
            "fee": {
                "0-4": 30,
                "4-12": 60,
                "12": 100
            },
            "spots": 1000
        },
        c.LWM: {
            "fee": {
                "0-4": 60,
                "4-12": 120,
                "12": 200

            },
            "spots": 1500
        },
        c.HWM: {
            "fee": False,
            "spots": None
        }
    },
    c.AIRPORT: {
        "hourly_rate": True,
        "summing_up": False,
        c.MOTORCYCLE: {
            "fee": {
                "0-1": 0,
                "1-8": 40,
                "8-24": 60
            },
            "day": 80,
            "spots": 200
        },
        c.LWM: {
            "fee": {
                "0-12": 60,
                "12-24": 80
            },
            "day": 100,
            "spots": 500
        },
        c.HWM: {
            "fee": False,
            "spots": 100
        }
    }
}


