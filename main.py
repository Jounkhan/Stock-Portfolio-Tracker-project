class StockPortfolio:
    def __init__(self, name):
        self.name = name
        self.stock_prices= {"AAPL": 180, "TSLA": 250, "PCAL": 145, "FFC" :535, "LUCK" :416, "UBL" : 414, "OGDC" : 315}

        self.user_portfolio = {}


    def display_available_stocks(self):
        for stock , price in self.stock_prices.items():
            print(f"Today, The price {stock} stock in pakistan is RS:{price}")


    def add_stock(self, symbol, quantity):
        clean_symbol = symbol.upper()
        if clean_symbol in self.stock_prices:
            if clean_symbol in self.user_portfolio:
                self.user_portfolio[clean_symbol] += quantity
            else:
                self.user_portfolio[clean_symbol] = quantity
        else:
            print("This stock is not in List")


    def calculate_total(self):
        total_value = 0
        for symbol , quantity in self.user_portfolio.items():
            price_of_stock = self.stock_prices[symbol]
            total_value += quantity*price_of_stock
        print(total_value)


    def save_to_file(self):
        clean_name = self.name.lower().strip()
        filename = f"{clean_name}_stocks_details.txt"
        with open(f"{filename}", "w") as file:
            file.write(f"-- {self.name.upper().strip()} STOCK PORTFOLIO --\n")
            grand_total = 0
            for symbol, quantity in self.user_portfolio.items():
                price = self.stock_prices[symbol]
                item_total = price * quantity
                grand_total += item_total
                file.write(f"Stock: {symbol} | Qty: {quantity} | Price: RS:{price} | Total: RS:{item_total}\n")
            text = str(grand_total)
            file.write("----------------------------\n")
            file.write(f"Total investment value : RS:{text}\n")


joun = StockPortfolio("Joun")
joun.add_stock("AAPL", 2)
joun.save_to_file()


ali = StockPortfolio("Ali")
ali.add_stock("OGDC", 5)
ali.save_to_file()