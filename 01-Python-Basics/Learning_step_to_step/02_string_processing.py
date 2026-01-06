raw_string = " pyThon-is-AWESOME "
new_raw_string = raw_string.strip().lower()
cleaned_string = new_raw_string.replace("-" , " ")

print(f"Original: '{raw_string}'")
print(f"Cleaned: '{cleaned_string}'")
print(f"Character Count: {len(cleaned_string)}")