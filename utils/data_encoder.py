# Unique ID: 1338d897-c18c-40db-8731-845fc09c6b78
import base64

def encode_data(data: bytes) -> str:
    """
    Encodes binary data to a base64 string.

    Parameters:
    - data: The binary data to encode.

    Returns:
    - The base64-encoded string.
    """
    try:
        # Encode the binary data to base64
        encoded_data = base64.b64encode(data).decode('utf-8')

        return encoded_data

    except Exception as e:
        print(f"Error occurred during data encoding: {e}")
        raise

def decode_data(encoded_data: str) -> bytes:
    """
    Decodes a base64-encoded string to binary data.

    Parameters:
    - encoded_data: The base64-encoded string.

    Returns:
    - The decoded binary data.
    """
    try:
        # Decode the base64-encoded string to binary data
        decoded_data = base64.b64decode(encoded_data.encode('utf-8'))

        return decoded_data

    except Exception as e:
        print(f"Error occurred during data decoding: {e}")
        raise

    
