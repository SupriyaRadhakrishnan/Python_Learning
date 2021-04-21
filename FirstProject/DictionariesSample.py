month_conversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" :"April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
     1: "January",
     2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

print(month_conversions["Nov"])
print(month_conversions.get("Dec"))
print(month_conversions.get("Luv","Not a valid Key")) #second param is the deafult value

print(month_conversions[11])
print(month_conversions.get(12))
print(month_conversions.get(0,"Not a valid Key")) #second param is the deafult value