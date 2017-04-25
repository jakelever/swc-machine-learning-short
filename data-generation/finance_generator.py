import random
import os
import argparse

def generateCompanyName(prefixes,suffixes):
	prefix = ['']


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Create financial statements for SWC shell adventure lesson')
	parser.add_argument('--transactionCount',type=int,default=100,help='Number of transactions to generate')
	parser.add_argument('--outFile',required=True,type=str,help='Output filename for statements')
	args = parser.parse_args()

	# Set up the set of company prefix and suffixes
	scriptDir = os.path.dirname(__file__)
	prefixPath = os.path.join(scriptDir,'company_prefixes.txt')
	with open(prefixPath) as f:
		prefixes = [ line.strip() for line in f ]
	suffixes = ['Ltd.', 'and Sons', 'Incorporated', 'Technologies', 'Farmers', 'Services', 'Worldwide', 'Global']

	companyNames = [ "%s %s" % (random.choice(prefixes),random.choice(suffixes)) for _ in xrange(30) ]

	# Now make a set of transcations with random amounts
	with open(args.outFile,'w') as outF:
		for i in range(args.transactionCount):

			if random.random() > 0.02:
				#companyName = "%s %s" % (random.choice(prefixes),random.choice(suffixes))
				companyName = random.choice(companyNames)
				
				amount = random.randint(1000,9999) / 100.0
			else:
				companyName = "Bishop Research"
				amount = random.randint(9000,9999) / 100.0

			line = "%-30s $ %4.2f" % (companyName,amount)
			outF.write(line+"\n")




