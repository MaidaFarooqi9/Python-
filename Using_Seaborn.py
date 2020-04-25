
import matplotlib.pyplot as plt
import seaborn as sns


#x=list(range(0,10))
#y=list(range(-10,0))
#plt.plot(x,y)
#plt.show()

#a=[0,-100,25,67,-323]
#b=[0,3,7,3,9]
#plt.plot(a,b)
#plt.show()


c=[-100,0,100,120]
d=[1,3,5,9]
#plt.plot(c,d,'ro') #red dots
#plt.show()

#plt.plot([1,3,5,6],[4,5,6,8],'g^') #green triangle
#plt.show()





                                 #SEABORN
seabornData=sns.load_dataset('planets') #tips,planets is the buil-in data set in seaborn
print(seabornData.head()) #to print data
#plt.show(sns.distplot(seabornData['orbital_period'],bins=10))

# #bins value is if less then broader graph appear
#distplot(like histogram) show along with kde ,you can set its value to false to remove


                         #joinplot
                         #best for large dataset

#plt.show(sns.jointplot(x='orbital_period',y='mass',data=seabornData)) #scatter dots
#plt.show(sns.jointplot(x='orbital_period',y='mass',data=seabornData,kind='hex',color='red')) #hex like honeycomb structure
#plt.show(sns.jointplot(x='mass',y='distance',data=seabornData,kind='kde'))


                            #pairplot
#plt.show(sns.pairplot(seabornData,palette='coolwarm'))#it takes time in loading if data is large
seabornData2=sns.load_dataset('tips')
print(seabornData2.head())


#plt.show(sns.pairplot(seabornData2,hue='tip',palette='coolwarm'))

                          #rugplot
#plt.show(sns.rugplot(seabornData['mass']))

                           #CategoricalPlot

                           #countplot
#plt.show(sns.barplot(x='sex',y='size',data=seabornData2))#notworking

#plt.show(sns.countplot(x='sex',data=seabornData2)) #same as barplot,y-axis counts number of occurences

#plt.show(sns.countplot(x='year',data=seabornData))

                           #Boxplot
#plt.show(sns.boxplot(x='day',y='total_bill',hue='smoker'data=seabornData2,palette='cool')) #it shows quartiles,outliers
#plt.show(sns.boxplot(x='method',y='year',data=seabornData,palette='pastel'))

                           #violinplot
#plt.show(sns.violinplot(x='method', y='year', data=seabornData, palette='pastel'))#violin,boxplot shows separate graphs for each category like one for smokers and other for non-smokers
#plt.show(sns.violinplot(x='day',y='total_bill',hue='smoker',split=True,data=seabornData2,palette='cool')) #split shows 1figure instead of 2


                            #StripPlot
#plt.show(sns.stripplot(x='method', y='year', data=seabornData, palette='pastel'))
#plt.show(sns.stripplot(x='day',y='total_bill',hue='smoker',data=seabornData2,palette='cool'))
#plt.show(sns.stripplot(x='day',y='total_bill',hue='smoker',split=True,data=seabornData2,palette='cool'))

                            #SwarmPlot
#plt.show(sns.swarmplot(x='day', y='total_bill', data=seabornData2, palette='cool'))
#combination of violin and stripplot

                           #FactorPlot
                           #it is the most preferable plot

#plt.show(sns.factorplot(x='day',y='total_bill',hue='sex',kind='violin',data=seabornData2,palette='cool'))


                          #MatrixPlots

#plt.show(sns.heatmap(seabornData.corr(),annot=True,cmap='coolwarm'))#it shows data in matrix form ,relation of each col with row's element by indicating different colors,annot shows the value range of colors

#you can add linewidth and linecolor to have a clear view

#plt.show(sns.heatmap(seabornData.corr(),annot=True,linecolor='white',linewidths=3,cmap='coolwarm'))


                          #GridPlot
#g=sns.PairGrid(seabornData,palette='coolwarm')
      #arrangement must be the same as below
#g.map_diag(sns.distplot )
#g.map_upper(plt.scatter)
#g.map_lower(sns.kdeplot)
#plt.show()

                      #FacetGrid
           #it shows written values of smoker(yes,no) and time(lunch,dinner)
#grid=sns.FacetGrid(data=seabornData2,col='time',row='smoker')
#grid.map(sns.distplot,'total_bill')
#plt.show()



                         #RegressionPlots
                         #notworking
#plt.show(sns.lmplot(x='mass',y='distance',data=seabornData))
#plt.show(sns.lmplot(x='total_bill',y='tip',data=seabornData2))



