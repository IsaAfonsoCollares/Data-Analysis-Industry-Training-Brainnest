import pandas as pd
import scipy.stats


df = pd.read_spss("Birthweight_reduced_kg_SPSS.sav")
smoker_df = df[df.smoker.eq('Smoker')]
non_smoker_df = df[df.smoker.eq('Non-smoker')]