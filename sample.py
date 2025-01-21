import csv
import os

def parse_csv(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    encodings = ['utf-8', 'iso-8859-1', 'cp1252']

    for encoding in encodings:
        try:
            with open(file_path, mode='r', encoding=encoding) as file:
                csv_reader = csv.reader(file)
                header = next(csv_reader)  # Read the header row
                print(f'Header: {header} (Encoding: {encoding})')

                for row in csv_reader:
                    print(row)
            break  # Exit the loop if the file is read successfully
        except UnicodeDecodeError:
            print(f"Encoding error with {encoding}. Trying next encoding...")
        except FileNotFoundError as e:
            print(f"Error: {e}")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

# Example usage
file_path = 'C:\\Users\\PranayTejaS\\OneDrive - SREETECH INC\\profile\\Downloads\\Weekly Status Report 18-06-2024 to 21-06-2024.xlsx'
parse_csv(file_path)

# "C:\Users\PranayTejaS\OneDrive - SREETECH INC\profile\Downloads\Weekly Status Report 18-06-2024 to 21-06-2024.xlsx"