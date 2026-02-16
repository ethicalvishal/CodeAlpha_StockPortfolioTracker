stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130
}

total_investment = 0

print("📈 Stock Portfolio Tracker")

while True:
    stock_name = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock_name == "DONE":
        break
    
    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))
        investment = stocks[stock_name] * quantity
        total_investment += investment
        print(f"Added {stock_name}, Investment: ${investment}")
    else:
        print("⚠ Stock not found!")

print("\n💰 Total Investment Value: $", total_investment)

# Optional file save
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment: ${total_investment}")

print("📁 Data saved to portfolio.txt")
