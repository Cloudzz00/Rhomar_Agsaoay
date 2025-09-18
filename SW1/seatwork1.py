def convert_usd(usd, india, british, china):
    ruppe = usd * india
    pound = usd * british
    yuan = usd * china
    return ruppe, pound, yuan

india = 88.50   
british = 0.7331  
china = 7.115   

while True:
    value = input("Enter dollar ($) (* to exit): ")
    if value.strip() == "*":
        print("Bye")
        break

    money = value.split("@")
    print(f"{'Dollar ($)':<15}{'Indian Rupee (R)':<20}{'British (Pound)':<20}{'China (Y)':<15}")
    
    for amount in money:
        usd_amt = float(amount)
        val_ruppe, val_pound, val_yuan = convert_usd(usd_amt, india, british, china)
        print(f"{usd_amt:<15}{val_ruppe:<20.2f}{val_pound:<20.2f}{val_yuan:<15.2f}")
