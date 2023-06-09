# Define list to store energy values
energies = []

# Open file and read line by line
with open("H_HMDS.log") as log_file:
    for line in log_file:
        if 'SCF Done' in line:
            energies.append(float(line.split()[4]))

# Define list to store number of steps for plotting purposes
steps = list(range(1, len(energies) + 1))
