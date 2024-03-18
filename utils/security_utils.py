# Unique ID: a5eef76c-26af-4028-98cc-a5838b1a66af
import hashlib

def hash_data(data: str, algorithm: str = 'sha256') -> str:
    """
    Hashes input data using the specified algorithm.

    Parameters:
    - data: The input data to hash.
    - algorithm: The hashing algorithm to use. Default is 'sha256'.

    Returns:
    - The hashed data as a hexadecimal string.
    """
    try:
        # Initialize the hash object with the specified algorithm
        hash_object = hashlib.new(algorithm)

        # Update the hash object with the input data
        hash_object.update(data.encode('utf-8'))

        # Get the hexadecimal representation of the hashed data
        hashed_data = hash_object.hexdigest()

        return hashed_data

    except Exception as e:
        print(f"Error occurred during data hashing: {e}")
        raise

    
