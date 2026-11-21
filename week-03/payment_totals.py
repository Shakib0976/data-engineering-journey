import os


def clean_amount(text):
    return float(text.strip().replace("৳", "").replace(",", ""))

def clean_payment(text):
    return text.strip().lower()  

def clean_status(text):
    return text.strip().lower()   


def main () :
    PATH = os.path.join( "data", "raw_sales.txt")

    with open(PATH, encoding="utf-8") as fh:
        lines = fh.read().strip().split("\n")

    bkash_total = 0.0
    bkash_count = 0
    nagad_count = 0
    nagad_total = 0.0
    card_total = 0.0
    card_count = 0
    rocket_total = 0.0
    rocket_count = 0
    cash_on_delivery_total = 0.0
    cash_on_delivery_count = 0
    total_amount = 0.0


   

    for raw in lines:
        parts   = raw.split(";")
    
    
        # level 01 task
    
        # amount  = float(parts[5].strip().replace("৳", "").replace(",", ""))
        # payment = parts[6].strip().lower()
        # status  = parts[7].strip().lower()
    
        amount  = clean_amount(parts[5])
        payment = clean_payment(parts[6])
        status  = clean_status(parts[7])
    
        if status == "cancelled":
              continue
    
        if payment == "bkash":
              bkash_total = bkash_total + amount
              bkash_count = bkash_count + 1
        elif payment == "nagad":
             nagad_total = nagad_total + amount
             nagad_count = nagad_count + 1
        elif payment == "card":
                card_total = card_total + amount
                card_count = card_count + 1
        elif payment == "rocket":
                rocket_total = rocket_total + amount
                rocket_count = rocket_count + 1
        elif payment == "cash on delivery":
                cash_on_delivery_total = cash_on_delivery_total + amount
                cash_on_delivery_count = cash_on_delivery_count + 1
        

    total_amount = (bkash_total + nagad_total + card_total + rocket_total + cash_on_delivery_total)




    print("লেভেল ১")
    print(f"bkash  {bkash_count}টা  ৳{bkash_total:.2f}")
    print(f"nagad  {nagad_count}টা  ৳{nagad_total:.2f}")
    print(f"card   {card_count}টা  ৳{card_total:.2f}")
    print(f"rocket {rocket_count}টা  ৳{rocket_total:.2f}")
    print(f"cash on delivery {cash_on_delivery_count}টা  ৳{cash_on_delivery_total:.2f}")
    print(f"সব মিলিয়ে:  ৳{total_amount:.2f}")
    print()
   



if __name__ == "__main__":
    main()

