def transform(legacy_data):
    data={}
    for score in legacy_data.keys():
    	for values in legacy_data[score]:
    		data[values.lower()]=score

    return data
