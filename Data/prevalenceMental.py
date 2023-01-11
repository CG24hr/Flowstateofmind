# line plot : alcohol use disorders in SEA
# bar chart : prevalence of mental disorders in United States (2019)
# scatter : prevalence of Schizophrenia around in selected countries

import pandas as pd

prevalence = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\prevalence-of-mental-diseases.csv')
print(prevalence)

# line plot : Drug use disorders in SEA

SEA = ['Myanmar', 'Cambodia', 'Indonesia', 'Malaysia', 'Philippines', 'Singapore', 'Thailand', 'Vietnam']


SEA_drug = prevalence[prevalence['Entity'].isin(SEA)]
SEA_drug = SEA_drug.loc[:, ['Entity', 'Year', 'Drug use disorders']]
print(SEA_drug)

Myanmar = SEA_drug[SEA_drug['Entity'] == 'Myanmar']
Cambodia = SEA_drug[SEA_drug['Entity'] == 'Cambodia']
Indonesia = SEA_drug[SEA_drug['Entity'] == 'Indonesia']
Malaysia = SEA_drug[SEA_drug['Entity'] == 'Malaysia']
Philippines = SEA_drug[SEA_drug['Entity'] == 'Philippines']
Singapore = SEA_drug[SEA_drug['Entity'] == 'Singapore']
Thailand = SEA_drug[SEA_drug['Entity'] == 'Thailand']
Vietnam = SEA_drug[SEA_drug['Entity'] == 'Vietnam']

import matplotlib.pyplot as plt
fig1 = plt.figure(figsize = (12,8))
plt.plot(Myanmar['Year'], Myanmar['Drug use disorders'], marker = 'o', label = 'Myanmar')
plt.plot(Cambodia['Year'], Cambodia['Drug use disorders'], marker = 'o', label = 'Cambodia')
plt.plot(Indonesia['Year'], Indonesia['Drug use disorders'], marker = 'o', label = 'Indonesia')
plt.plot(Malaysia['Year'], Malaysia['Drug use disorders'], marker = 'o', label = 'Malaysia')
plt.plot(Philippines['Year'], Philippines['Drug use disorders'], marker = 'o', label = 'Philippines')
plt.plot(Singapore['Year'], Singapore['Drug use disorders'], marker = 'o', label = 'Singapore')
plt.plot(Thailand['Year'], Thailand['Drug use disorders'], marker = 'o', label = 'Thailand')
plt.plot(Vietnam['Year'], Vietnam['Drug use disorders'], marker = 'o', label = 'Vietnam')
plt.title('Prevalence of Drug use disorders in SOUTH EAST ASIA')
plt.xlabel('Years')
plt.ylabel('Prevalence')
plt.legend()
plt.show()


# bar chart : prevalence of mental disorders in United States (2019)

USA = prevalence[(prevalence['Entity'] == 'United States') & (prevalence['Year'] == 2019)]
USA = USA.iloc[:, 3:]
print(USA)

import numpy as np
disorders = []
prevalence_USA_2019 = []
for i in USA.columns :
    disorders.append(i)
for i in USA.iloc[0, :] : 
    prevalence_USA_2019.append(i)

print(disorders)
print(prevalence_USA_2019)
disorders = np.array(disorders)
prevalence_USA_2019 = np.array(prevalence_USA_2019)
plt.bar(disorders, prevalence_USA_2019)
plt.title('Prevalence of Mental disorders in USA 2019')
plt.xlabel('Mental disorders')
plt.ylabel('Prevalence rate')
plt.show()


# scatter : prevalence of Schizophrenia around in SEA
prevalence_sex = pd.read_csv('D:\\Users\\Desktop\\Python code\\GitHub\\Flowstateofmind\\Data\\csv\\mental-disorders-prevalence-sex.csv')
prevalence_sex = prevalence_sex[(prevalence_sex['Male'] > 0 ) & (prevalence_sex['Female'] > 0 ) & (prevalence_sex['Population'] > 0) & (prevalence_sex['Entity'] != 'World' ) & (prevalence_sex['Entity'] != 'North America' )  ]
prevalence_sex = prevalence_sex[prevalence_sex['Year'] == 2017]
prevalence_sex = prevalence_sex.loc[:, ['Entity', 'Code', 'Year', 'Male', 'Female', 'Population']]
print(prevalence_sex)

Europe = ['Albania',    'Andorra',    'Armenia',    'Austria',    'Azerbaijan',    'Belarus',    'Belgium',    'Bosnia and Herzegovina',    'Bulgaria',    'Croatia',    'Cyprus',    'Czech Republic',    'Denmark',    'Estonia',    'Finland',    'France',    'Georgia',    'Germany',    'Greece',    'Hungary',    'Iceland',    'Ireland',    'Italy',    'Kazakhstan',    'Kosovo',    'Latvia',    'Liechtenstein',    'Lithuania',    'Luxembourg',    'Macedonia',    'Malta',    'Moldova',    'Monaco',    'Montenegro',    'Netherlands',    'Norway',    'Poland',    'Portugal',    'Romania',    'Russia',    'San Marino',    'Serbia',    'Slovakia',    'Slovenia',    'Spain',    'Sweden',    'Switzerland',    'Turkey',    'Ukraine',    'United Kingdom',    'Vatican City']
Asia = [
        'Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China',
        'Cyprus', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan',
        'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea',
        'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Russia', 'Saudi Arabia', 'Singapore', 'South Korea',
        'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkey', 'Turkmenistan', 'United Arab Emirates',
        'Uzbekistan', 'Vietnam', 'Yemen'
        ]       
Africa = [
    'Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde', 'Central African Republic', 'Chad',
    'Comoros', 'Democratic Republic of the Congo', 'Republic of the Congo', 'Ivory Coast', 'Djibouti', 'Egypt', 'Equatorial Guinea',
    'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia',
    'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria',
    'Rwanda', 'São Tomé and Príncipe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan',
    'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe'
]
North = [
    'Antigua and Barbuda', 'The Bahamas', 'Barbados', 'Belize', 'Canada', 'Costa Rica', 'Cuba', 'Dominica',
    'Dominican Republic', 'El Salvador', 'Grenada', 'Guatemala', 'Haiti', 'Honduras', 'Jamaica', 'Mexico',
    'Nicaragua', 'Panama', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Trinidad and Tobago',
    'United States'
]

South = [
    'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru',
    'Suriname', 'Uruguay', 'Venezuela'
]

Australia = [
    'Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia', 'Nauru', 'New Zealand', 'Palau',
    'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu'
]



prevalence_sex['Population'] = prevalence_sex['Population'].apply(lambda x : round(x / 1000000))
print(prevalence_sex.sort_values('Population', ascending = False))


colors_world =  []
for index, rows in prevalence_sex.iterrows() : 
    if rows['Entity'] in Europe :
        colors_world.append('pink')
    elif rows['Entity'] in Asia  :
        colors_world.append('indigo')
    elif rows['Entity'] in Africa  :
        colors_world.append('red')
    elif rows['Entity'] in North  :
        colors_world.append('darkcyan')
    elif rows['Entity'] in South  :
        colors_world.append('orange')
    elif rows['Entity'] in Australia  :
        colors_world.append('green')
    else :
        colors_world.append('brown')



plt.scatter(prevalence_sex['Male'], prevalence_sex['Female'], alpha = 0.5, c = colors_world, s = prevalence_sex['Population']*4, label = prevalence_sex['Code'])
plt.title('Prevalence of Mental disorders around the world 2017')
plt.xlabel('Male(%)')
plt.ylabel('Female(%)')
plt.show()