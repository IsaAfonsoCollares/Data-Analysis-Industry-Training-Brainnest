import pandas as pd
import scipy.stats


df = pd.read_spss("Birthweight_reduced_kg_SPSS.sav")
smoker_df = df[df.smoker.eq('Smoker')]
non_smoker_df = df[df.smoker.eq('Non-smoker')]

def smoker(filter):
    avg = round(smoker_df[filter].mean(),2)
    maximum=smoker_df[filter].max()
    minimum=smoker_df[filter].min()
    std_dev = smoker_df[filter].std()
    return avg, maximum, minimum, std_dev

def non_smoker(filter):
    avg = round(non_smoker_df[filter].mean(),2)
    maximum=non_smoker_df[filter].max()
    minimum=non_smoker_df[filter].min()
    std_dev=non_smoker_df[filter].std()
    return avg, maximum, minimum, std_dev


#Q1 - Mean birthweight for babies of non-smoking mothers
print(f"A1 - The mean birthweight for babies non-smoking mothers is {non_smoker('Birthweight')[0]}kg\n")

#Q2 - Mean birthweight for babies of smoking mothers
print(f"A2 - The mean birthweight for babies of smoking mothers is {smoker('Birthweight')[0]}kg\n")

#Q3 - Mean head circumference of non-smoking mothers
print(f"A3 - The mean head circumference for babies of non-smoking mothers is {non_smoker('Headcirc')[0]}cm\n")

#Q4. Mean gestational age at birth for babies of smoking mothers
print(f"A4 -The mean gestational age at birth for babies of smoking mothers is {smoker('Gestation')[0]} weeks\n")

#Q5. Maximum head circumference for babies of non-smoking mothers
print(f"A5 - The maximum head circumference for babies of non-smoking mothers is {non_smoker('Headcirc')[1]}cm.")

#Q6. What is the minimum gestational age at birth for babies of smoking mothers?
print(f"A6 - The minimum gestational age at birth for babies of smoking mothers is {smoker('Gestation')[2]} weeks.")

#Q7. Based on the dataset you have, out of the two, which one would be a better bet:
#	Pregnancy period in smoking mothers is shorter
#	Pregnancy period in non-smoking mothers is shorter
if smoker('Gestation')[0]>non_smoker('Gestation')[0]:
    print("Pregnancy period in non-smoking mothers is shorter")
elif smoker('Gestation')[0]<non_smoker('Gestation')[0]:
    print("Pregnancy period in smoking mothers is shorter")
else:
    print("Pregnancy period is similar in ")
#Q8. Justify the above choice in a few words.
print("The mean gestational age of birth for babies of smoking mothers is smaller than the mean gestational age of non-smoking mothers.")

#Q9. What is the baby birth weight range for babies of smoking mothers?
range_smoker = round((smoker('Birthweight')[1]-smoker('Birthweight')[2]),2)
print(f"The baby birthweight range for babies of smoking mothers is {range_smoker}")

#Q10. In your own words describe what the value of the above range for baby's birthweight tells us about smoking versus non-smoking mothers?
range_non_smoker = round((non_smoker('Birthweight')[1]-non_smoker('Birthweight')[2]),2)
if range_non_smoker<range_smoker:
    print("The baby’s birthweight of smoking mothers varies more than the one’s of non-smoking mothers.")
elif range_non_smoker>range_smoker:
    print("The baby’s birthweight of non smoking mothers varies more than the one’s of smoking mothers.")
else:
    print("Both varies in the same way.")

#Q11. Are head circumference data for babies of smoking mothers normally distributed?
shapiro_test = scipy.stats.shapiro(smoker_df['Headcirc'])
print("The head circumference data for babies of smoking mothers is normally distributed, as can be seen from the result of the Shapiro-Wilk test being larger than 0.05")

#Q12. What is the significance value for the above on the Shapiro-Wilk test?
print(f"The p value for the test above is {round((shapiro_test[1]),3)}")

#Q13. What is the standard score (Z-score) for head circumference of 35.05 (X=35.05) in non-smoking mothers?
z_score=round (35.05-non_smoker('Headcirc')[0])/non_smoker('Headcirc')[3]
print(f"The Z-score = {z_score}")

#Q14. How are birth weight data of non-smoking mothers skewed?
skweness = round(non_smoker_df['Birthweight'].skew(),2)
print(f"The skweness is equal to {skweness}")
#It is positively skewed and approximately symmetric.

#Q15. Are birth weight data for babies of smoking mothers normally distributed?
shapiro_test = scipy.stats.shapiro(smoker_df['Birthweight'])
print("The head circumference data for babies of smoking mothers is normally distributed, as can be seen from the result of the Shapiro-Wilk test being larger than 0.05")
#Yes , they are.
#Q16. What is the significance value for the above on the Shapiro-Wilk test?
print(f"The p value for the test above is {round((shapiro_test[1]),3)}")
#It is 0.949.

#Q17. Based on the dataset you have, how confident can you be in saying that a baby's birth weight will be +/- 1 standard deviation from the mean?
print("68.2%. Since the birth weight is normally distributed +/-1 standart devitiation falls within the 68.2% confidence threshold.")

#Q18. Based on the dataset you have, what is the probability that the birth weight for a baby of a smoking mother will be less than 4.2 kg?
z_score=round (4.2-smoker('Birthweight')[0])/smoker('Birthweight')[3]
p = round(scipy.stats.norm.sf(abs(z_score)),4)
print(f"The probability that the birth weight for a baby of a smoking mother will be less than 4.2k is {p*100}%")
#Z=(x-μ)/σ =(4.2-3.14)/0.63 =1.06/0.63 =1.68
#P(Z≤1.68)≅0.9535

  
#Q19. Are data for length of baby of non-smoking mothers normally distributed?
shapiro_test = scipy.stats.shapiro(non_smoker_df['Length'])
print("The length data for babies of non-smoking mothers is normally distributed, as can be seen from the result of the Shapiro-Wilk test being larger than 0.05")
#Yes, they are.
  
#Q20. What is the significance value for the above on the Shapiro-Wilk test?
#It is 0.07
print(f"The p value for the test above is {round((shapiro_test[1]),3)}")

#Q21. What is the standard score for the length of a baby of 48.5cm for non-smoking mothers?
z_score=round (48.5-non_smoker('Length')[0])/non_smoker('Length')[3]
print(z_score)
#Z=(x-μ)/σ=(48.5-51.8)/3.25=(-3.3)/3.25  =-1.02
  
#Q22. Based on the dataset you have, what is the probability that the length of baby for non-smoking #mothers will be more than 55 cm?
z_score=round (55-non_smoker('Length')[0])/non_smoker('Length')[3]
p = round(scipy.stats.norm.sf(abs(z_score)),4)
print(f"{(1-p)*100}%")
#Z=(x-μ)/σ=(55-51.8)/3.25=3.2/3.25  =0.98
#(Z>0.98)=1-P(Z≤0.98)=1-0.8365=0.1635