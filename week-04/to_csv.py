import csv
from pathlib import Path
from item_report import DATA_PATH, parse_record, totals_by

OUTPUT_DIR = Path(__file__).parent / "output"
SALES_COLUMNS = "order_id order_date customer_name item_name quantity amount payment status".split()
SUMMARY_COLUMNS = ["item_name", "orders", "total_amount"]


def main():
    with open(DATA_PATH, encoding="utf-8") as file:
        lines = file.read().splitlines()

    records = []
    for line in lines:
        record = parse_record(line)
        if record["status"] != "cancelled":
            records.append(record)

    totals, counts = totals_by(records, "item_name")
    OUTPUT_DIR.mkdir(exist_ok=True)

    clean_path = OUTPUT_DIR / "sales_week2_clean.csv"
    with open(clean_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=SALES_COLUMNS)
        writer.writeheader()
        writer.writerows(records)

    print(
        f"লেখা হলো: week-04/output/sales_week2_clean.csv  "
        f"({len(records)}টা সারি + হেডার)"
    )

    summary_path = OUTPUT_DIR / "item_summary.csv"
    with open(summary_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=SUMMARY_COLUMNS)
        writer.writeheader()
        for name in sorted(totals):
            row = {
                "item_name": name,
                "orders": counts[name],
                "total_amount": totals[name],
            }
            writer.writerow(row)

    print(
        f"লেখা হলো: week-04/output/item_summary.csv       "
        f"({len(totals)}টা সারি + হেডার)"
    )

    back = []
    with open(clean_path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["quantity"] = int(row["quantity"])
            row["amount"] = float(row["amount"])
            back.append(row)

    total = 0.0
    for record in back:
        total += record["amount"]
    print()
    print(f"CSV থেকে ফেরত পড়লাম: {len(back)}টা record")
    print(f"সব মিলিয়ে: ৳{total:.2f}")


if __name__ == "__main__":
    main()
