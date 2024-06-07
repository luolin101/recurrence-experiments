import pandas as pd

def test1():
    df = pd.DataFrame({
        "A":[1,1,3],"B":[1,4,6]
    })
    df= df.loc[df["A"]==1,:].copy()
    df.loc[:,"C"] = 1
    print(df)

test1()
