import pandas as pd
csv_files = ['aryanlog.csv', 'danishlog.csv', 'preetinderlog.csv', 'jahnvilog.csv', 'botdata.csv']
combined_df = pd.DataFrame()
for file in csv_files:
    df = pd.read_csv(file)
    combined_df = pd.concat([combined_df, df], ignore_index=True)
combined_df.to_csv('combineddata.csv', index=False)
print('Data successfully combined into combineddata.csv')