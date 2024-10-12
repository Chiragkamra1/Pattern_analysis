import os
import pandas as pd
from fuzzywuzzy import process
import re

# Load data from CSV file
file_path = './SMS-Data.csv'
df = pd.read_csv(file_path)

# Convert the text column to string and handle missing values
df['text'] = df['text'].astype(str).fillna('')

# Extract the text column
messages = df['text'].tolist()

def extract_static_part(message):
    # Example: Remove monetary amounts, URLs, and any other variable parts
    message = re.sub(r'\d+(\.\d{1,2})?', '<LOG>', message)  # Replace amounts
    message = re.sub(r'https?://\S+|[A-Za-z0-9._%+-]+(?:\.com|\.in|\.gov|\.net|\.org|\.edu|\.co|\.uk|\.us)\b', '<URL>', message)
    message = re.sub(r'\d+', '<ID>', message)  # Replace IDs
    return message

def group_messages(messages, threshold=60):
    grouped_messages = []
    used_indices = set()
    
    for i, msg in enumerate(messages):
        if i in used_indices:
            continue
        
        # Create a new group for the current message
        new_group = [msg]
        used_indices.add(i)
        
        # Extract static parts
        static_msg = extract_static_part(msg)
        
        # Find similar messages to the current message
        for j, other_msg in enumerate(messages):
            if i != j and j not in used_indices:
                static_other_msg = extract_static_part(other_msg)
                similarity = process.fuzz.ratio(static_msg, static_other_msg)
                if similarity >= threshold:
                    new_group.append(other_msg)
                    used_indices.add(j)
        
        # Merge the new group with existing groups if applicable
        merged = False
        for group in grouped_messages:
            if any(process.fuzz.ratio(static_msg, extract_static_part(existing_msg)) >= threshold for existing_msg in group):
                group.extend(new_group)
                merged = True
                break
        
        if not merged:
            grouped_messages.append(new_group)
    
    return grouped_messages

# Group messages based on fuzzy matching
grouped_messages = group_messages(messages)

# Create a directory for grouped messages
output_dir = './Grouped_Messages'
os.makedirs(output_dir, exist_ok=True)

# Save grouped messages into CSV files within folders
for idx, group in enumerate(grouped_messages):
    if group:
        group_folder = os.path.join(output_dir, f'Group_{idx + 1}')
        os.makedirs(group_folder, exist_ok=True)
        
        # Extract static parts of messages
        static_group = [extract_static_part(msg) for msg in group]
        
        # Create a DataFrame for the static group
        group_df = pd.DataFrame({'Static_Message': static_group})
        group_csv_path = os.path.join(group_folder, 'messages.csv')
        group_df.to_csv(group_csv_path, index=False)

# Print total number of grouped messages and total number of groups
total_grouped_messages = sum(len(group) for group in grouped_messages)
total_groups = len(grouped_messages)

print(f"Total number of grouped messages: {total_grouped_messages}")
print(f"Total number of groups created: {total_groups}")
print(f"Grouped messages have been saved to {output_dir}")
