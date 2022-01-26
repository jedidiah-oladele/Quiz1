import pandas

data = pandas.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding = "ISO-8859-1")
# print(data['Y2015'].std())
# print(data['Y2015'].mean())

# print(data['Y2016'].isnull().sum())
# print(data['Y2016'].isnull().sum()/len(data['Y2016']))

# col_1 = data['Element Code']
years = ['Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018']

# # correlation = []
# for year in years:
#     correlation.append(col_1.corr(year))

# print(max(correlation))

# print(len(data['Area'].value_counts()))

group = data.groupby('Element')
print(group['Y2017'].count()[7])

correlation = []
years = ['Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018']
for year in years:
    correlation.append(group[year].count()[7])

print(correlation)