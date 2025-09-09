import csv
from datetime import datetime

class StockPortfolioTracker:
    def __init__(self):
        self.stock_prices = {
            "AAPL": 180.00,
            "TSLA": 250.00,
            "GOOGL": 2800.00,
            "MSFT": 420.00,
            "AMZN": 3400.00,
            "NVDA": 900.00,
            "META": 350.00,
            "NFLX": 450.00,
            "AMD": 120.00,
            "INTC": 45.00
        }
        self.portfolio = {}
        self.total_value = 0.0

    def display_available_stocks(self):
        print("\n📈 Available Stocks:")
        print("-" * 30)
        for stock, price in self.stock_prices.items():
            print(f"{stock}: ${price:.2f}")
        print("-" * 30)

    def add_stock_to_portfolio(self):
        while True:
            stock_symbol = input("\nEnter stock symbol (or 'done' to finish): ").upper()
            
            if stock_symbol == 'DONE':
                break
            
            if stock_symbol not in self.stock_prices:
                print(f"❌ Stock '{stock_symbol}' not found in our database.")
                continue
            
            try:
                quantity = int(input(f"Enter quantity of {stock_symbol} shares: "))
                if quantity <= 0:
                    print("❌ Quantity must be a positive number.")
                    continue
                
                if stock_symbol in self.portfolio:
                    self.portfolio[stock_symbol] += quantity
                    print(f"✅ Updated {stock_symbol}. Total shares: {self.portfolio[stock_symbol]}")
                else:
                    self.portfolio[stock_symbol] = quantity
                    print(f"✅ Added {quantity} shares of {stock_symbol} to portfolio.")
                    
            except ValueError:
                print("❌ Please enter a valid number for quantity.")

    def calculate_portfolio_value(self):
        self.total_value = 0.0
        portfolio_details = []
        
        print("\n📊 Portfolio Summary:")
        print("-" * 60)
        print(f"{'Stock':<8} {'Shares':<8} {'Price':<10} {'Total Value':<12}")
        print("-" * 60)
        
        for stock, quantity in self.portfolio.items():
            price = self.stock_prices[stock]
            stock_value = quantity * price
            self.total_value += stock_value
            
            print(f"{stock:<8} {quantity:<8} ${price:<9.2f} ${stock_value:<11.2f}")
            
            portfolio_details.append({
                'stock': stock,
                'shares': quantity,
                'price': price,
                'total_value': stock_value
            })
        
        print("-" * 60)
        print(f"{'TOTAL PORTFOLIO VALUE:':<38} ${self.total_value:.2f}")
        print("-" * 60)
        
        return portfolio_details

    def save_to_txt(self, portfolio_details):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"portfolio_summary_{timestamp}.txt"
        
        try:
            with open(filename, 'w') as file:
                file.write("STOCK PORTFOLIO SUMMARY\n")
                file.write("=" * 50 + "\n")
                file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                file.write(f"{'Stock':<8} {'Shares':<8} {'Price':<10} {'Total Value':<12}\n")
                file.write("-" * 50 + "\n")
                
                for detail in portfolio_details:
                    file.write(f"{detail['stock']:<8} {detail['shares']:<8} "
                             f"${detail['price']:<9.2f} ${detail['total_value']:<11.2f}\n")
                
                file.write("-" * 50 + "\n")
                file.write(f"TOTAL PORTFOLIO VALUE: ${self.total_value:.2f}\n")
            
            print(f"✅ Portfolio saved to {filename}")
            
        except Exception as e:
            print(f"❌ Error saving to text file: {e}")

    def save_to_csv(self, portfolio_details):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"portfolio_summary_{timestamp}.csv"
        
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                
                writer.writerow(['Stock Symbol', 'Shares', 'Price per Share', 'Total Value'])
                
                for detail in portfolio_details:
                    writer.writerow([detail['stock'], detail['shares'], 
                                   detail['price'], detail['total_value']])
                
                writer.writerow([])
                writer.writerow(['TOTAL PORTFOLIO VALUE', '', '', self.total_value])
            
            print(f"✅ Portfolio saved to {filename}")
            
        except Exception as e:
            print(f"❌ Error saving to CSV file: {e}")

    def run(self):
        print("🚀 Welcome to Stock Portfolio Tracker!")
        print("=" * 40)
        
        while True:
            print("\nWhat would you like to do?")
            print("1. View available stocks")
            print("2. Add stocks to portfolio")
            print("3. Calculate portfolio value")
            print("4. Save portfolio to file")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                self.display_available_stocks()
            
            elif choice == '2':
                if not self.portfolio:
                    self.display_available_stocks()
                self.add_stock_to_portfolio()
            
            elif choice == '3':
                if not self.portfolio:
                    print("❌ No stocks in portfolio. Please add some stocks first.")
                else:
                    portfolio_details = self.calculate_portfolio_value()
            
            elif choice == '4':
                if not self.portfolio:
                    print("❌ No stocks in portfolio. Please add some stocks first.")
                else:
                    portfolio_details = self.calculate_portfolio_value()
                    
                    save_choice = input("\nSave as (1) TXT or (2) CSV? Enter 1 or 2: ").strip()
                    
                    if save_choice == '1':
                        self.save_to_txt(portfolio_details)
                    elif save_choice == '2':
                        self.save_to_csv(portfolio_details)
                    else:
                        print("❌ Invalid choice. Please enter 1 or 2.")
            
            elif choice == '5':
                print("👋 Thank you for using Stock Portfolio Tracker!")
                break
            
            else:
                print("❌ Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    tracker = StockPortfolioTracker()
    tracker.run()
