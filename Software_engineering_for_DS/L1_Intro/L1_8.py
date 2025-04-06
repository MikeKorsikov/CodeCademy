# project

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}"
    
    def calculate_bill(self, purchased_items):
        """Calculate total bill for purchased items"""
        total = 0
        for item in purchased_items:
            if item in self.items:
                total += self.items[item]
        return total


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    def __repr__(self):
        return f"Franchise located at {self.address}"
    
    def available_menus(self, time):
        """Return menus available at the given time"""
        available = []
        for menu in self.menus:
            current_time = self.convert_time(time)
            start_time = self.convert_time(menu.start_time)
            end_time = self.convert_time(menu.end_time)
            
            if start_time <= current_time <= end_time:
                available.append(menu)
        return available
    
    def convert_time(self, time_str):
        """Convert time string to 24-hour format for comparison"""
        if 'am' in time_str:
            hour = int(time_str.replace('am', ''))
            if hour == 12:  # 12am is 0 in 24-hour
                return 0
            return hour
        elif 'pm' in time_str:
            hour = int(time_str.replace('pm', ''))
            if hour != 12:  # 12pm stays 12
                hour += 12
            return hour
        return 0  # default if format is wrong


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# ========== Menu Creation ==========
# Brunch Menu (11am-4pm)
brunch = Menu("Brunch", {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 
    'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, "11am", "4pm")

# Early Bird Menu (3pm-6pm)
early_bird = Menu("Early Bird", {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 
    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 
    'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
}, "3pm", "6pm")

# Dinner Menu (5pm-11pm)
dinner = Menu("Dinner", {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 
    'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 
    'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
}, "5pm", "11pm")

# Kids Menu (11am-9pm)
kids = Menu("Kids", {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 
    'apple juice': 3.00
}, "11am", "9pm")

# ========== Franchise Creation ==========
all_menus = [brunch, early_bird, dinner, kids]

# Original Basta Fazoolin' locations
flagship_store = Franchise("1232 West End Road", all_menus)
new_installment = Franchise("12 East Mulberry Street", all_menus)

# ========== Business Creation ==========
basta_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Arepa Business Components
arepas_menu = Menu("Take a' Arepa", {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 
    'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, "10am", "8pm")

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
arepa_business = Business("Take a' Arepa", [arepas_place])

# ========== Demonstration ==========
if __name__ == "__main__":
    print("=== Menu Demonstration ===")
    print(brunch)
    print(f"Brunch order total: ${brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])}")
    print(f"Early bird order total: ${early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])}")
    
    print("\n=== Franchise Demonstration ===")
    print(flagship_store)
    print("Menus available at 12pm:", flagship_store.available_menus("12pm"))
    print("Menus available at 5pm:", flagship_store.available_menus("5pm"))
    
    print("\n=== Business Demonstration ===")
    print(f"Business: {basta_business.name} with {len(basta_business.franchises)} locations")
    print(f"Business: {arepa_business.name} with {len(arepa_business.franchises)} location")