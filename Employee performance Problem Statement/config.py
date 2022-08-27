
import pandas
import json
from io import StringIO
#Reading the data into pandas Dataframe from Excel
excel_data_df = pandas.read_excel('Hackathon Timesheet.xlsx', sheet_name='All Projects')


# json_str = excel_data_df.to_json()
# str_io_obj = StringIO(json_str)
# print('Excel Sheet to JSON:\n', json.load(str_io_obj))


