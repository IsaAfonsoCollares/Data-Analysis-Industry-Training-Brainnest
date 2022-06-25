import pandas as pd

df = pd.read_spss("Birthweight_reduced_kg_SPSS.sav")

def smoker(filter):
    filtered_df = df[df.smoker.eq('Smoker')]
    avg = round(filtered_df[filter].mean(),2)
    maximum=filtered_df[filter].max()
    minimum=filtered_df[filter].min()
    return avg, maximum, minimum

def non_smoker(filter):
    filtered_df = df[df.smoker.eq('Non-smoker')]
    avg = round(filtered_df[filter].mean(),2)
    maximum=filtered_df[filter].max()
    minimum=filtered_df[filter].min()
    return avg, maximum, minimum


#Q1 - Mean birthweight for babies of non-smoking mothers
print(f"A1 - The mean birthweight for babies non-smoking mothers is {non_smoker('Birthweight')[0]}kg\n")

#Q2 - Mean birthweight for babies of smoking mothers
print(f"A2 - The mean birthweight for babies of smoking mothers is {smoker('Birthweight')[0]}kg\n")

#Q3 - Mean head circumference of non-smoking mothers
print(f"A3 - The mean head circumference for babies of non-smoking mothers is {non_smoker('Headcirc')[0]}cm\n")

#Q4. Mean gestational age at birth for babies of smoking mothers
print(f"A4 -The mean gestational age at birth for babies of smoking mothers is {smoker('Gestation')[0]} weeks\n")

#Q5. Maximum head circumference for babies of non-smoking mothers
print(f"A5 - The maximum head circumference for babies of non-smoking mothers is {non_smoker('Headcirc')[1]}")
#Q6. What is the minimum gestational age at birth for babies of smoking mothers?
#It is 33 weeks
#Q7. Based on the dataset you have, out of the two, which one would be a better bet:
#	Pregnancy period in smoking mothers is shorter
#	Pregnancy period in non-smoking mothers is shorter
#The better bet would be that pregnancy period in smoking mothers is shorter.
#Q8. Justify the above choice in a few words.
#The mean gestational age of birth for babies of smoking mothers is smaller than the mean gestational age of non-smoking mothers.
#Q9. What is the baby birth weight range for babies of smoking mothers?
#It is 2.65 kg.
#Q10. In your own words describe what the value of the above range for baby's birthweight tells us about smoking versus non-smoking mothers?
#It tells us that the baby’s birthweight of smoking mothers varies more than the one’s of non-smoking mothers.
#Q11. Are head circumference data for babies of smoking mothers normally distributed?
#Yes, they are.
#Q12. What is the significance value for the above on the Shapiro-Wilk test?
#It is 0.372.
#Q13. What is the standard score (Z-score) for head circumference of 35.05 (X=35.05) in non-smoking mothers?
#It is 0 because x=mean as you can also see from the formula below:
#Z=(x-μ)/σ=(35.05-35.05)/2.08=0/2.08=0
#Q14. How are birth weight data of non-smoking mothers skewed?
#It is positively skewed and approximately symmetric.
#Q15. Are birth weight data for babies of smoking mothers normally distributed?
#Yes , they are.
#Q16. What is the significance value for the above on the Shapiro-Wilk test?
#It is 0.949.
#Q17. Based on the dataset you have, how confident can you be in saying that a baby's birth weight will be +/- 1 standard deviation from the mean?
#68.2%.
#Q18. Based on the dataset you have, what is the probability that the birth weight for a baby of a smoking mother will be less than 4.2 kg?
#Z=(x-μ)/σ =(4.2-3.14)/0.63 =1.06/0.63 =1.68
#P(Z≤1.68)≅0.9535

  
#Q19. Are data for length of baby of non-smoking mothers normally distributed?
#Yes, they are.
  
#Q20. What is the significance value for the above on the Shapiro-Wilk test?
#It is 0.07
  
#Q21. What is the standard score for the length of a baby of 48.5cm for non-smoking mothers?
#Z=(x-μ)/σ=(48.5-51.8)/3.25=(-3.3)/3.25  =-1.02
  
#Q22. Based on the dataset you have, what is the probability that the length of baby for non-smoking #mothers will be more than 55 cm?
#Z=(x-μ)/σ=(55-51.8)/3.25=3.2/3.25  =0.98
#(Z>0.98)=1-P(Z≤0.98)=1-0.8365=0.1635