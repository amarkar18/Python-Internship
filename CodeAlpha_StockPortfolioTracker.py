import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol} to your portfolio.")

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if shares >= self.portfolio[symbol]:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol} from your portfolio.")
            else:
                self.portfolio[symbol] -= shares
                print(f"Removed {shares} shares of {symbol} from your portfolio.")
        else:
            print(f"Stock {symbol} is not in your portfolio.")

    def view_portfolio(self):
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        print("\nYour Portfolio:")
        for symbol, shares in self.portfolio.items():
            print(f"{symbol}: {shares} shares")

    def get_stock_price(self, symbol):
        try:
            stock = yf.Ticker(symbol)
            price = stock.history(period="1d").iloc[-1]["Close"]
            return price
        except Exception as e:
            print(f"Error fetching price for {symbol}: {e}")
            return None

    def track_performance(self):
        if not self.portfolio:
            print("Your portfolio is empty. Add stocks to track performance.")
            return

        print("\nPortfolio Performance:")
        total_value = 0
        for symbol, shares in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price is not None:
                value = price * shares
                total_value += value
                print(f"{symbol}: {shares} shares x ${price:.2f} = ${value:.2f}")

        print(f"\nTotal Portfolio Value: ${total_value:.2f}")

if __name__ == "__main__":
    portfolio = StockPortfolio()

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Track Performance")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)
        elif choice == "2":
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(symbol, shares)
        elif choice == "3":
            portfolio.view_portfolio()
        elif choice == "4":
            portfolio.track_performance()
        elif choice == "5":
            print("Exiting Stock Portfolio Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
