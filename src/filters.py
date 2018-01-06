def use_n_most_occuring_users(df, n=100):
    users = df.groupby(df['by']).size()
    filtered_users, _ = zip(
        *users.sort_values(ascending=False).head(n).items())
    unique_users = set(filtered_users)
    return df[df['by'].map(lambda x: x in unique_users)]
