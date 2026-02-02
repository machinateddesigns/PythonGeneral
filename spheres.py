import itertools
import json

# 1. Define the 9 Spheres of Reality
spheres = [
    'correspondence', 'entropy', 'forces', 'life', 
    'matter', 'mind', 'prime', 'spirit', 'time'
]

# 2. Sort them reverse-alphabetically (high-to-low) 
# as per your previous preference
spheres.sort(reverse=True)

# 3. Generate all unique sets of 3
# itertools.combinations naturally prevents repeats
unique_sphere_sets = list(itertools.combinations(spheres, 3))

# 4. Print Summary
print(f"Generated {len(unique_sphere_sets)} unique Sphere archetypes.\n")

# 5. Output first 5 as an example
for archetype in unique_sphere_sets[:84]:
    print(f"{', '.join(archetype).title()}")

# 6. Optional: Save to JSON for game data
with open('mage_archetypes.json', 'w') as f:
    json.dump(unique_sphere_sets, f, indent=4)
