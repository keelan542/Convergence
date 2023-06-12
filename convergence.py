# Import statements
import matplotlib.pyplot as plt
import sys

# Define list to store energy values
energies = []

# Open file and read line by line
try:
    with open(sys.argv[1]) as log_file:
        for line in log_file:
            if 'SCF Done' in line:
                energies.append(float(line.split()[4]))
except Exception:
    print(sys.argv[1] + " does not exist!")
    sys.exit()

# Getting zero point of energies
zero_point = min(energies)

# Redefining all items in energies list to be relative to zero_point and in kcal/mol
for i in range(len(energies)):
    energies[i] = (energies[i] - zero_point) * 627.51

# Define list to store number of steps for plotting purposes
steps = list(range(1, len(energies) + 1))

# Creating plot
fig, ax = plt.subplots()
ax.plot(steps, energies, marker='x')
ax.set_xticks(steps)
ax.set_xlabel('Step')
ax.set_ylabel('Energy [kcal/mol]')
ax.set_title('Convergence')
plt.show()
