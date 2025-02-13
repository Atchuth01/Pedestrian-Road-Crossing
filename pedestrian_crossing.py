import pandas as pd

# Load vehicle count data
df = pd.read_csv("D:/Documents/archive (1)/Videos/vehicle_counts.csv")

# Define vehicle threshold for safe crossing
SAFE_VEHICLE_THRESHOLD = 4

# Group safe frames together
safe_durations = []
current_start = None

# Process each video separately
for video in df["Video"].unique():
    video_df = df[df["Video"] == video]

    for _, row in video_df.iterrows():
        frame = row["Frame"]
        vehicle_count = row["Vehicle Count"]

        if vehicle_count <= SAFE_VEHICLE_THRESHOLD:
            if current_start is None:
                current_start = frame  # Start of safe crossing duration
        else:
            if current_start is not None:
                safe_durations.append([video, current_start, frame - 1])  # Store safe duration
                current_start = None

    # If the last frames were safe, close the range
    if current_start is not None:
        safe_durations.append([video, current_start, frame])

# Save results to CSV
safe_df = pd.DataFrame(safe_durations, columns=["Video", "Start Frame", "End Frame"])
safe_df.to_csv("D:/Documents/archive (1)/Videos/safe_durations.csv", index=False)

print("Safe crossing durations saved as safe_durations.csv")
