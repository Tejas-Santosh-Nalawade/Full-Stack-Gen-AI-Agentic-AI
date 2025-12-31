chai_type = "ginger chai"

customer_name = "Priya"

print(f"{customer_name} ordered {chai_type}")


chai_description = "Aromatic and Bold"

print(f"{customer_name} ordered {chai_type} which is {chai_description[:8]}")

print(f"last character {chai_description[12:]}")

print(f"reverse {chai_description[::-1]}")

label_text = "Chai"
encode = label_text.encode("utf-8")
print(encode)

decode = encode.decode("utf-8")
print(decode)

