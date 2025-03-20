import csv

class CSVFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self) -> dict:
        """Reads a CSV file and returns a dictionary with column-wise data."""
        with open(self.file_path, newline='', encoding='utf-8') as file_obj:
            reader = csv.DictReader(file_obj)

            data = {column: [] for column in reader.fieldnames} if reader.fieldnames else {}

            for row in reader:
                for column in reader.fieldnames:
                    data[column].append(row[column])

        return data

    def write_file(self, data: dict) -> int:
        """Writes a dictionary to a CSV file.
        
        Returns:
        - 0: Data written successfully
        - 1: Empty file created
        - 2: Failure due to invalid input
        """
        try:
            with open(self.file_path, "w", newline='', encoding='utf-8') as file_obj:
                if not data:
                    file_obj.write("")  # Create a blank file
                    return 1  # Empty file created

                field_names = data.keys()
                writer = csv.DictWriter(file_obj, fieldnames=field_names)
                writer.writeheader()

                rows = [dict(zip(field_names, values)) for values in zip(*data.values())]
                writer.writerows(rows)

            return 0  # Data written successfully

        except Exception as e:
            print(f"Error writing file: {e}")  # Log error (optional)
            return 2  # Failure due to an exception

# Example Usage:
csv_file = CSVFile("data.csv")

# Read CSV
data = csv_file.read_file()
print("Read Data:", data)

# Example: Writing to a file
status = csv_file.write_file(data)

if status == 0:
    print("✅ File written successfully!")
elif status == 1:
    print("⚠️ Empty file created.")
elif status == 2:
    print("❌ Failed to write file.")

