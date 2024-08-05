from datetime import date
import inflect
import sys

def main():
    # Prompt user for date of birth in YYYY-MM-DD format
        dob = date.fromisoformat(input("Enter your Date of Birth (YYYY-MM-DD): "))

if __name__ == 'main':
    main()