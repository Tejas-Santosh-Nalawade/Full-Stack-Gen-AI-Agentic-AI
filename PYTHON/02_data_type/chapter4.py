is_boiling = True
stri_count = 10

total_actions = is_boiling + stri_count # True = 1 False = 0 upcasting boolean to integer
print(f"Total actions {total_actions}")


# Logical operaiton and or not

is_boiling = True
stri_count = 10

is_boiling and stri_count > 5
print(f"Is boiling and stri count greater than 5 {is_boiling and stri_count > 5}")

is_boiling or stri_count > 5
print(f"Is boiling or stri count greater than 5 {is_boiling or stri_count > 5}")

not is_boiling
print(f"Not is boiling {not is_boiling}")


