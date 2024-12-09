# Imports.
import asyncio

import avro


# Please follow the detailed guidelines given in the README.md file about each function to learn more.
async def main() -> None:
    dummy_text = "amar sOnar bangla"  # Dummy text.
    print("Original English Text:", dummy_text)

    parsed_text = await avro.parse_async(
        dummy_text
    )  # Parse the text to Bengali.
    print("Parsed Unicode Output:", parsed_text)

    # We can parse it directly to Bijoy, or use the to_bijoy function to convert it.
    # Both should return the same result.
    bijoy_text_direct = await avro.parse_async(dummy_text, bijoy=True)
    bijoy_text_function = await avro.to_bijoy_async(parsed_text)

    if bijoy_text_direct == bijoy_text_function:
        print(f"Bijoy Output: {bijoy_text_direct}")

    # Now, we can return the Bijoy text to Unicode since we'd like the original output (assuming).
    # This should be the same as the old parsed_text variable.
    unicode_text = await avro.to_unicode_async(bijoy_text_direct)
    print("Reversed Unicode Output:", unicode_text)

    # Finally, we can reverse the Bengali text, back to English!
    reversed = await avro.reverse_async(unicode_text)
    print("Reversed English Output:", reversed)


if __name__ == "__main__":
    asyncio.run(main())
