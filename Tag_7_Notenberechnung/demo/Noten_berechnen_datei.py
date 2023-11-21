
import pickle
import os

def save_subjects(fächer, filename):
    """
    Save the subjects to a file using pickle serialization.

    Args:
        fächer (list): The list of subjects to be saved.
        filename (str): The name of the file to save the subjects to.

    Returns:
        None
    """
    with open(filename, "wb") as file:
        pickle.dump(fächer, file)

def load_subjects(filename):
    """
    Load subjects from a file.

    Args:
        filename (str): The name of the file to load subjects from.

    Returns:
        list or None: A list of subjects if the file exists, None otherwise.
    """
    if os.path.exists(filename):
        with open(filename, "rb") as file:
            fächer = pickle.load(file)
        return fächer
    else:
        return None
