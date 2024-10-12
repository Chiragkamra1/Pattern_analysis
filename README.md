Message Grouping and Pattern Detection

Overview

This project is designed to group similar messages and identify dynamic elements such as amounts, URLs, phone numbers, and unique IDs within the message content. By leveraging fuzzy matching techniques and pattern recognition, the program can effectively categorize messages and separate the static content from variable elements like transaction amounts, verification codes, or URLs.

The final output is a set of groups with messages that share a similar structure, stored in CSV files, with dynamic elements (such as amounts, URLs, etc.) being detected and handled separately.

Features

Fuzzy Message Grouping: Automatically groups similar messages using fuzzy matching, which checks how closely two messages resemble each other.
Pattern Recognition: Dynamically detects and categorizes variable elements in messages:
Amounts: Detects currency amounts, supporting various formats like Rs, ₹, USD, etc.
URLs: Recognizes web addresses starting with http, https, or common URL shorteners like bit.ly.
Phone Numbers: Identifies phone numbers as sequences of 10 or more digits, with or without a + sign.
Unique IDs: Extracts alphanumeric unique identifiers like transaction IDs or verification codes.
CSV Output: Each group of messages is saved as a CSV file in a folder structure, making it easy to analyze grouped content.
Modular Code: The code is modular and adaptable, allowing for easy customization of thresholds and patterns for different types of messages.
How It Works

Load Data: The program loads the data from a CSV file where each message is represented as a text string.
Fuzzy Matching: Messages are compared using fuzzy string matching techniques, and those with a similarity score above a configurable threshold are grouped together.
Pattern Detection: The program identifies variable parts of each message (e.g., amounts, phone numbers, URLs, and unique IDs) and retains only the static content for grouping purposes.
Organized Output: Each group of similar messages is saved into a folder with a CSV file, where all grouped messages are stored.
Prerequisites

Python 3.x
Required Python libraries:
pandas
fuzzywuzzy
python-Levenshtein (optional, but recommended for faster fuzzy matching)
You can install the necessary packages using:


pip install pandas fuzzywuzzy python-Levenshtein
Setup

Prepare the Data: Ensure your data is in a CSV file with a column containing the message text you want to process.
Run the Script: Execute the Python script, and it will group similar messages and categorize the dynamic content.
Example Use Case

This program is ideal for businesses or developers working with large sets of messages (such as customer SMS notifications, transactional alerts, or verification codes). By grouping and processing similar messages, you can streamline data analysis, detect patterns, and automate workflows.

Customization

Threshold Adjustment: You can adjust the similarity threshold for fuzzy matching to make the grouping stricter or more lenient.
Pattern Recognition Customization: Modify the patterns for amounts, URLs, phone numbers, or unique IDs as per your requirements.
Future Improvements

Additional Dynamic Elements: Expand the pattern recognition to cover more variable message components (e.g., dates, times).
Enhanced Visualization: Add support for visualizing the grouped messages or showing key statistics on the patterns identified.
Contributing

If you'd like to contribute, feel free to submit a pull request or open an issue to discuss any improvements, bug fixes, or features.

