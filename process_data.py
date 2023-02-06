# pylint:disable=E1101
import pandas as pd


def main():
    df = pd.read_json('data/results.json',lines=True)
    df = (pd.DataFrame(df['specs'].values.tolist())
        .join(df.drop('specs', axis=1)))

    # rename column names
    df.columns = (df.columns
        .str.replace(' ', '_')
        .str.replace('?','', regex=True)
        .str.replace('(','', regex=True)
        .str.replace(')','', regex=True)
        .str.replace('-','_', regex=True) 
        .str.lower()
        )

    # Save results
    df.to_csv("data/results.csv", sep=",", index=False)


if __name__ == "__main__":
    main()
