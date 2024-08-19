def pay_bill(expenses, percent_commission=0.098, offer_amount=None):
    # calculating the total bill amount
    total_bill_amount = 0
    for amount in expenses:
        total_bill_amount += amount

    # calculate extra commision percentage
    extra_commission = 0
    if offer_amount:
        if total_bill_amount >= offer_amount:
            extra_commission = 0.012
            print(f"Congratulations! You earned 1.2% extra commission.")

    # Calculate final payable amount
    commission_amount = total_bill_amount * (percent_commission + extra_commission)
    final_amount = total_bill_amount - commission_amount
    return final_amount


print(pay_bill([300,500,600,700]))

print(pay_bill([300,500,600,700],.098,500))

print(pay_bill([300,500,600,700],.098,800))



