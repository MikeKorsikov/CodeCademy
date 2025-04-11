# project

# Import necessary libraries
import random
import logging
from datetime import datetime

# Configure logging
def configure_logging():
    """Configure logging settings for the ATM application"""
    logger = logging.getLogger('ATM_Logger')
    
    # Set log level (DEBUG for development, could be INFO for production)
    logger.setLevel(logging.DEBUG)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    
    # File handler
    file_handler = logging.FileHandler('atm_transactions.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    
    # Add handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

# Initialize logger
logger = configure_logging()

class BankAccount:
    """A class representing a bank account with deposit, withdrawal, and balance checking functionality"""
    
    def __init__(self):
        """Initialize the bank account with a default balance"""
        self.balance = 100
        logger.info("Hello! Welcome to the ATM Depot!")
        logger.debug("BankAccount initialized with default balance of $100")
    
    def authenticate(self):
        """Authenticate user with PIN verification"""
        while True:
            try:
                pin = int(input("Enter account pin: "))
                if pin != 1234:
                    logger.warning("Invalid PIN entered")
                    print("Error! Invalid pin. Try again.")
                else:
                    logger.debug("User authenticated successfully")
                    return True
            except ValueError:
                logger.error("Non-numeric value entered for PIN")
                print("Error! Please enter a numeric PIN.")
    
    def log_transaction(self, transaction_type, amount, status, message=""):
        """Helper method to log transaction details consistently"""
        transaction_id = random.randint(10000, 1000000)
        log_message = (f"{transaction_type} - Amount: ${amount:.2f} - "
                      f"Status: {status} - Transaction ID: {transaction_id}")
        
        if message:
            log_message += f" - Note: {message}"
        
        if status == "Successful":
            logger.info(log_message)
        else:
            logger.error(log_message)
        
        logger.debug(f"Current balance after transaction: ${self.balance:.2f}")
    
    def deposit(self):
        """Handle deposit transactions"""
        try:
            amount = float(input("Enter amount to be deposited: "))
            if amount < 0:
                self.log_transaction("Deposit", amount, "Failed", "Negative amount entered")
                print("Warning! You entered a negative number to deposit.")
                return
            
            self.balance += amount
            self.log_transaction("Deposit", amount, "Successful")
            print(f"Amount Deposited: ${amount:.2f}")
            
        except ValueError:
            self.log_transaction("Deposit", 0, "Failed", "Non-number value entered")
            print("Error! You entered a non-number value to deposit.")
    
    def withdraw(self):
        """Handle withdrawal transactions"""
        try:
            amount = float(input("Enter amount to be withdrawn: "))
            
            if amount < 0:
                self.log_transaction("Withdrawal", amount, "Failed", "Negative amount entered")
                print("Warning! You entered a negative number to withdraw.")
                return
            
            if self.balance >= amount:
                self.balance -= amount
                self.log_transaction("Withdrawal", amount, "Successful")
                print(f"You withdrew: ${amount:.2f}")
            else:
                self.log_transaction("Withdrawal", amount, "Failed", "Insufficient funds")
                print("Error! Insufficient balance to complete withdraw.")
                
        except ValueError:
            self.log_transaction("Withdrawal", 0, "Failed", "Non-number value entered")
            print("Error! You entered a non-number value to withdraw.")
    
    def display_balance(self):
        """Display current account balance"""
        logger.info(f"Balance checked - Current balance: ${self.balance:.2f}")
        print(f"Available Balance = ${self.balance:.2f}")

# Main program execution
if __name__ == "__main__":
    try:
        account = BankAccount()
        if account.authenticate():
            account.deposit()
            account.withdraw()
            account.display_balance()
    except KeyboardInterrupt:
        logger.warning("Program terminated by user")
        print("\nProgram terminated by user")
    except Exception as e:
        logger.critical(f"Unexpected error: {str(e)}")
        print("An unexpected error occurred. Please contact support.")