#Shadi Taha
#02/1/2019
#CS3910 Spring 2019
#HWA 1: Data cleaning, reshaping and visualization in Excel & Python

import pandas as pd
import sqlite3

print('Starting...')


dirty_csv = str(input("Input the name of the CSV you want cleaned (Include .csv): ")) # Reads the csv file and places into a Dataframe
print('Dirty CSV name: '+dirty_csv)
df = pd.read_csv(dirty_csv) #reads dirty CSV into Dataframe


df = pd.melt(df, id_vars=['State']) #Reshapes Wide to Lang


df.columns = ['State','Type','Rate'] #Rename Column



df['Year'], df['Event'] = df['Type'].str.split(' ', 1).str #Splits the "2011 Divorce" into "Year" and "Event" columns



df = df.drop(['Type'], axis=1) #Drops the original un-split column



cols = df.columns.tolist() #Gets the column names and places into a list


reorderColumn = cols[:1] + cols[2:] + cols[1:2] #Re-order the list of columns to preferred order


df = df[reorderColumn] #Applies the column ordering to the dataframe

print('Successfully processed DataFrame from Wide to Long')
print('')

##### Create the new cleaned CSV File #####

#Ask user for the new CSV name they want.
new_csv_name = str(input("Enter a name for the new CSV (Include .csv): "))
print('CSV NAME: '+new_csv_name)
df.to_csv(new_csv_name, index=False)  #Creates the CSV
print('Created the CSV successfully.')


##### DATABASE #####
db_name = str(input("Enter a name for the new Database (Include .db): ")) # Ask user for name of Database they want.
print('Database name: '+db_name)


conn = sqlite3.connect(db_name) #Connection to database, create a cursor
cur = conn.cursor()


new_table_name = str(input("Enter a name for the table: ")) #Ask user for a table name, and creates it.
print('Table name: '+new_table_name)
df.to_sql(new_table_name, conn, if_exists='replace', index=False) #Dataframe -> SQL
print('Dataframe to SQL successful.')


print('Here are all the SQL rows below...') #Shows the user everything in the database


show_all_script = str("select * from %s;") % new_table_name #Creates the query to show all rows


cur.execute(show_all_script) #Executes the query


results = cur.fetchall() #Fetches the results and displays them
print(results)

print('All done, Thanks!')


conn.commit() #Commits and closes the connection
conn.close()