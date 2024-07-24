from decimal import Decimal, getcontext
import time
from mpmath import mp, mpf

# Customizable parameters
X_VALUES = [10, 100, 1000]  # Add or modify exponents here (n will be 10^x)
PRECISION = 5000  # Set your desired precision here

# Set precision for Decimal and mpmath calculations
getcontext().prec = PRECISION
mp.dps = PRECISION

def calculate_approximations(x):
    n = Decimal(10) ** x
    
    # Original method
    e_approx1 = (Decimal(1) + Decimal(1)/n) ** n
    e_approx2 = Decimal(1) / ((Decimal(1) - Decimal(1)/n) ** n)
    original_result = (e_approx2 - e_approx1) * n
    
    # New method
    term1 = ((n + Decimal(2)) / n) ** n
    new_approx1 = term1.sqrt()
    term2 = ((n - Decimal(2)) / n) ** n
    new_approx2 = Decimal(1) / term2.sqrt()
    new_result = (new_approx1 + new_approx2) / 2
    
    return original_result, new_result

def calculate_refined_difference(x):
    original_result, new_result = calculate_approximations(x)
    
    # Calculate the difference
    difference = new_result - original_result
    
    # Multiply by 24 and divide by 23
    refined_difference = (difference * Decimal('24')) / Decimal('23')
    
    return original_result, new_result, difference, refined_difference

def format_estimation(value):
    value_str = f"{value:.{PRECISION}f}"
    return value_str.rstrip('0').rstrip('.')

def count_accurate_decimals(approximation, true_value):
    approx_str = str(approximation)
    true_str = str(true_value)
    
    count = 0
    for a, t in zip(approx_str, true_str):
        if a == t:
            count += 1
        else:
            break
    return max(0, count - 2)  # Subtract 2 to exclude "2." and ensure non-negative result

if __name__ == '__main__':
    print("Starting e Approximation with Refined Difference Calculation")
    
    # Calculate true e value using mpmath
    true_e = mpf(mp.e)
    
    print(f"Processing {len(X_VALUES)} X_VALUES: {X_VALUES}")
    overall_start_time = time.time()

    results = []
    for x in X_VALUES:
        start_time = time.time()
        original, new, diff, refined_diff = calculate_refined_difference(x)
        end_time = time.time()
        results.append((x, original, new, diff, refined_diff, end_time - start_time))

    overall_end_time = time.time()
    print(f"All calculations completed in {overall_end_time - overall_start_time:.2f} seconds")

    for x, original, new, diff, refined_diff, calc_time in results:
        print(f"\nResults for x = {x} (n = 10^{x}):")
        
        print("Original Method:")
        original_estimation = format_estimation(Decimal('2') + original)
        original_accurate = count_accurate_decimals(original_estimation, true_e)
        print(f"  Estimated e value: {original_estimation}")
        print(f"  Accurate decimal places: {original_accurate}")
        
        print("\nNew Method:")
        new_estimation = format_estimation(new)
        new_accurate = count_accurate_decimals(new_estimation, true_e)
        print(f"  Estimated e value: {new_estimation}")
        print(f"  Accurate decimal places: {new_accurate}")
        
        print("\nDifference (New - Original):")
        print(f"  {format_estimation(diff)}")
        
        print("\nRefined Difference ((New - Original) * 24/23):")
        print(f"  {format_estimation(refined_diff)}")
        
        print(f"\nCalculation time: {calc_time:.2f} seconds")

    print("\nProgram completed successfully")
