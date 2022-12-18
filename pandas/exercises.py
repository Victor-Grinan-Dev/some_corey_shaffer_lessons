import pandas as pd

# each column/key is a serie.


# dictionarie
people = {
    "first": ['victor', 'annu', 'jorge', ],
    "last": ['grinan', 'grinan', 'machete'],
    "email": ['victor.grinan@gmail.com', 'annu.grinan@gmail.com', 'jorge.machete@gmail.com']
}
df = pd.DataFrame(people)

# def dict_df(dictionarie):
#     data = pd.DataFrame(dictionarie)
#     # print(data, '\n')
#     return data
#
#
# def schema_csv(schema_df):
#     pd.set_option('display.max_rows', 85)
#     print(schema_df)
#
#
# def data_frame_as_it_is(df):
#     """in console you can't have visual access to all the data frame"""
#     print(df)
#
#
# def my_shape(df):
#     # print(df.shape)  # number of rows and columns
#     rows = df.shape[0]
#     columns = df.shape[1]
#
#     return rows, columns
#
#
# def set_view_options(df, rows, col):
#     if col is None:
#         col = my_shape(df)[1]
#     pd.set_option('display.max_rows', rows)
#     return pd.set_option('display.max_columns', col)
#
#
# def first_x_rows(df, rows, col=None):
#     set_view_options(df, rows, col)
#     print(df.head(rows))
#
#
# def last_x_rows(df, rows, col=None):  # x are rows
#     set_view_options(df, rows, col)
#     print(df.tail(rows))
#
#
# def pick_column_s(data_frame, list_of_col_name):
#     """returns a list of elements of the given column
#     list_of_col_name can be a list of str with the names of the columns
#     """
#
#     # print(data_frame[list_of_col_name], '\n')
#     return data_frame[list_of_col_name]
#
#
# # x = dict_df(people)
# # pick_column_s(x, ['first', 'last'])
#
# def pick_row(data_frame, row_name):  # NOT WORKING
#     """returns a list of elements of the given row"""
#     print(data_frame[row_name], '\n')
#     return data_frame[row_name]
#
#
# def find_columns_and_col_names(data_frame):
#     """takes the data frame as argument
#     returns a tuple with list of the columns names and int lenth
#     """
#     print(data_frame.columns)
#     col_names = []
#     for item in data_frame.columns:
#         col_names.append(item)
#     return col_names, len(col_names)
#
#
# # x = dict_df(people)
# # print(find_columns_and_col_names(x))
#
#
# # select a row by index location ILOC
#
# def find_data_in_row(data_frame, list_of_index=None, index_or_label_colums=None):
#     """index can be a list of integers"""
#     row_data = []
#     if list_of_index and not index_or_label_colums:
#         print(data_frame.iloc[list_of_index])
#         return data_frame.iloc[list_of_index]  # there is something wrong with this returns
#
#     if index_or_label_colums is str and list_of_index:
#         print(data_frame.loc[list_of_index, index_or_label_colums])
#
#     elif list_of_index and index_or_label_colums:
#         print(data_frame.iloc[list_of_index, index_or_label_colums])
#         return data_frame.iloc[list_of_index, index_or_label_colums]  # there is something wrong with this return
#
#     # TODO: add each info in data list and return it... maybe a generator?
#     return row_data
#
#
# x_df = dict_df(people)  # turn the dictionary in to dataframe
#
#
# # print(x_df.iloc[0])
# # x = find_data_in_row(x_df, [1, 2], 1)
# # print(find_data_in_row_index(x))
#
# # set a labeled column as the index.
# def set_index_to_labeled_column(df, col_name):
#     """takes the default int as index ou and replace it for labeled col_namestr"""
#     df.set_index(col_name, inplace=True)  # inplace == True will change the actual df to this index reference
#     print(df)
#
#
# def reset_index_to_labeled_column(df):
#     df.reset_index(inplace=True)  # to reset the mistakes
#     print(df)
#
#
# # set_index_to_labeled_column(x_df, 'email')
#
# # FILTERING # comparisson!!!
# df = dict_df(people)
# # filter is equal to data frame's column 'last' if last iquals 'Doe'
# filt = (df['last'] == 'grinan')
# print(filt)
# # print data frame where filt is true
# print(df[filt])
# # this gives the same result:
# print(df.loc[filt])
# # but ths way yo can pass more values to filter the data
# print(df.loc[filt, 'email'])
#
# # the shortcut is:
# print(df[df['last'] == 'grinan'])
#
# # and = &
# # or = |
# # variable = (data_frame ['column1'] == 'name') and (data_frame ['column2'] == 'name2')
# # print(data_frame.loc[variable, 'third_column_name']
#
# filt = (df['last'] == 'grinan') & (df['first'] == 'annu')
# print(df.loc[filt, 'email'])
#
# # if you want to negate the filter and recive the oposite of what you are searching use ~
# # print(df.loc[~filt, 'email'])
#
# # ALTERING # updating!!!
# # updating column labels
# print('\nprinting the columns labels')
# print(df.columns)
# print('\nalter the labels of the columns')
# df.columns = ['first_name', 'last_name', 'email']
# print(df.columns)
# print('\nusing list comprehensions')
# df.columns = [x.upper() for x in df.columns]
# print(df.columns)
#
# df.columns = [x.capitalize() for x in df.columns]
# print(df.columns)
# df.columns = df.columns.str.replace('_', ' ')
# print(df.columns)
# df.columns = df.columns.str.replace(' ', '_')
# df.columns = [x.lower() for x in df.columns]
# print(df.columns)
#
# # changing individual columns
# df.rename(columns={'first_name': 'first', 'last_name': 'last'}, inplace=True)
# print(df.columns)
#
# # update values in the data
# # single value
# print(df.loc[2])
# df.loc[2] = ['george', 'smith', 'george.smith@gmail.com']
# print(df.loc[2])
# # specify the columns and rows
# df.loc[2, ['last', 'email']] = ['machete', 'george.machete@gmail.com']
# print(df.loc[2])
#
# df.at[2, 'first'] = 'jorge'  # at is a way to locate data with single value only
# filt = (df['email'] == 'george.machete@gmail.com')
# df.loc[filt, 'email'] = 'jorge.machete@gmail.com'
#
# # many data changes
# df['email'] = df['email'].str.upper()
# print(df)
#
# # 4 methods to change many datas
# # apply: used for calling func on our values. for data frames or series obj
# # on a series:
# print('\napply()')
#
#
# # print(df['email'].apply(len))
#
#
# def lower_case(email):
#     return email.lower()
#
#
# def upper_case(email):
#     return email.upper()
#
#
# df['email'] = df['email'].apply(lower_case)
# print(df)
#
# df['first'] = df['first'].apply(lambda x: x.capitalize())
# df['email'] = df['email'].apply(upper_case)
# print(df)
# print('''\ncase df['email'].apply(len):''')
# print(df['email'].apply(len))
# print('''\ncase len(df['email']):''')
# print(len(df['email']))
# print('''\ncase df.apply(len):''')
# print(df.apply(len))  # this doesnt map all the datas but just the items in the frame
# print('''\ncase df.apply(len, axis='columns'):''')
# print(df.apply(len, axis='columns'))
#
# # APPLYMAP: this only works on data frames no series objects
# print('''\nAPPLYMAP()''')
# print('''\nexample 1''')
# print(df.applymap(len))
#
# print('''\nexample 2''')
# print(df.applymap(str.lower))  # if you have numerial values you will have error
#
# # MAP
# print('''\nmap()''')
# print(df['first'].map({'victor': 'javier', 'annu': 'liina maria'}))  # the values that are not specified are converted
# # into NaN (none)
#
# # replace
# print('''\nreplace()''')
# print(df['first'].replace({'victor': 'javier', 'annu': 'liina maria'}))
#
# # rename
# print('''\nrename column label''')
# df.rename(columns={"email": "mail"}, inplace=False)


# add remove columns from data frame
# add
# print('\nadd a column')
# df['full_name'] = df['first'] + ' ' + df['last']
# print(df)
#
# # delete columns
# print('\ndelete a column')
# df.drop(columns=['first', 'last'], inplace=True)
# print(df)
#
# # split a column data:
# print('\nsplit a columns information')
# print(df['full_name'].str.split(' '))
# print('\nasign splited information to diferent columns')
# print(df['full_name'].str.split(' ', expand=True))
# print('\nadd two columns out of one ')
# df[['first', 'last']] = df['full_name'].str.split(' ', expand=True)
# print(df)
# print('\nappend a columns')
# df = df.append({'first': 'Tony'}, ignore_index=True)
# print(df)


# people2 = {
#     "first": ['yohakner', 'charlie'],
#     "last": ['el yoyo', 'bocaccio'],
#     "email": ['layoyamenta@gmail.com', 'bocadejaruco@gmail.com']
# }
#
# df2 = pd.DataFrame(people2)
# print(df2)
# print('\nappend a columns')
# df = df.append(df2, ignore_index=True, sort=False)
# print(df)
#
# print('\nerasing a row')  # should be always treated by the index
# # df.drop(index=4, inplace=True)# exaple 1, not the best practice
# # print(df)
#
# filt = df['last'] == 'bocaccio'
# df = df.drop(index=df[filt].index)
# print(df)
# print('\nsorting')
# print(df.sort_values(by='last'))
# print(df.sort_values(by='last', ascending=False))
# print(df.sort_values(by=['last', 'first'], ascending=False))  # if last is duplicated
# print(df.sort_values(by=['last', 'first'], ascending=[False, True]))
#
# print(df['last'].sort_values())

# grouping and aggregating

## heavy exercises
# Inputs
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
print(mylist)
myarr = np.arange(26)
print(myarr)
mydict = dict(zip(mylist, myarr,))
print(mydict)


# Solution
ser1 = pd.Series(mylist)
print(ser1)
ser2 = pd.Series(myarr)
print(ser2)
ser3 = pd.Series(mydict)
print(ser3)
print(ser3.head())