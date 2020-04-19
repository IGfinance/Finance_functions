import pandas as pd
import random as rd

def PushVariable(df, variable, min_value, max_value):
    df.loc[len(df)] = [variable, min_value, max_value]

def PushAllVariable(df, table_variables):
    for row in table_variables:
        PushVariable(df, row[0], row[1], row[2])

def GenerateRandomValues(df, number):
    name = []
    for k in range(len(df)):
        name.append(df.loc[k, 'Название'])
    df_new = pd.DataFrame(columns=name)
    for N in range(number):
        rand_stroka = []
        for i in range(len(df)):
            from_value = df.loc[i, 'Min']
            to_value = df.loc[i, 'Max']
            rand_value = rd.randint(from_value, to_value)
            rand_stroka.append(rand_value)
        df_new.loc[len(df_new)] = rand_stroka
    return df_new

def Generator(table_variables, length_data):
    columns = ['Название', 'Min', 'Max']
    df = pd.DataFrame(columns=columns)
    PushAllVariable(df, table_variables)
    print(df)
    df_new = GenerateRandomValues(df, length_data)
    print(df_new)

table_variables = [
    ['Revenue', 1000, 2000],
    ['COGS', 200, 400],
    ['OPEX', 250, 400],
    ['Taxes', 20, 40],
    ['Interest', 10, 20]
]
length_data = 100
Generator(table_variables, length_data)