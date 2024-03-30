# A function named calculate_discount(price, discount_percent) that calculates the 
# final price after applying a discount.
# The function should take the original price (price) and
# the discount percentage (discount_percent) as parameters.
# If the discount is 20% or higher, apply the discount; 
# otherwise, return the original price.

# My Function

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

# prompt the user to enter the original price of an item and the discount percentage.
# Print the final price after applying the discount,
# or if no discount was applied, print the original price.


def main():    # Starting point of python program

    original_price = float(input("Enter the original price of the item: $"))  # Prompt user input
    discount_percent = float(input("Enter the discount percentage: "))      # discount prompt
    
    final_price = calculate_discount(original_price, discount_percent)
    # start of conditional statement
    if final_price == original_price:
        print("No discount applied. Final price: ${:.2f}".format(final_price))
    else:
        print("Final price after discount: ${:.2f}".format(final_price))

# a conditional statement that tells the Python interpreter under
# what conditions the main method should be executed.
        
if __name__ == "__main__": 
     main()
