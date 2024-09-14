import subprocess

# List of paths to your .exe files
exe_files = [
    r"C:\Program Files\WindowsApps\AD2F1837.OMENCommandCenter_1101.2409.4.0_x64__v10z8vjag6ke6\OmenCommandCenterApp\HP.Omen.OmenCommandCenter.exe",
    r"C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe",
    r"C:\Program Files\ThrottleStop_9.6\ThrottleStop.exe"
]

# Loop through and run each .exe file
for exe in exe_files:
    try:
        # Start the .exe process
        process = subprocess.Popen(exe)
        # process.wait()  # Wait for the process to complete
        print(f"Executed {exe} successfully.")
    except Exception as e:
        print(f"Failed to run {exe}: {e}")

