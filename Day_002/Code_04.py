import os

print("*************** Let's deal with the os module in Python *************")

# Current working directory
print("Current working directory is:", os.getcwd())

# List all files and directories in current working directory
print("List of files and directories in current working directory:", os.listdir())

# Create new directory
os.mkdir("new_directory")
print("Created a new directory named 'new_directory'.")

# Rename directory
os.rename("new_directory", "renamed_directory")
print("Renamed the directory 'new_directory' to 'renamed_directory'.")

# Remove directory
os.rmdir("renamed_directory")
print("Removed the directory 'renamed_directory'.")

# Environment variables
print("Current environment variables are:", os.environ)

# Current username (with error handling)
try:
    print("Current user name is:", os.getlogin())
except OSError:
    print("Could not get login name (might be running in an environment without a terminal).")

# Process ID
print("Current process ID is:", os.getpid())

# OS name
print("Current platform (os.name) is:", os.name)

# System information using uname()
if hasattr(os, 'uname'):
    uname = os.uname()
    print("System information:")
    print("  System name:", uname.sysname)
    print("  Node name:", uname.nodename)
    print("  Release:", uname.release)
    print("  Version:", uname.version)
    print("  Machine:", uname.machine)
else:
    print("os.uname() is not available on this platform.")

print("In this way, we can use the os module to interact with the operating system.")
print("========================================")
print("This is the end of the os module demonstration.")
