Project for the fisrt week of the Data Anaysis Industry Training from Brainnest 

Purpose:Analyse a dataset with data about babies of smoking and non-smoking mothers
  
Development:  
  
Using Pandas and Scypy Stats packages the dataset was analyzed to find descriptive statistics variables, such as mean, range, and standard deviation, the Shapiro-Wilk test was applied to some of the variables to test if the distribution was normal, z-scores and probability for specific values were also calculated.
      
The questions that needed to be answered are listed bellow as well as the answers to each one.
Q1. What is the mean birth weight for babies of non-smoking mothers?
The mean is 3.51 Kg.
  
Q2. What is the mean birth weight for babies of smoking mothers?
The mean is 3.13 kg.
  
Q3. What is the mean head circumference for babies of non-smoking mothers? 
The mean is 35.05 cm.
  
Q4. What is the mean gestational age at birth for babies of smoking mothers? 
The mean is 38.95 weeks.
  
Q5. What is the maximum head circumference for babies of non-smoking mothers?
It is 39 cm
  
Q6. What is the minimum gestational age at birth for babies of smoking mothers?
It is 33 weeks
  
Q7. Based on the dataset you have, out of the two, which one would be a better bet:
	Pregnancy period in smoking mothers is shorter
	Pregnancy period in non-smoking mothers is shorter
The better bet would be that pregnancy period in smoking mothers is shorter.
  
Q8. Justify the above choice in a few words.
The mean gestational age of birth for babies of smoking mothers is smaller than the mean gestational age of non-smoking mothers.
  
Q9. What is the baby birth weight range for babies of smoking mothers?
It is 2.65 kg.
  
Q10. In your own words describe what the value of the above range for baby's birthweight tells us about smoking versus non-smoking mothers?
It tells us that the baby’s birthweight of smoking mothers varies more than the one’s of non-smoking mothers.
  
Q11. Are head circumference data for babies of smoking mothers normally distributed?
Yes, they are.
  
Q12. What is the significance value for the above on the Shapiro-Wilk test?
It is 0.372.
  
Q13. What is the standard score (Z-score) for head circumference of 35.05 (X=35.05) in non-smoking mothers?
It is 0 because x=mean as you can also see from the formula below:
Z=(x-μ)/σ=(35.05-35.05)/2.08=0/2.08=0
  
Q14. How are birth weight data of non-smoking mothers skewed?
It is positively skewed and approximately symmetric.
  
Q15. Are birth weight data for babies of smoking mothers normally distributed?
Yes , they are.
  
Q16. What is the significance value for the above on the Shapiro-Wilk test?
It is 0.949.
  
Q17. Based on the dataset you have, how confident can you be in saying that a baby's birth weight will be +/- 1 standard deviation from the mean?
68.2%.
  
Q18. Based on the dataset you have, what is the probability that the birth weight for a baby of a smoking mother will be less than 4.2 kg?
Z=(x-μ)/σ =(4.2-3.14)/0.63 =1.06/0.63 =1.68
P(Z≤1.68)≅0.9535
  
Q19. Are data for length of baby of non-smoking mothers normally distributed?
Yes, they are.
  
Q20. What is the significance value for the above on the Shapiro-Wilk test?
It is 0.07
  
Q21. What is the standard score for the length of a baby of 48.5cm for non-smoking mothers?
Z=(x-μ)/σ=(48.5-51.8)/3.25=(-3.3)/3.25  =-1.02
  
Q22. Based on the dataset you have, what is the probability that the length of baby for non-smoking mothers will be more than 55 cm?
Z=(x-μ)/σ=(55-51.8)/3.25=3.2/3.25  =0.98
P(Z>0.98)=1-P(Z≤0.98)=1-0.8365=0.1635
