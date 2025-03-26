import logging

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_seconds(total_seconds: float) -> tuple[int, int, int]:
    """
    Converts total seconds to hours, minutes, and seconds.
    
    Args:
        total_seconds (float): Total number of seconds to convert
    
    Returns:
        tuple: (hours, minutes, seconds) as integers
    """
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative.")
    
    # Use int() to round down and ensure whole numbers
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    
    return hours, minutes, seconds

def convert_to_12_hour_format(hours: int, minutes: int, seconds: int) -> tuple[int, int, int, str]:
    """
    Converts hours to 12-hour format with AM/PM designation.
    
    Args:
        hours (int): Hours in 24-hour format
        minutes (int): Minutes
        seconds (int): Seconds
    
    Returns:
        tuple: (hours, minutes, seconds, period)
    """
    period = "AM"
    adjusted_hours = hours
    
    if hours >= 12:
        period = "PM"
        adjusted_hours = hours - 12 if hours > 12 else 12
    elif hours == 0:
        adjusted_hours = 12  # Midnight is 12 AM
    
    return adjusted_hours, minutes, seconds, period

def display_time(hours: int, minutes: int, seconds: int, format_24h: bool = True):
    """
    Displays the converted time in hours, minutes, and seconds.
    
    Args:
        hours (int): Hours to display
        minutes (int): Minutes to display
        seconds (int): Seconds to display
        format_24h (bool, optional): Whether to use 24-hour format. Defaults to True.
    """
    if format_24h:
        print(f"Here is the time in 24-hour format: {hours:02d}:{minutes:02d}:{seconds:02d}")
    else:
        h, m, s, period = convert_to_12_hour_format(hours, minutes, seconds)
        print(f"Here is the time in 12-hour format: {h:02d}:{m:02d}:{s:02d} {period}")

def get_user_input() -> float:
    """
    Gets and validates the user input for total seconds.
    
    Returns:
        float: Validated number of total seconds
    """
    while True:
        try:
            user_input = input("Enter a number of seconds: ").strip()
            total_seconds = float(user_input)
            
            if total_seconds < 0:
                raise ValueError("Total seconds must be a positive number.")
            
            return total_seconds
        except ValueError as e:
            logging.error(f"Invalid input: {e}")
            print(f"Invalid input. Please enter a valid number of seconds.")

def main():
    """
    Main function to orchestrate time conversion process.
    """
    try:
        total_seconds = get_user_input()
        hours, minutes, seconds = convert_seconds(total_seconds)
        
        # Improved format choice input handling
        while True:
            format_choice = input("Would you like the time in 24-hour format? (yes/no): ").lower().strip()
            if format_choice in ['yes', 'no', 'y', 'n']:
                break
            print("Please enter 'yes' or 'no'.")
        
        display_time(hours, minutes, seconds, format_24h=format_choice not in ['no', 'n'])
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
