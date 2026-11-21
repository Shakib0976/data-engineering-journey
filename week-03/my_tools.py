def clean_amount(text):
    return float(text.strip().replace("৳", "").replace(",", ""))

def clean_payment(text):
    return text.strip().lower()  

def clean_status(text):
    return text.strip().lower()   

def read_lines(path):
     with open(path, encoding="utf-8") as fh:
        lines = fh.read().strip().split("\n")
     return lines