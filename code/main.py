from utils import open_json_file
from functions import get_successful_op
from functions import sorted_data
from functions import getting_date_output
from functions import getting_index
from functions import get_op_output
from functions import getting_str

remittance = open_json_file()
list_val = get_successful_op(remittance)
list_sorted = sorted_data(list_val)
data_output = getting_date_output(list_sorted)
list_index = getting_index(list_val, list_sorted)
text_data = get_op_output(list_val, list_index)

print(getting_str(text_data, data_output))
