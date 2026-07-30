import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 200
}

portfolio = []
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    print("\nAvailable Stocks:", ", ".join(stock_prices.keys()))

    stock = input("Enter Stock Name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid Stock Name!")
        continue

    quantity = int(input("Enter Quantity: "))

    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    portfolio.append([stock, quantity, price, investment])

print("\n------ Portfolio Summary ------")

for item in portfolio:
    print(f"Stock: {item[0]}, Quantity: {item[1]}, Price: ₹{item[2]}, Investment: ₹{item[3]}")

print(f"\nTotal Investment: ₹{total_investment}")

save = input("\nDo you want to save the result to CSV? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Stock Name", "Quantity", "Price", "Investment"])

        for item in portfolio:
            writer.writerow(item)

        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total_investment])

    print("Portfolio saved successfully as 'portfolio.csv'")
else:
    print("File not saved.")