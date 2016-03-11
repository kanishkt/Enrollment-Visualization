import csv
import collections

def get_state_codes():
	state_codes = dict()

	with open('static/data/codefiles/state.txt', 'rb') as f:
		next(f) #skip first line
		for line in f:
			parts = line.split('|') #file is pipe delimited
			code = parts[0] #state code
			name = parts[2] #state name
			state_codes[name] = code
	return state_codes

def fix_states(state_codes, year):
	filename = 'data/state' + '-' + year + '.csv'
	temp = list()

	with open(filename, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			temp.append(row)

	if len(temp[0]) < 3:

		temp[0].append('fips')
		for i in range(1, len(temp)):
			state_name = temp[i][0].strip() #get state name, strip off the trailing space
			state_code = state_codes[state_name] #lookup state code

			temp[i].append(state_code) #add state code
			temp[i][0] = state_name #replace with stripped state name just in case..

		print temp

		with open(filename, 'wb') as f: #overwrite the old file
			writer = csv.writer(f)
			writer.writerows(temp)

def get_country_codes():
	country_codes = dict()

	with open('static/data/codefiles/country.csv', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			code = row[0]
			name = row[1]
			if name == "Korea, Republic of":
				name = "Korea, South"
			if name == "Macao":
				name = "Macau"
			if name == "United Kingdom":
				country_codes["Great Britain"] = code

			
			country_codes[name] = code
	return country_codes

def fix_countries(country_codes, year):
	filename = 'data/country' + '-' + year + '.csv'
	temp = list()

	with open(filename, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			temp.append(row)

	if len(temp[0]) < 3:

		temp[0].append('code')
		for i in range(1, len(temp)):
			country_name = temp[i][0].strip() #get country name, strip off the trailing space
			country_code = country_codes[country_name] #lookup state code

			temp[i].append(country_code) #add state code
			temp[i][0] = country_name #replace with stripped country name just in case..

		print temp

		with open(filename, 'wb') as f: #overwrite the old file
			writer = csv.writer(f)
			writer.writerows(temp)

def condense_states(state_codes):
	all_data = dict()
	for state, code in state_codes.items():
		all_data[state] = ['US'+code]
	row_one = ['state', 'fips']

	for year in range(2006, 2016):
		year = str(year)
		row_one.append(year)
		filename = 'static/data/state' + '-' + year + '.csv'
		temp = list()
		with open(filename, 'rb') as f:
			next(f)
			reader = csv.reader(f)
			for row in reader:
				state = row[0]
				number = row[1]
				#fips = row[2]

				all_data[state].append(number)
				temp.append(state)

		for state in state_codes.keys():
			if state not in temp:
				all_data[state].append('0')

	with open('static/data/state-all.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(row_one)
		for state, values in all_data.items():
			row = [state]
			row.extend(values)
			writer.writerow(row)

def condense_countries(country_codes):
	all_data = dict()
	for country, code in country_codes.items():
		all_data[country] = [code]
	row_one = ['country', 'code']

	for year in range(2006, 2016):
		year = str(year)
		row_one.append(year)
		filename = 'static/data/country' + '-' + year + '.csv'
		temp = list()
		with open(filename, 'rb') as f:
			next(f)
			reader = csv.reader(f)
			for row in reader:
				country = row[0]
				number = row[1]

				all_data[country].append(number)
				temp.append(country)

		for country in country_codes.keys():
			if country not in temp:
				all_data[country].append('0')

	with open('static/data/country-all.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(row_one)
		for country, values in all_data.items():
			row = [country]
			row.extend(values)
			writer.writerow(row)

if __name__ == "__main__":

	#state_codes = get_state_codes()
	#for year in range(2006, 2016):
		#fix_states(state_codes, str(year))

	country_codes = get_country_codes()
	#for year in range(2006, 2016):
	#	fix_countries(country_codes, str(year))
	
	#condense_states(state_codes)
	condense_countries(country_codes)
