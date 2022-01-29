from datetime import datetime

def converter(*, dt:str):
	data_time_object = datetime.strptime(dt, "%Y/%m/%d, %H:%M:%S")
	unix_time = (data_time_object - datetime(1970,1,1)).total_seconds()
