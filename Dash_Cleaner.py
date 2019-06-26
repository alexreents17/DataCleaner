#!/usr/bin/python
import pandas as pd
import numpy as np

# Special Case: 
#				28W092-1 Commercial Ave & 28W092-2 Commercial Ave (Fixed)
# 				13318-B Wicker Ave 
#				13640 Us-41 
#				1085 In-149
# 				4644 1/2-4648 N Western Ave
#				0 Us-41
#				1N046-1N050 Linlar Dr
#				1061A-E Caton Farm Rd
				
'''
effects:  Delete the second number if there is a dash connects 
		  two numbers. Ex. 1229-1241 74th St  -> 1229 74th St
returns:  A dataframe named "Fixed Address"
'''
def fixedAddress(dataFrame):
	L=[]
	for str_complete in dataFrame:
			s_split=str_complete.split()
			if("-" in s_split[0]):
				# Split the first string by dash
				# "1229-1241" -> "[1229,1241]"
				s_nums=s_split[0].split("-")
				# Check if is digit or the second string is a fraction
				if ((s_nums[0]).isdigit() and ((s_nums[1]).isdigit() or checkFraction(s_nums[1]))):                                                                                                                                                                                                                                                                                                                                                                                                                           
					# Delete the second number, and combine with the rest of the strings
					s_final=s_nums[0]+" "+" ".join(s_split[1:])
					L.append(s_final)
				else:
					L.append(str_complete)
			else:
				L.append(str_complete)
	df=pd.DataFrame(L,columns = ["Fixed Address"])
	#dataFrame['FixedAddress'] =df
	return df

'''
returns:  True if the given string is a fraction
		  Ex. 1/2 -> True
'''
def checkFraction(s):
	values = s.split('/')
	return len(values) == 2 and all(i.isdigit() for i in values)
	
