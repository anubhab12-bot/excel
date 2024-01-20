import pandas as pd
import json

# Load JSON data from the provided file
with open('datasheet.json', 'r') as json_file:
    data = json.load(json_file)

# Extract relevant information from the JSON data
overviews_df = pd.DataFrame(data['overviews'])
worker_types_df = pd.DataFrame(data['workerTypes'])

# Flatten the 'groups' field with dynamic prefixes to avoid conflicts
groups_df = pd.json_normalize(data['groups'], 'fields', sep='_', meta=['label', 'description'],
                               record_prefix=lambda x: f'{x}_')

# Create an Excel writer and write all data to one sheet
with pd.ExcelWriter('output1.xlsx', engine='xlsxwriter') as writer:
    overviews_df.to_excel(writer, sheet_name='AllData', startrow=0, startcol=0, index=False)
    worker_types_df.to_excel(writer, sheet_name='AllData', startrow=0, startcol=len(overviews_df.columns) + 2, index=False)
    groups_df.to_excel(writer, sheet_name='AllData', startrow=0, startcol=len(overviews_df.columns) + len(worker_types_df.columns) + 4, index=False)

print("Excel file 'output.xlsx' has been created successfully.")
