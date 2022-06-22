def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(length_string):
    return len(length_string)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(st1, st2):
    return int(st1) + int(st2)

calendar = {
        1 : {"full_name" : "January",
            "short_name" : "Jan"
        },
        2 : {"full_name" : "February",
            "short_name" : "Feb"
        },
        3 : {"full_name" : "March",
            "short_name" : "Mar"
        },
        4 : {"full_name" : "April",
            "short_name" : "Apr"
        },
        5 : {"full_name" : "May",
            "short_name" : "May"
        },
        6 : {"full_name" : "June",
            "short_name" : "Jun"
        },
        7 : {"full_name" : "July",
            "short_name" : "Jul"
        },
        8 : {"full_name" : "August",
            "short_name" : "Aug"
        },
        9 : {"full_name" : "September",
            "short_name" : "Sep"
        },
        10 : {"full_name" : "October",
            "short_name" : "Oct"
        },
        11 : {"full_name" : "November",
            "short_name" : "Nov"
        },
        12 : {"full_name" : "December",
            "short_name" : "Dec"
        }
    }

def number_to_full_month_name(month_no):
    return calendar[month_no]["full_name"]

def number_to_short_month_name(month_no):
    return calendar[month_no]["short_name"]

def cubed(length):
    return length*length*length

def reverse_string(phrase):
    return phrase[::-1]

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 0.5556
