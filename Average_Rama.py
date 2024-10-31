import pandas as pd

# Function to read and parse the data from the text file
def parse_data(filename):
    data = []
    #Name of the file
    with open("phi-psi.dat", 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            if len(parts) == 3:  # Ensure there are exactly three parts
                try:
                    residue = parts[0]
                    x = float(parts[1])
                    y = float(parts[2])
                    data.append([residue, x, y])
                except ValueError:
                    # Skip the line if conversion to float fails
                    continue
    return data[:114]  # Ensure only the first 114 lines are considered for CLP1 type and 87 for CLP2 type

# Generate filenames for all 1543 frames
filenames = [f'frame{i}.txt' for i in range(1500)]

# Read data for all frames
data_frames = [parse_data(filename) for filename in filenames]

# Convert each frame's data to DataFrames
dfs = [pd.DataFrame(data, columns=["Residue", "X", "Y"]) for data in data_frames]

# Ensure all DataFrames have the same Residue order
for df in dfs:
    df.set_index("Residue", inplace=True)

# Calculate the average across all frames
average_df = sum(dfs) / len(dfs)

# Reset index to make 'Residue' a column again
average_df.reset_index(inplace=True)

# Save the result to a CSV file
average_df.to_csv('averaged_residues_phi-psi.csv', index=False)

# Optionally, print the result
print(average_df)
