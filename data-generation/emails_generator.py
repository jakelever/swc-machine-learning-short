import argparse
import os
import random
import time

import random
import time
from collections import defaultdict

# From: http://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
def strTimeProp(start, end, format, prop):
	"""Get a time at a proportion of a range of two formatted times.

	start and end should be strings specifying times formated in the
	given format (strftime-style), giving an interval [start, end].
	prop specifies how a proportion of the interval to be taken after
	start.  The returned time will be in the specified format.
	"""
	stime = time.mktime(time.strptime(start, format))
	etime = time.mktime(time.strptime(end, format))

	ptime = stime + prop * (etime - stime)

	return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
	return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Create fake emails for the Software Carpentry Unix Shell Adventure lesson')
	parser.add_argument('--contactsFile',type=str,required=True,help='File to output contacts')
	parser.add_argument('--emailsDir',type=str,required=True,help='Directory to output emails to')
	parser.add_argument('--emailsSummaryDir',type=str,required=True,help='Directory to output email summaries to')
	args = parser.parse_args()

	dateFrom = "1/1/2017 1:30 PM"
	dateTo = "4/1/2017 4:50 AM"

	scriptDir = os.path.dirname(__file__)
	firstnamesPath = os.path.join(scriptDir,'firstnames.txt')
	with open(firstnamesPath) as f:
		firstnames = [line.strip() for line in f]
	surnamesPath = os.path.join(scriptDir,'surnames.txt')
	with open(surnamesPath) as f:
		surnames = [line.strip() for line in f]


	prefixPath = os.path.join(scriptDir,'company_prefixes.txt')
	with open(prefixPath) as f:
		prefixes = [ line.strip() for line in f ]
	suffixes = ['Ltd.', 'and Sons', 'Incorporated', 'Technologies', 'Farmers', 'Services', 'Worldwide', 'Global']

	rolesPath = os.path.join(scriptDir,'job_roles.txt')
	with open(rolesPath) as f:
		roles = [ line.strip() for line in f ]
	
	locationsPath = os.path.join(scriptDir,'locations.txt')
	with open(locationsPath) as f:
		locations = [ line.strip() for line in f ]
	#companyNames = [ "%s %s" % (random.choice(prefixes),random.choice(suffixes)) for _ in xrange(30) ]


	sentTemplatesPath = os.path.join(scriptDir,'templates.sent.txt')
	with open(sentTemplatesPath) as f:
		sentTemplates = f.read().split('~')
	receivedTemplatesPath = os.path.join(scriptDir,'templates.received.txt')
	with open(receivedTemplatesPath) as f:
		receivedTemplates = f.read().split('~')

	print "Generating contacts..."
	contacts = []
	for _ in range(200):
		firstname,surname = (random.choice(firstnames),random.choice(surnames))
		companyname = "%s %s" % (random.choice(prefixes),random.choice(suffixes))
		role = random.choice(roles)
		location = random.choice(locations)
		contact = (firstname,surname,companyname,role,location)
		contacts.append(contact)

	with open(args.contactsFile,'w') as outF:
		for contact in contacts:
			line = "%s %s\t%s\t%s\t%s" % (contact)
			#print line
			outF.write(line+"\n")

	print "Generating emails..."
	receivedDict = defaultdict(list)
	sentDict = defaultdict(list)
	emailsDict = defaultdict(list)
	for _ in range(2000):
		sent = random.random() > 0.5
		contact = random.choice(contacts)
		if sent:
			email = random.choice(sentTemplates)
		else:
			email = random.choice(receivedTemplates)

		(firstname,surname,companyname,role,location) = contact
		fullname = "%s %s" % (firstname,surname)
		fullnameUnderscore = "%s_%s" % (firstname,surname)

		email = email.replace('FIRSTNAME',firstname)
		email = email.replace('SURNAME',surname)
		email = email.replace('FULLNAME',fullname)
		email = email.replace('COMPANYNAME',companyname)
		email = email.replace('ROLE',role)
		email = email.replace('LOCATION',location)

		dateTime = randomDate(dateFrom,dateTo,random.random())
		date = dateTime[:10]
		emailTime = dateTime[10:]

		if sent:
			sentDict[fullnameUnderscore].append(dateTime)
		else:
			receivedDict[fullnameUnderscore].append(dateTime)

		
		emailsDict[date].append((sent,contact,email,emailTime))

	emailsSummaryDir = args.emailsSummaryDir
	receivedDir = os.path.join(emailsSummaryDir,'received')
	sentDir = os.path.join(emailsSummaryDir,'sent')

	if not os.path.isdir(receivedDir):
		os.mkdir(receivedDir)
	if not os.path.isdir(sentDir):
		os.mkdir(sentDir)

	print "Writing received emails summary"
	for fullNameUnderscore,datetimes in receivedDict.items():
		path = os.path.join(receivedDir,'%s.txt' % fullNameUnderscore)
		datetimes = sorted(datetimes)
		with open(path,'w') as outF:
			for dt in datetimes:
				outF.write(dt+"\n")

	print "Writing sent emails summary"
	for fullNameUnderscore,datetimes in sentDict.items():
		path = os.path.join(sentDir,'%s.txt' % fullNameUnderscore)
		datetimes = sorted(datetimes)
		with open(path,'w') as outF:
			for dt in datetimes:
				outF.write(dt+"\n")

	print "Saving emails..."
	for date in emailsDict:
		dateDir = os.path.join(args.emailsDir,date.replace('/','_'))
		if not os.path.isdir(dateDir):
			os.mkdir(dateDir)

		for emailObj in emailsDict[date]:
			#print date,emailObj
			(sent,contact,email,emailTime) = emailObj
			(firstname,surname,companyname,role,location) = contact

			timeFixed = emailTime.replace(':','_').replace(' ','')
			if sent:
				filename = "SENT_TO_%s_%s.%s.txt" % (firstname,surname,timeFixed)
			else:
				filename = "RECEIVED_FROM_%s_%s.%s.txt" % (firstname,surname,timeFixed)

			fullFilename = os.path.join(dateDir,filename)
			with open(fullFilename,'w') as outF:
				outF.write(email+"\n")

				


