deposit = float(input())
months = int(input())
annual_percent = float(input())
# сума = депозирана  + срок депозита * ((депоз. сума * год. лих. %   ) / 12)
annual_interest = deposit * annual_percent / 100
monthly_interest = annual_interest / 12
total_sum = deposit + (months * monthly_interest)
print(total_sum)