import pandas as pd
import scipy.stats
from math import log10

df = pd.read_spss("Birthweight_reduced_kg_SPSS.sav")
low_weight = df[df.lowbwt.eq('Low birthweight')]

def stats(database,filter):
    avg = round(database[filter].mean(),2)
    maximum=database[filter].max()
    minimum=database[filter].min()
    std_dev = database[filter].std()
    return avg, maximum, minimum, std_dev


#Q1-Mean father's age
print(f"The mean father's age is {stats(df,'fage')[0]}' years\n")

#Q2-What is the mean father’s age for low birthweight babies?
print(f"The mean father'sage for low birthweight babies is {stats(low_weight,'fage')[0]} years\n")

#Q3-Is father's age for low-weigth babies normally distributed?
shapiro_test = scipy.stats.shapiro(df['fage'])
if shapiro_test[1]>=0.05:
    print(f"Father's age is normally distributed, since the result for theShapiro-Wilk test is {round(shapiro_test[1],3)}\n")
else:
    print(f"Father's age is not normally distributed, since the result for theShapiro-Wilk test is {round(shapiro_test[1],3)}\n")

#Q4-If you apply the log transformation to the father's age, what is the mean score of the transformed variable?
log_fage=[]
for element in df['fage']:
    new_element=log10(element)
    log_fage.append(new_element)
df['log_fage']=log_fage
print(f"The mean of the log transformed father's age is'{stats(df, 'log_fage')[0]}\n")

#Q5. Is the above mean score a good representation of the real value? Justify your answer.
print("The above mean is not a good representation of the real value because when you transform the variable you change the values.")

#Q6. Is the new variable (log transform of father’s age) normally distributed? Justify your answer.
shapiro_test = scipy.stats.shapiro(df['log_fage'])
if shapiro_test[1]>=0.05:
    print(f"Log Father's age is normally distributed, since the result for theShapiro-Wilk test is {round(shapiro_test[1],3)}\n")
else:
    print(f"Log Father's age is not normally distributed, since the result for theShapiro-Wilk test is {round(shapiro_test[1],3)}\n")

#Q7. Is the variable “years father was in education” normally distributed?
shapiro_test = scipy.stats.shapiro(df['fedyrs'])
if shapiro_test[1]>=0.05:
    print(f"Father's years in education is normally distributed, since the result for theShapiro-Wilk test is {round(shapiro_test[1],3)}\n")
else:
    print(f"Father's years in education is not normally distributed, since the result for theShapiro-Wilk test is {round(shapiro_test[1],3)}\n")

#Q8. Mentioning the null and alternative hypotheses, explain the above answer.
print(f"The null hypotheses for the above case would be that “years father was in education” is normally distributed or that the sig. value in the Shapiro-Wilk test is larger than 0.05 whereas the alternative hypotheses would be that “years father was in education” is not normally distributed or that the sig. value in the Shapiro-Wilk test is smaller or equal to 0.05. Since the value of the sig. for this variable in the Shapiro- Wilk test is {shapiro_test[1]} the null hypotheses is rejected, therefore the alternative hypotheses is accepted.")

#Q9. What is the mean score for the variable “years father was in education” after you apply the Box-Cox transformation?
fedyrs=df['fedyrs']
bc_fedyrs = scipy.stats.boxcox(fedyrs)[0]
df['bc_fedyrs'] = bc_fedyrs
print(f"The mean of the Box-Cox transformed father's years in education is'{stats(df, 'bc_fedyrs')[0]}\n")

#Q10. Is this new variable normally distributed? Explain.