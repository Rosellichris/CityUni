def make_shirt(size, message):
    """Print a sentence describing the shirt."""
    print(f"The shirt size is {size} and the message is '{message}'.")


# Call the function using positional arguments.
make_shirt("Large", "I love Python")

# Call the function using keyword arguments.
make_shirt(size="Medium", message="Python is fun")