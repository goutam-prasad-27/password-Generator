# password-Generator
 **Here's a breakdown of the code:**

**1. Imports:**

- **Imports the `random` and `string` modules** for working with random numbers and string manipulation.

**2. Character Sets:**

- **Defines four character sets:**
    - `lower_case`: Contains all lowercase letters (`a-z`).
    - `upper_case`: Contains all uppercase letters (`A-Z`).
    - `symbols`: Contains all punctuation symbols (`!@#$%^&*()_+-=[]{};':"\|,./<>?`).
    - `digits`: Contains all digits (`0-9`).

**3. Password Generation Function:**

- **`passGen(len, add_upper=True, add_digit=True, add_symbols=True)`:** This function generates a password.
    - **Arguments:**
        - `len`: The desired length of the password.
        - `add_upper` (default: True): Whether to include uppercase letters.
        - `add_digit` (default: True): Whether to include digits.
        - `add_symbols` (default: True): Whether to include symbols.
    - **Steps:**
        1. Creates an empty string `all_Char` to hold potential characters.
        2. Conditionally adds character sets to `all_Char` based on user preferences for uppercase, digits, and symbols.
        3. Always adds lowercase letters to `all_Char`.
        4. Uses `random.sample(all_Char, len)` to randomly select `len` characters from `all_Char` without replacement.
        5. Joins the selected characters into a string using `"".join()`.
        6. Returns the generated password.

**4. User Input:**

- **Prompts the user for:**
    - Desired password length.
    - Whether to include uppercase letters, symbols, and numbers.

**5. Calling the Function and Printing the Result:**

- **Calls the `passGen` function** with the user's preferences as arguments.
- **Prints the generated password** to the console.

