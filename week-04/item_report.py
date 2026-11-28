from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "raw_sales_week2.txt"


def parse_record(raw):
    parts = raw.split(";")
    amount = parts[5].strip().replace("৳", "").replace(",", "")
    return {
        "order_id": parts[0].strip().upper(),
        "order_date": parts[1].strip(),
        "customer_name": " ".join(parts[2].strip().title().split()),
        "item_name": parts[3].strip(),
        "quantity": int(parts[4].strip()),
        "amount": float(amount),
        "payment": parts[6].strip().lower(),
        "status": parts[7].strip().lower(),
    }


def totals_by(records, key):
    totals = {}
    counts = {}
    for rec in records:
        name = rec[key]
        totals[name] = totals.get(name, 0.0) + rec["amount"]
        counts[name] = counts.get(name, 0) + 1
    return totals, counts


def main():
    lines = DATA_PATH.read_text(encoding="utf-8").splitlines()
    records = []
    cancelled = 0

    for raw in lines:
        rec = parse_record(raw)
        if rec["status"] == "cancelled":
            cancelled += 1
            continue
        records.append(rec)

    totals, counts = totals_by(records, "item_name")

    print(f"মোট লাইন: {len(lines)}টা  ·  বাতিল: {cancelled}টা  ·  হিসাবে: {len(records)}টা")
    print()
    print("পণ্য ধরে হিসাব")
    for name in sorted(totals):
        print(f"   {name:<20} {counts[name]}টা   ৳{totals[name]:.2f}")

    grand_total = sum(totals.values())
    print(f"   {'সব মিলিয়ে':<20} {len(records)}টা   ৳{grand_total:.2f}")
    print()

    top_item = max(totals, key=totals.__getitem__)
    print(
        f"সবচেয়ে বেশি বিক্রি: {top_item} — ৳{totals[top_item]:.2f} "
        f"({counts[top_item]}টা অর্ডার)"
    )


if __name__ == "__main__":
    main()