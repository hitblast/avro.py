# Import the package.
import avro

# Let's assume we'd like to convert "amar sOnar bangla" to Unicode.
dummy_text = "amar sOnar bangla"
print("Original English Text:", dummy_text)

# Parse the text to Avro.
parsed_text = avro.parse(dummy_text)
print("Parsed Unicode Output:", parsed_text)

# We can parse it directly to Bijoy, or use the to_bijoy function to convert it.
# Both should return the same result.
bijoy_text_direct = avro.parse(dummy_text, bijoy=True)
bijoy_text_function = avro.to_bijoy(parsed_text)

# Print the Bijoy text.
if bijoy_text_direct == bijoy_text_function:
    print(f"Bijoy Output: {bijoy_text_direct}")

# Now, we can return the Bijoy text to Unicode since we'd like the original output (assuming).
# This should be the same as the old parsed_text variable.
unicode_text = avro.to_unicode(bijoy_text_direct)
print("Reversed Unicode Output:", unicode_text)

# Finally, we can reverse the Bengali text, back to English!
reversed = avro.reverse(unicode_text)
print("Reversed English Output:", reversed)
