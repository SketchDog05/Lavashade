import urllib.request
import zipfile
import os

# Define the URL of the ReShade archive
reshade_url = "<RESHADE_URL>"

# Define the target directory where ReShade will be installed
target_directory = "<TARGET_DIRECTORY>"

# Define the path to the Roblox executable
roblox_executable = "<ROBLOX_EXECUTABLE>"

def install_reshade():
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Download the ReShade archive
    print("Downloading ReShade archive...")
    urllib.request.urlretrieve(reshade_url, "reshade_archive.zip")

    # Extract the contents of the ReShade archive
    print("Extracting ReShade archive...")
    with zipfile.ZipFile("reshade_archive.zip", "r") as zip_ref:
        zip_ref.extractall(target_directory)

    # Clean up the downloaded ZIP file
    os.remove("reshade_archive.zip")

    # Install ReShade for Roblox
    print("Installing ReShade for Roblox...")
    install_script = os.path.join(target_directory, "ReShade_Setup.exe")
    os.system(f'"{install_script}" /install "{roblox_executable}"')

    print("ReShade installed successfully!")

# Run the installer
install_reshade()
