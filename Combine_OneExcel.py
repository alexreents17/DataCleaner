#!/usr/bin/python
'''
This function combines all the worksheets
'''
def Combine_OneExcel(file):
	xls=pd.ExcelFile(file)
	sheetnames=xls.sheet_names
	dataFrames=[]
	for name in sheetnames:
		dataFrames.append(pd.read_excel(xls,name))
	df_final=pd.concat(dataFrames,sort=False)
	return df_final
	