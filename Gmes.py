#%%
import pandas as pd
from pandas.io.formats import style 
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

Games_sales_df= pd.read_csv('vgsales.csv',index_col='Rank')
# print(Games_sales_df)

#to convert values ad true or false
def split_multicolum(col_series):
    result_df = col_series.to_frame()
    options = []
    for idx,value in col_series[col_series.notnull()].iteritems():
        # Break each value into list of options
        for option in value.split(';'):
            # Add the option as a column to result
            if not option in result_df.columns:
                options.append(option)
                result_df[option] = False
            # Mark the value in the option column as True
            result_df.at[idx, option] = True
    return result_df[options]

top_15_Gn = Games_sales_df.name.value_counts().head(20) 
# print(Game_Name)
plt.figure(figsize=(12,6))
sns.barplot(x=top_15_Gn, y=top_15_Gn.index)
plt.title('top_15_Games_name')
# print(Games_sales_df)
#what is the top 15 platforms in games sales 
top_pltf = Games_sales_df.Platform.value_counts()
plt.figure(figsize=(12,6))
sns.barplot(x=top_pltf,y=top_pltf.index,color='g')
plt.title('Top_platforms')

#the puplisher of the games 
publishers = Games_sales_df.Publisher.value_counts().head(20) * 100 / Games_sales_df.Publisher.value_counts().head(20).sum()
# print(publishers.index)
plt.figure(figsize=(12,6))
plt.xticks(rotation=75)
sns.barplot(x=publishers,y=publishers.index)


#what is the gender of the highest games in sales 
top_15_Genre = Games_sales_df.Genre.value_counts() * 100 / Games_sales_df.Genre.value_counts().sum()
# print(top_15_Genre)
#barchart 
plt.figure(figsize=(12,6))
plt.pie(top_15_Genre,labels=top_15_Genre.index,autopct='%1.1f%%', startangle=180);

#show how na sales developed by years 
na_sales_20 = Games_sales_df.NA_Sales.head(20)
# print(na_sales_15)
years = Games_sales_df.Year.head(20)
plt.figure(figsize=(12,6))
sns.barplot(x=years,y=na_sales_20)
plt.title('Na_sales over the first 15 years')


# the top_15 sales globally
global_sales_15 = Games_sales_df.Global_Sales.head(20)
# print(global_sales)
plt.figure(figsize=(12,6))
sns.barplot(x=global_sales_15,y=Games_sales_df.name.head(20))

#comapring na with jp sales 
eu_sales = Games_sales_df.EU_Sales.head(20)
plt.figure(figsize=(12,6))
sns.scatterplot(x=eu_sales,y=na_sales_20,hue=years)

# comaprin all of the sales 
jp_sales = Games_sales_df.JP_Sales .head(20)
# print(jp_sales)
# print(na_sales_20)
plt.figure(figsize=(12,6))
plt.hist([eu_sales,jp_sales ,na_sales_20 ], 
        bins=np.arange(10, 100, 5), 
        stacked=True);
plt.legend(['EU_sales','Jp_sales','Na_sales']);        

# def plot_hbar(df, col, n, hover_data=[]):
#     fig = Games_sales_df.bar(df.sort_values(col).tail(n), 
#                  x=col, y="name", color='name',  
#                  text=col, orientation='h', width=700, hover_data=hover_data,
#                  color_discrete_sequence = Games_sales_df.colors.qualitative.Dark24)
#     fig.update_layout(title=col, xaxis_title="", yaxis_title="", 
#                       yaxis_categoryorder = 'total ascending',
#                       uniformtext_minsize=8, uniformtext_mode='hide')
#     fig.show()
# plot_hbar(top_15_Genre,'4',10)

#to make a tabel for all the datas 

Games_sales_df.head(15).sort_values('Rank', ascending= False).fillna(0).style.background_gradient(cmap='Reds',subset=["JP_Sales"])\
                     .background_gradient(cmap='Blues',subset=["Year"])\
                     .background_gradient(cmap='Greens',subset=['EU_Sales'])  




# Tb_vis.style.background_gradient(cmap='Reds',subset=['Genre'])        
# Tb_vis.style.background_gradient(cmap='Reds',subset=['Rank'])









#%%