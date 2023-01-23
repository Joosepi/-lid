sales = {
    "Johnver": {
        "expenses": {
            "tea": 190,
            "coffe": 325,
            "water": 682,
            "milk": 829

        },
        "revenue": {
            "tea": 120,
            "coffe": 300,
            "water": 50,
            "milk": 67

        }
    },
    "Vanston": {
        "expenses": {
            "tea": 190,
            "coffe": 325,
            "water": 682,
            "milk": 829

        },
        "revenue": {
             "tea": 140,
            "coffe": 19,
            "water": 14,
            "milk": 140

        }
    },
     "Danbree": {
        "expenses": {
            "tea": 890,
            "coffe": 23,
            "water": 1290,
            "milk": 89

        },
        "revenue": {
             "tea": 1926,
            "coffe": 293,
            "water": 852,
            "milk": 609

        }
    },
     "Vansey": {
        "expenses": {
            "tea": 54,
            "coffe": 802,
            "water": 12,
            "milk": 129

        },
        "revenue": {
             "tea": 14,
            "coffe": 1491,
            "water": 56,
            "milk": 120
        }
    },
     "Mundyke": {
        "expenses": {
            "tea": 430,
            "coffe": 235,
            "water": 145,
            "milk": 76

        },
        "revenue": {
             "tea": 143,
            "coffe": 162,
            "water": 659,
            "milk": 87

        }
    }
}
for k, v in sales.items():
    print(k)
    print(v['revenue'])
    print(v['expenses'])