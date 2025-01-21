# import pandas as pd
# import requests
# from sqlalchemy import create_engine
# from io import StringIO

# # SharePoint file URL and authentication details
# sharepoint_url = 'https://yoursharepointsite.com/path/to/your/file.csv'
# sharepoint_username = 'your_username'
# sharepoint_password = 'your_password'

# # Database connection details
# db_username = 'your_db_username'
# db_password = 'your_db_password'
# db_host = 'your_db_host'
# db_port = 'your_db_port'
# db_name = 'your_db_name'

# # Create a database connection
# engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

# # Function to download the CSV file from SharePoint
# def download_file_from_sharepoint(url, username, password):
#     response = requests.get(url, auth=(username, password))
#     if response.status_code == 200:
#         return response.text
#     else:
#         response.raise_for_status()

# # Download the CSV file
# csv_content = download_file_from_sharepoint(sharepoint_url, sharepoint_username, sharepoint_password)

# # Load the CSV content into a pandas DataFrame
# csv_buffer = StringIO(csv_content)
# df = pd.read_csv(csv_buffer)

# # Dump the DataFrame into the PostgreSQL database
# table_name = 'sharepoint_data'  # Replace with your table name
# df.to_sql(table_name, engine, if_exists='replace', index=False)

# print(f'Data from SharePoint has been loaded into the {table_name} table in the database.')

# import pandas as pd
# from shareplum import Site
# from shareplum import Office365
# from io import BytesIO

# # SharePoint credentials
# username = 'pranay.s@sreetechinc.com'
# password = ''
# site_url = 'https://sreetechinc1.sharepoint.com/:x:/r/sites/SREETECHINC/Shared%20Documents/employee_data.csv'
# doc_library = 'Documents'  # Change to your document library

# # Authenticate and get the site
# authcookie = Office365(site_url, username=username, password=password).GetCookies()
# site = Site(site_url, authcookie=authcookie)

# # Get the SharePoint folder
# folder = site.Folder(doc_library)

# # Get the file from the SharePoint folder
# file_name = 'employee_data.csv'  # Change to your file name
# file_content = folder.get_file(file_name)

# # Read the file content into a pandas DataFrame
# excel_file = BytesIO(file_content)
# df = pd.read_excel(excel_file)

# # Display the DataFrame
# print(df)

# import pandas as pd
# from office365.sharepoint.client_context import ClientContext
# from office365.sharepoint.files.file import File
# from shareplum import Site
# from shareplum import Office365
# from io import BytesIO
# from sqlalchemy import create_engine

# # SharePoint credentials
# sharepoint_url = 'https://your_sharepoint_site_url'
# sharepoint_username = 'your_username'
# sharepoint_password = 'your_password'
# relative_url = '/path/to/your/file.csv'

# # PostgreSQL credentials
# postgresql_user = 'your_postgresql_user'
# postgresql_password = 'your_postgresql_password'
# postgresql_host = 'your_postgresql_host'
# postgresql_port = 'your_postgresql_port'
# postgresql_db = 'your_postgresql_db'

# # Initialize SharePoint client
# ctx = ClientContext(sharepoint_url).with_credentials(sharepoint_username, sharepoint_password)
# response = File.open_binary(ctx, relative_url)

# # Save the file to a local path
# with open('local_file.csv', 'wb') as local_file:
#     local_file.write(response.content)

# # Read the CSV file into a DataFrame
# df = pd.read_csv('local_file.csv')

# # Create SQLAlchemy engine to connect to PostgreSQL
# engine = create_engine(f'postgresql+psycopg2://{postgresql_user}:{postgresql_password}@{postgresql_host}:{postgresql_port}/{postgresql_db}')

# # Write the DataFrame to a PostgreSQL table
# df.to_sql('your_table_name', engine, if_exists='replace', index=False)

# print("Data has been successfully dumped into PostgreSQL")

import csv

def parse_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Read the header row
        print(f'Header: {header}')
        
        for row in csv_reader:
            print(row)

# Example usage
file_path = 'C:\Users\PranayTejaS\OneDrive - SREETECH INC\profile\Downloads\business-operations-survey-2023-CSV-notes.xlsx'
parse_csv(file_path)

