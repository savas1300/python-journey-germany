alphabet = "abcdefghijklmnopqrstuvwxyz"
letter = "a"
shift = 3

index = alphabet.find(letter)
new_index = index + shift
ciphered_letter = alphabet[new_index]

print(f"Original letter: {letter}")
print(f"Ciphered letter: {ciphered_letter}")