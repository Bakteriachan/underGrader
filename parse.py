import os
def parse():
	for a,b,c in os.walk('./data'):
		for i in c:
			if i.startswith('0'):
				os.rename(os.path.join('.','data',i),os.path.join('.','data',i[1:]))
				
				
Flag = True

while Flag:
	curr = False
	for a,b,c in os.walk('./data'):
		for i in c:
			if i.startswith('0'):
				curr = True
				break
				
	if curr == True:
		parse()
	else:
		Flag = False
