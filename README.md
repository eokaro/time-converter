This Python script is designed to convert a total number of seconds into a more readable time format, breaking it down into hours, minutes, and seconds. The program supports both 24-hour and 12-hour (AM/PM) formats, making it flexible for various user preferences.

Key Features
Input Validation & Error Handling:
The script continuously prompts the user to enter a valid, non-negative number of seconds. If the input is invalid, a detailed error message is logged using Python’s built-in logging module, and the user is asked to re-enter the value.

Modular Design:
The functionality is broken down into several functions:

convert_seconds(total_seconds): Converts the total seconds into hours, minutes, and seconds.

convert_to_12_hour_format(hours, minutes, seconds): Adjusts a 24-hour time format to 12-hour format with an AM/PM designation.

display_time(hours, minutes, seconds, format_24h): Displays the formatted time based on the user’s preference (either 24-hour or 12-hour format).

get_user_input(): Handles the user input, ensuring that only valid data is processed.

main(): Orchestrates the overall flow by calling the necessary functions and handling exceptions gracefully.

Logging:
Logging is configured at the start to capture debug-level messages. This is useful for tracking errors and understanding the flow of the program during execution, which is especially helpful during development or when troubleshooting issues.

User-Friendly Interaction:
The script interacts with the user through the console. It prompts for the number of seconds and asks whether the output should be in a 24-hour or 12-hour format, ensuring the interface is simple and straightforward.

How It Works
User Input:
The program begins by asking the user to input a number of seconds. It validates this input, ensuring it's a valid, non-negative number.

Conversion Process:
Once valid input is provided, the program converts the total seconds into hours, minutes, and seconds using the convert_seconds function.

Format Selection:
The user is then prompted to choose between a 24-hour or 12-hour output format. Depending on the choice, the program either directly prints the time in 24-hour format or converts it to 12-hour format using convert_to_12_hour_format before displaying.

Error Management:
Throughout the process, any exceptions or invalid inputs are caught and logged, ensuring that the program fails gracefully with meaningful messages.

