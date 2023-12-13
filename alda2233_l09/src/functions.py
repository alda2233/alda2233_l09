"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-12-09"
-------------------------------------------------------
"""
# Imports

# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
        chemical - a chemical formula (str)
    Returns:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """

    hydroxide = chemical.endswith('OH')

    return hydroxide


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """

    pc = product_code[:3]
    pi = product_code[3:7]
    pq = product_code[7:]

    return pc, pi, pq


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if three upper-case characters, False otherwise
        digits - True if four digits, False otherwise
        qualifiers - True if starts with 1 upper-case letter, False otherwise
    -------------------------------------------------------
    """

    category = len(product_code[:3]) == 3 and product_code[:3].isupper()

    digits = len(product_code[3:7]) == 4 and product_code[3:7].isdigit()

    qualifiers = product_code[7:].startswith(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                                              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                                              'U', 'V', 'W', 'X', 'Y', 'Z')) if len(product_code) > 7 else False

    return category, digits, qualifiers


def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """

    if len(password) < 8:
        print("not long enough")

    # Check if the password contains digits
    if not any(char.isdigit() for char in password):
        print("no digits")

    # Check if the password contains upper-case letters
    if not any(char.isupper() for char in password):
        print("no upper case")

    # Check if the password contains lower-case letters
    if not any(char.islower() for char in password):
        print("no lower case")

    return None


def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """

    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0

    for char in txt:
        if char.isupper() == True:
            uppr += 1
        if char.islower() == True:
            lowr += 1
        if char.isdigit() == True:
            dgts += 1
        if char.isspace() == True:
            whtspc += 1

    return uppr, lowr, dgts, whtspc
