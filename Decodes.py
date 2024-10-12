def caesar_cipher(text, shift):
  """Encodes or decodes a text using the Caesar cipher.

  Args:
    text: The text to be encoded or decoded.
    shift: The number of positions to shift the letters.

  Returns:
    The encoded or decoded text.
  """

  result = ""
  for char in text:
    if char.isalpha():
      # Determine the new letter based on the shift
      new_char = ord(char) + shift
      if char.isupper():
        # Ensure the new character remains uppercase
        if new_char > ord('Z'):
          new_char -= 26
        elif new_char < ord('A'):
          new_char += 26
      else:
        # Ensure the new character remains lowercase
        if new_char > ord('z'):
          new_char -= 26
        elif new_char < ord('a'):
          new_char += 26
      result += chr(new_char)
    else:
      result += char
  return result

# Get user input
mode = input("Type encode to encrypt, type decode to decrypt: ")
text = input("Type your message: ")
shift = int(input("Type the shift number: "))

# Perform the encoding or decoding
if mode == "encode":
  result = caesar_cipher(text, shift)
  print("Here is the encoded result:", result)
elif mode == "decode":
  result = caesar_cipher(text, -shift)
  print("Here is the decoded result:", result)
else:
  print("Invalid mode. Please enter 'encode' or 'decode'.")