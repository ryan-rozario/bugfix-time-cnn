import csv
import requests
import logging

f=open('2015.csv')
data=f.readlines()
data.pop(0)
total=len(data)
logging.basicConfig(filename="logfile.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
success,failure=0,0

push_data=["ID","who","when","field_name","added","removed"]


for i in range(len(data)):
	temp=list(data[i].split(','))
	ID=temp[0]
	print("requesting",ID)
	r=requests.get("https://bugzilla.mozilla.org/rest/bug/"+str(ID)+"/history")
	print("acquired",ID)
	json=r.json()
	fname="data/"+str(ID)+".csv"
	with open(fname,'w',newline='') as file:
		writer=csv.writer(file)
		writer.writerow(push_data)
		try:
			base=json['bugs']
			for j in range(len(base)):
				base2=base[j]['history']
				for k in range(len(base2)):
					base3=base2[k]
					var_who=base3['who']
					var_when=base3['when']
					base3=base2[k]['changes']
					for l in range(len(base3)):
						base4=base3[l]
						var_fieldname=base4['field_name']
						var_removed=base4['removed']
						var_added=base4['added']
						temp2=[ID,var_who,var_when,var_fieldname,var_added,var_removed]
						writer.writerow(temp2)
			logger.info("DONE: "+str(ID)+" written successfuly")
			print(str(ID)+" written successfuly")
			success+=1
			print()
			

		except Exception as e:
			logger.error("ERROR:"+str(ID))
			logger.error(e)
			print("ERROR ",ID,"see logfile for more info")
			failure+=1
			print()
		
	print(success,failure,total)
	print()
	print('-----------------------')



	

	


 