import random
import pandas as pd

def roll_die_simulation(n=1000):
    """
    Simulates rolling a die 'n' times and assigns continuous values to different die faces.
    """
    faces = {i: [] for i in range(1, 7)}  # Store die face values

    for _ in range(n):
        working_number = random.random()  # Generates a number in [0,1]

        if working_number < 1/6:
            faces[1].append(working_number)
            continue
        if working_number < 2/6:
            faces[2].append(working_number)
            continue
        if working_number < 3/6:
            faces[3].append(working_number)
            continue
        if working_number < 4/6:
            faces[4].append(working_number)
            continue
        if working_number < 5/6:
            faces[5].append(working_number)
            continue
        faces[6].append(working_number)  # Last category

    # Compute frequency of each die face
    frequency = {key: len(value) for key, value in faces.items()}
    total_rolls = sum(frequency.values())

    # Compute percentage frequency
    percentage_frequency = {key: round((value / total_rolls) * 100, 2) for key, value in frequency.items()}

    # Create a well-structured DataFrame
    df = pd.DataFrame({
        'Die Face': list(frequency.keys()),
        'Frequency': list(frequency.values()),
        'Percentage Frequency (%)': list(percentage_frequency.values())
    })

    print(df)

# Run the simulation
roll_die_simulation()
