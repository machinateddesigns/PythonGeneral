import itertools
import csv

# 1. Your specific list of Mage Spheres
spheres = [
    'correspondence', 'entropy', 'forces', 'life', 
    'matter', 'mind', 'prime', 'spirit', 'time'
]

# 2. Sort reverse-alphabetically (optional, based on your preference)
spheres.sort(reverse=True)

# 3. Generate all unique sets of 3
# itertools handles the 'no repeats' logic automatically
unique_sets = list(itertools.combinations(spheres, 3))

# 4. Write to CSV file
filename = "mage_sphere_combinations.csv"
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(["Sphere 1", "Sphere 2", "Sphere 3"])
    
    # Write all 84 combinations
    writer.writerows(unique_sets)

print(f"Successfully saved {len(unique_sets)} combinations to {filename}.")