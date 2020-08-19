# import functions

# import functions
import gt3x_functions as gt3x 

def read_gt3x(f, save_location = None):

	# unzip .gt3x file and get the file location of the binary log.bin (which contains the raw data) and the info.txt which contains the meta-data
	log_bin, info_txt = gt3x.unzip_gt3x_file(f = file, save_location = save_location, delete_source_file = False)

	# get meta data from info.txt file
	meta_data = gt3x.extract_info(info_txt)

	# read raw data from binary data
	log_data, time_data = gt3x.extract_log(log_bin = log_bin, acceleration_scale = float(meta_data['Acceleration_Scale']), sample_rate = int(meta_data['Sample_Rate']), use_scaling = False)

	actigraph_acc = gt3x.rescale_log_data(log_data = log_data, acceleration_scale = meta_data['Acceleration_Scale'])

	# convert time data to correct time series array with correct miliseconds values
	actigraph_time = gt3x.create_time_array(time_data)
	return actigraph_acc, actigraph_time, meta_data
