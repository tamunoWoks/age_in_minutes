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

if __name__ == 'main':
    main()