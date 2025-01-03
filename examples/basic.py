# Imports.
import avro


# Please follow the detailed guidelines given in the README.md file about each function to learn more.
def main() -> None:
    dummy_text = "amar sOnar bangla"  # Dummy text.
    print("Original English Text:", dummy_text)

    parsed_text = avro.parse(dummy_text)  # Parse the text to Bengali.
    print("Parsed Unicode Output:", parsed_text)

    # We can parse it directly to Bijoy, or use the to_bijoy function to convert it.
    # Both should return the same result.
    bijoy_text_direct = avro.parse(dummy_text, bijoy=True)
    bijoy_text_function = avro.to_bijoy(parsed_text)

    if bijoy_text_direct == bijoy_text_function:
        print(f"Bijoy Output: {bijoy_text_direct}")

    # Now, we can return the Bijoy text to Unicode since we'd like the original output (assuming).
    # This should be the same as the old parsed_text variable.
    unicode_text = avro.to_unicode(bijoy_text_direct)
    print("Reversed Unicode Output:", unicode_text)

    # Finally, we can reverse the Bengali text, back to English!
    reversed = avro.reverse(unicode_text)
    print("Reversed English Output:", reversed)


if __name__ == "__main__":
    main()
