import decimal
from decimal import Decimal, getcontext

# Set the precision high enough to handle large values of n
getcontext().prec = 200

# Define n
n = 100000
n_decimal = Decimal(n)

# Calculate the approximations
approx_e = ((n_decimal + Decimal(1)) / n_decimal) ** n_decimal
approx_1_over_e = ((n_decimal - Decimal(1)) / n_decimal) ** n_decimal
reciprocal_of_1_over_e = Decimal(1) / approx_1_over_e

# Calculate the difference
difference = approx_e - reciprocal_of_1_over_e

# Calculate the absolute value of the difference
absolute_difference = abs(difference)

# Convert to string and remove the leading '0.'
absolute_difference_str = str(absolute_difference).lstrip('0.')

# Place the first non-zero digit in the ones column
final_result_str = '2.' + absolute_difference_str[1:]

# Print the results
print("approx_e:", approx_e)
print("reciprocal_of_1_over_e:", reciprocal_of_1_over_e)
print("difference:", difference)
print("absolute difference without leading zeros, first digit in the ones column:", final_result_str)
