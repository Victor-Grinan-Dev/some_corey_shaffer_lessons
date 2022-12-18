import pandas as pd

file_data = 'survey_results_public.csv'
df = pd.read_csv(file_data, index_col='Respondent')  # index_col set the column label as the unique value to search
# definitions of questions of survey
schema_df = pd.read_csv('survey_results_schema.csv', index_col='Column')

print(df)

for column in df.columns:
    print(column)

## grab a labeled column
for index, data in enumerate(df['Hobbyist']):
    print(index, data)

# grab counts of labeled column different values
for index, data in enumerate(df['Hobbyist'].value_counts()):
    print(index, data)

# grab one person row of answers, one row all data
for index, data in enumerate(df.loc[0]):  # taking just the first line
    if index > 0:
        print('Question', index, data)

# slicing data
print(df.loc[0:2, 'Hobbyist'])  # NOTE: notice the 0:2 has no brackets while slicing

print(df.loc[0:2, 'Hobbyist':'Employment'])

# search by label: set the label as an index and use df.loc to find the data of that row.

schema_df.sort_index(inplace=False, ascending=False)
print(schema_df)

# 'ConvertedComp'
high_salaries = (df['ConvertedComp'] > 70000)
print(df.loc[high_salaries, ['ConvertedComp', 'LanguageWorkedWith']])

countries = ['United States', 'Canada']
filt = df['Country'].isin(countries)
print(df.loc[filt, 'Country'])

coding_lang = df['LanguageWorkedWith'].str.contains('Python', na=False)  # na represent unfilled cell
print(df.loc[coding_lang, 'LanguageWorkedWith'])

# sorting
df.sort_values(by=['Country', 'ConvertedComp'], ascending=[True, False], inplace=True)
print(df[['Country', 'ConvertedComp']].head(60))  # apparently is the mx number that will be shown  from a column

print(df['ConvertedComp'].nlargest(10))

print(df.nlargest(10, 'ConvertedComp'))

# grouping and aggregating
print(df['ConvertedComp'].head(15).median())
print(df['ConvertedComp'].median())
print(df.median())  # finds all the numerical values in dataframe and runs on them
print(df.describe())  # finds all the statistics values of numerical columns in the dataframe
print(df['ConvertedComp'].count())  # this count the filled cells
print(df['Hobbyist'].value_counts())  # counts the amount of answers sorted per possibilities
print(df['SocialMedia'].value_counts())
print(df['SocialMedia'].value_counts(normalize=True))  # returns the porcentage
print('\ngrouping')
print(df['Country'].value_counts())
country_group = df.groupby(['Country'])
print(country_group.get_group('United States'))  # gets the same response group all row

filt = df['Country'] == 'China'
print(df.loc[filt]['SocialMedia'].value_counts())

filt = df['Country'] == 'United States'
print(df.loc[filt]['SocialMedia'].value_counts().head(60))

print(country_group['SocialMedia'].value_counts().head(60))
print(country_group['SocialMedia'].value_counts(normalize=True).loc['India'])

print(country_group['ConvertedComp'].median().loc['Finland'])
