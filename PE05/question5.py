def make_shirt(size="Large", message="I love Python"):
    """Print a sentence describing the shirt."""
    print(f"The shirt size is {size} and the message is '{message}'.")


# Make a large shirt using the default values.
make_shirt()

# Make a medium shirt with the default message.
make_shirt(size="Medium")

# Make a shirt of any size with a different message.
make_shirt(size="Small", message="Python is awesome")