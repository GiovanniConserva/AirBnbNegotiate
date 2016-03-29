import json
import pandas as pd

bucket = "days2_weeks1"
test= []
outputfile = "merged/"+ bucket+ "_result" + '.json'
test.append( pd.read_json('merging/'+bucket+ "_result"+'.json') )

count = 1

exit= False


while not exit:
	try:
		count= count+1
		suffix= "_" + str(count)
		print "suffix: "  + bucket+ "_result"+ suffix + '.json'
		test.append( pd.read_json('merging/'+bucket+ "_result"+ suffix + '.json') )		
	except:
		exit=True
n=0
for bunch in test:
	
	print "Bunch " + str(n)+  " \n \n"
	n=n+1 
	print bunch ['id']

result = pd.concat(test)
print result ['id']
result= result.loc[result['successfuls'] == True]
result= result.drop_duplicates(cols='id')

id_field= []
successfuls_field= []
reasons_field=[]
url_field=[]
for index,row in result.iterrows():
	id_field.append( row['id'] )
	successfuls_field.append (row['successfuls'])
	reasons_field.append(row['reasons'])
	#url_field.append(row['urls'])
#successfuls_field = result ['successfuls'][1]
#url_field= result['urls']
#reasons_field= result['reasons'][1]
print "************"
print id_field
#result.to_json(outputfile)	
res_df = pd.DataFrame({'id': id_field, 'successfuls': successfuls_field, 'reasons': reasons_field})
#res_df.index.name = 'id'

res_df.to_json(outputfile)

print "\n \nfinal result"
#res_df.sort_index()
#print res_df ['id']	
#print res_df.index
num= 0

	