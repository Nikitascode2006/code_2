def decrypt_cypher_text(encrypted_text, key):
#     # function implementation here...
    decrypted_text = ""
    
    # Iterate over each character in the input text
    for char in encrypted_text:
        # Step 1: Convert character to ASCII code
        ascii_code = ord(char)
        
        # Step 2: Subtract the key from the ASCII code
        new_ascii_code = ascii_code - key
        
        # Step 3: Find the remainder when dividing by 256
        remainder_ascii_code = new_ascii_code % 256
        
        # Step 4: Convert back to character
        decrypted_char = chr(remainder_ascii_code)
        
        # Append the decrypted character to the result string
        decrypted_text += decrypted_char
    
    return decrypted_text
print(decrypt_cypher_text("Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$",3))