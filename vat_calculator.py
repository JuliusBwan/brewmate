#BrewMate Ltd - VAT Calculator

#Chapter 3: data freed from sentences. Marcus-approved arithmetic

from decimal import Decimal, ROUND_HALF_UP

# ---- Piccolo -----
piccolo_machine_name = "Piccolo"
piccolo_machine_price = Decimal("450") #ex-VAT
vat_rate = Decimal("0.20")  #20%, the UK standard rate

piccolo_vat_amount = (piccolo_machine_price * vat_rate).quantize(
    Decimal("0.01"), rounding=ROUND_HALF_UP #to the penny, HALF_UP:house rule
)
piccolo_total_price = piccolo_machine_price + piccolo_vat_amount

print("PICCOLO QUOTE")
print(f"Product: {piccolo_machine_name}")
print(f"Price: £{piccolo_machine_price}")
print(f"VAT (20%): £{piccolo_vat_amount}")
print(f"Total: £{piccolo_total_price}")

print("*" * 10)



# ---- Mezzo ----
mezzo_machine_name = "Mezzo"
mezzo_machine_price = Decimal("1200") #ex-VAT

mezzo_vat_amount = (mezzo_machine_price * vat_rate).quantize(
    Decimal("0.01"), rounding=ROUND_HALF_UP #to the penny, HALF_UP:house rule
)
mezzo_total_price = mezzo_machine_price + mezzo_vat_amount

print("MEZZO QUOTE")
print(f"Product: {mezzo_machine_name}")
print(f"Price: £{mezzo_machine_price}")
print(f"VAT (20%): £{mezzo_vat_amount}")
print(f"Total: £{mezzo_total_price}")
print("*" * 10)



# ---- Grande ----
grande_machine_name = "Grande"
grande_machine_price = Decimal("4800") #ex-VAT

grande_vat_amount = (grande_machine_price * vat_rate).quantize(
    Decimal("0.01"), rounding=ROUND_HALF_UP #to the penny, HALF_UP:house rule
)
grande_total_price = grande_machine_price + grande_vat_amount

print("GRANDE QUOTE")
print(f"Product: {grande_machine_name}")
print(f"Price: £{grande_machine_price}")
print(f"VAT (20%): £{grande_vat_amount}")
print(f"Total: £{grande_total_price}")

print("*" * 10)



# ---- Starter ----
starter_subscription_name = "Starter"
starter_subscription_price = Decimal("4.99") #2kg

starter_vat_amount = (starter_subscription_price * vat_rate).quantize(
    Decimal("0.01"), rounding=ROUND_HALF_UP #to the penny, HALF_UP:house rule
)
starter_total_price = starter_subscription_price + starter_vat_amount

print("STARTER QUOTE")
print(f"Product: {starter_subscription_price}")
print(f"Price: £{starter_subscription_price}")
print(f"VAT (20%): £{starter_vat_amount}")
print(f"Total: £{starter_total_price}")

print("*" * 10)


# ---- Professional ----
professional_subscription_name = "Professional"
professional_subscription_price = Decimal("129") #6kg

professional_vat_amount = (professional_subscription_price * vat_rate).quantize(
    Decimal("0.01"), rounding=ROUND_HALF_UP #to the penny, HALF_UP:house rule
)
professional_total_price = piccolo_machine_price + piccolo_vat_amount

print("PROFESSIONAL QUOTE")
print(f"Product: {professional_subscription_name}")
print(f"Price: £{professional_subscription_price}")
print(f"VAT (20%): £{professional_vat_amount}")
print(f"Total: £{professional_total_price}")

print("*" * 10)


# ---- Enterprise -----
enterprise_subscription_name = "Enterprise"
enterprise_subscription_price = Decimal("299") #15kg + priority support

vat_amount = (enterprise_subscription_price * vat_rate).quantize(
    Decimal("0.01"), rounding=ROUND_HALF_UP #to the penny, HALF_UP:house rule
)
enterprise_total_price = enterprise_subscription_price + vat_amount

print("BREWMATE QUOTE")
print(f"Product: {enterprise_subscription_name}")
print(f"Price: £{enterprise_subscription_price}")
print(f"VAT (20%): £{vat_amount}")
print(f"Total: £{enterprise_total_price}")
print("*" * 10)
