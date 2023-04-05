import pandas as pd
df = pd.DataFrame(
    {
        'col1': range(0, 20),
        'col2': range(20, 40),
        'col3': range(40, 60)
    }
)
#print(df)
x=df.iloc[:,1]
print(x)