# Tuple () immutable

masala_spices = ("cardamom", "cumin", "coriander", "cloves", "curry")

(spice1, spice2, spice3, spice4, spice5) = masala_spices

print(f"Main masala spice is {spice1}, {spice2}, {spice3}, {spice4}, {spice5}")



ginger_ratio, cardamom_ratio = 2,1

print(f"Ratio of ginger to cardamom is {ginger_ratio}:{cardamom_ratio}")

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio

print(f"Ratio of ginger to cardamom is {ginger_ratio}:{cardamom_ratio}")


# membership testing

print(f"Is ginger in masala spices? {'ginger' in masala_spices}")

print(f"Is ginger in masala spices? {'ginger' not in masala_spices}")
