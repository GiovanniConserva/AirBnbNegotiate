import json
import pandas as pd

total_buckets=[]
#total_retrieved= []


total_buckets.append("days1_weeks1")
#total_buckets.append("days1_weeks2") missing
total_buckets.append("days1_weeksM")
total_buckets.append("days2_weeks1")
total_buckets.append("days2_weeks2")
total_buckets.append("days2_weeksM")
total_buckets.append("days3_weeks1")
total_buckets.append("days3_weeks2")
total_buckets.append("days3_weeksM")
total_buckets.append("daysM_weeks1")
total_buckets.append("daysM_weeks2")
total_buckets.append("daysM_weeksM")

#total_retrieved.append("days2_weeks1")
total_processed= []

bucket_name=[]
availability= []
discount_obtained=[]
ids=[]
actions= []
nightly_prices_scraped=[]
responses= []
host_names= []
nightly_prices=[]
discount_asked= []



for item in total_buckets:
	#bucket_name=[]
	#availability= []
	#discount_obtained=[]
	temp_input= pd.read_json('buckets/'+item+ '.json')  
	temp_retrieved= pd.read_json('retrieved/'+item+ '_retrieved'+ '.json')  
	joined_data = pd.merge(temp_input,temp_retrieved,  how='inner',  left_on=['property_id'], right_on=['id']) 
	#for index,row in result.iterrows():
	for index,elem in joined_data.iterrows():
		bucket_name.append(item)
		availability.append(-1)
		discount_obtained.append(0)
		ids.append(elem['id'])
		actions.append(elem['actions'])
		responses.append(elem['responses'])
		nightly_prices.append(elem['nightly_price'])
		nightly_prices_scraped.append(elem['prices'])
		discount_asked.append(elem['discount_asked'])
		
	#print joined_data

res_df = pd.DataFrame({'id': ids, 'bucket_name': bucket_name, 'discount_asked':discount_asked,
'discount_obtained': discount_obtained, 'availability':availability, 'actions' :actions, 'response':responses,
'nightly_price':nightly_prices, 'nightly_price_scraped':nightly_prices_scraped })	
print res_df['discount_obtained']
res_df.to_csv("csv_merged/merged_retrieved_buckets.csv")
	
	
