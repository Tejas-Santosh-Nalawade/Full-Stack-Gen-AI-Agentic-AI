import sys 
from fractions import Fraction
from decimal import Decimal

ideal_temp = Decimal(191) / Decimal(2)
current_temp = Decimal(191) / Decimal(2) - Decimal(1) / Decimal(1000000000)

print(f"Ideal temperature {ideal_temp}")
print(f"Current temperature {current_temp}")
print(f"Difference {ideal_temp - current_temp}")
print(f"Difference {ideal_temp - current_temp:.2f}")
print(sys.float_info)   