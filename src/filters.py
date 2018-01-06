def use_n_most_occuring_users(df, n=100):
    users = df.groupby(df['by']).size()
    filtered_users, _ = zip(
        *users.sort_values(ascending=False).head(n).items())
    return df[df['by'].map(lambda x: x in filtered_users)]


def get_users_with_more_than_n_comments(df, n=10):
    users = df.groupby(df['by']).size()
    users, _ = zip(*users[users > n].items())
    return df[df['by'].map(lambda x: x in users)]
