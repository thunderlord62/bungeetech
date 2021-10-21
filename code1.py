import pandas as pd
filename='C:/Users/1/Desktop/bungeetech/input/question-1/main.csv'
fields = []
rows = []
data = pd.read_csv(filename)
grp = data.groupby((data['Year'] // 10) * 10)
q= ({"Population": "max", "Violent": "sum", "Property": "sum", "Murder": "sum", "Forcible_Rape": "sum", "Robbery": "sum",
 "Aggravated_assault": "sum", "Burglary": "sum", "Larceny_Theft": "sum", "Vehicle_Theft": "sum"})
data = grp.aggregate(q)
print(data)
