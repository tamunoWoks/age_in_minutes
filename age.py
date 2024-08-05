from datetime import date
import inflect
import sys

def main():
    try:
        # Prompt user for date of birth in YYYY-MM-DD format
        dob = date.fromisoformat(input("Enter your Date of Birth (YYYY-MM-DD): "))

        # Check if the date of birth is not in the future
        if dob > date.today():
            raise ValueError("Date of Birth cannot be in the future.")
        
    except ValueError as e:
        # Exit the program with an error message if input is invalid
        sys.exit(f"Invalid Input: {e}")

if __name__ == 'main':
    main()