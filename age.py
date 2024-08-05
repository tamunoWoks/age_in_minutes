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

    # Create an inflect engine instance for converting numbers to words
    p = inflect.engine()

    # Calculate total minutes from date of birth to today
    collective_mins = get_collective_mins(dob, date.today())


if __name__ == 'main':
    main()