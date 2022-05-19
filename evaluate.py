import sys,os
sys.argv = sys.argv[1:]

def run():

	try:
		with open('output.out') as ProgramOutputFile:
			with open(sys.argv[0]) as CorrectOutputFile:
				programOutputList = []
				correctOutputList = []
				for line in ProgramOutputFile:
					programOutputList.append(line)
				
				for line in CorrectOutputFile:
					correctOutputList.append(line)
					
				if correctOutputList[-1] == '\n':
					correctOutputList.pop()
				if programOutputList[-1] == '\n':
					programOutputList.pop()


				if(len(programOutputList) != len(correctOutputList)):
					print("Output length isn't correct",file=sys.stderr)
					print('3')
					return
					
				for i in range(len(programOutputList)):
					programOutputList[i] = programOutputList[i].strip(); 
					programOutputList[i] = programOutputList[i].strip('\n')
				
				for i in range(len(correctOutputList)):
					correctOutputList[i] = correctOutputList[i].strip(); 
					correctOutputList[i] = correctOutputList[i].strip('\n')
				
				for i in range(min(len(programOutputList),len(correctOutputList))):
					if programOutputList[i] != correctOutputList[i]:
						print(f'Expected {correctOutputList[i]}, found {programOutputList[i]} at line {i+1}',file=sys.stderr)
						print('3')
						return
				
					
				print('1')
				return
					
				
	except:
		print('2')

		print(sys.exc_info(),file=sys.stderr)


run()


