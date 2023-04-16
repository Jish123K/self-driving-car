import configparser

# Create a configparser object

config = configparser.ConfigParser()

# Set the default values for the settings

config["DEFAULT"]["screen_resolution"] = "1280x720"

config["DEFAULT"]["frame_rate"] = 30

config["DEFAULT"]["difficulty_level"] = "easy"

# Read the settings from the configuration file

with open("settings.ini", "r") as f:

    config.read_file(f)

# Get the current values for the settings

screen_resolution = config["DEFAULT"]["screen_resolution"]

frame_rate = config["DEFAULT"]["frame_rate"]

difficulty_level = config["DEFAULT"]["difficulty_level"]

# Display the settings to the user

print("Screen resolution:", screen_resolution)

print("Frame rate:", frame_rate)

print("Difficulty level:", difficulty_level)

# Allow the user to change the settings

while True:

    # Get the user's input for the screen resolution

    new_screen_resolution = input("Enter the new screen resolution: ")

    # If the user's input is valid, update the setting

    if new_screen_resolution:

        config["DEFAULT"]["screen_resolution"] = new_screen_resolution

    # Get the user's input for the frame rate

    new_frame_rate = input("Enter the new frame rate: ")

    # If the user's input is valid, update the setting

    if new_frame_rate:

        config["DEFAULT"]["frame_rate"] = new_frame_rate

    # Get the user's input for the difficulty level

    new_difficulty_level = input("Enter the new difficulty level: ")
# If the user's input is valid, update the setting

    if new_difficulty_level:

        config["DEFAULT"]["difficulty_level"] = new_difficulty_level

    # Ask the user if they are done changing the settings

    done = input("Are you done changing the settings? (y/n): ")

    # If the user says they are done, save the settings to the configuration file

    if done == "y":

        with open("settings.ini", "w") as f:

            config.write(f)

        break
        # If the user says they are not done, continue changing the settings

if done == "n":

    continue

# Display a message to the user that the settings have been saved

print("The settings have been saved.")

# Exit the settings menu

exit()
        
