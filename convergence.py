# Open file and read line by line
with open("H_HMDS.log") as log_file:
    for line in log_file:
        if 'SCF Done' in line:
            print(line)
