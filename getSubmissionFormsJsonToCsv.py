# Python program to convert
# JSON file to CSV


import json
import csv


# Opening JSON file and loading the data
# into the variable data
with open('submissions.json') as json_file:
	data = json.load(json_file)

submission_data = data['content']

# now we will open a file for writing
data_file = open('submissionForms.csv', 'w')
data_file2 = open('SubmissionFormValues.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)
csv_writer2 = csv.writer(data_file2)

# Counter variable used for writing
# headers to the CSV file
count = 0

for submission in submission_data:
	if count == 0:

		# Writing headers of CSV file
		header = submission.keys()
		csv_writer.writerow(header)
		count += 1
		count2  = 0
		csvanswers=[]
	for answer in submission["answers"]:
		if count2 == 0:
			header2 = submission["answers"][answer].keys()
			count2 += 1
			#print(header2) #csv_writer2.writerow(header2)
		namehold = " "
		for a2 in submission["answers"][answer]:
			if (a2=='name'):
				namehold=submission["answers"][answer][a2]
			if (a2=='answer'):
				csvanswers.append({ "SubmissionId": submission["id"] })
				csvanswers.append({ namehold : submission["answers"][answer][a2] })
				csv_writer2.writerow(csvanswers)
				csvanswers=[]
	# Writing data of CSV file
	csv_writer.writerow(submission.values())

data_file.close()

