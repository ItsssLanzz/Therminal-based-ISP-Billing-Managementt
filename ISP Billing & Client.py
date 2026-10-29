customers = []
payments = []

def find_customer(customer_id):
    for customer in customers:
        if customer["id"] == customer_id:
            return customer
    return None

def add_customer():
    name = input("Customer name: ").strip()
    phone = input("Phone number: ").strip()
    address = input("Address: ").strip()
    package = input("Package: ").strip()
    status = input("Status (Active): ").strip() or "Active"

    payment = float(input("Payment: ").strip() or "0")
    initial_balance = float(input("Balance: ").strip() or "0")
    
    customer = {
        "id": len(customers) + 1,
        "name": name,
        "phone": phone,
        "address": address,
        "package": package,
        "status": status,
        "payment": payment,   # total paid so far
        "balance": initial_balance   # remaining balance
    }

    customers.append(customer)

    if payment > 0:
        method = input("Payment method: ").strip()
        date = input("Date (MM-DD-YYYY): ").strip()

        payments.append({
            "customer_id": customer["id"],
            "amount": payment,
            "method": method,
            "date": date
        })

    print("Customer added.")

def add_payment():
    if not customers:
        print("No customers yet.")
        return

    print("Customers:")
    for c in customers:
        print(f"{c['id']}. {c['name']}")

    customer_id = int(input("Choose customer ID: "))
    customer = find_customer(customer_id)

    if customer is None:
        print("Invalid customer ID.")
        return

    amount = float(input("Amount: "))
    method = input("Payment method: ").strip()
    date = input("Date (MM-DD-YYYY): ").strip()

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    # subtract payment from customer's remaining balance
    customer["balance"] -= amount
    customer["payment"] += amount

    payments.append({
        "customer_id": customer_id,
        "amount": amount,
        "method": method,
        "date": date
    })

    print("Payment added.")

def show_customers():
    if not customers:
        print("No customers.")
        return

    print("\nCustomers:")
    for c in customers:
        print(
            f"{c['id']} | {c['name']} | {c['phone']} | {c['address']} | "
            f"{c['package']} | payment: {c['payment']} | balance: {c['balance']} | {c['status']}"
        )

def show_payments():
    if not payments:
        print("No payments.")
        return

    print("\nPayments:")
    for p in payments:
        customer = find_customer(p["customer_id"])
        customer_name = customer["name"] if customer else "Unknown"
        customer_phone = customer["phone"] if customer else "Unknown"

        print(
            f"Customer: {customer_name} | "
            f"Phone No.: {customer_phone} | "
            f"Payment Method: {p['method']} | "
            f"Amount: {p['amount']}"
        )

def summary():
    total_customers = len(customers)
    total_collected = sum(p["amount"] for p in payments)

    print("\nSummary")
    print(f"Total customers: {total_customers}")
    print(f"Total collected: {total_collected}")

#ISP= INTERNET SERVICE PROVIDER MWEHEHE
while True:
    print("\n===| ISP DASHBOARD |===")
    print("1. Add Customer")
    print("2. Add Payment")
    print("3. Show Customers")
    print("4. Show Payments")
    print("5. Summary")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_customer()
    elif choice == "2":
        add_payment()
    elif choice == "3":
        show_customers()
    elif choice == "4":
        show_payments()
    elif choice == "5":
        summary()
    elif choice == "0":
        print("Bye!")
        break
    else:
        print("Invalid option.")