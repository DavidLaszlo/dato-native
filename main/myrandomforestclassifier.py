from sklearn.ensemble import RandomForestClassifier


def classify(df_full, test_files):
    print('--- Training random forest')

    clf = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=0)
    train = df_full[df_full.sponsored.notnull()].fillna(0)
    test = df_full[df_full.sponsored.isnull() & df_full.file.isin(test_files)].fillna(0)
    clf.fit(train.drop(['file', 'sponsored'], 1), train.sponsored)

    print('--- Create predictions and submission')
    submission = test[['file']].reset_index(drop=True)
    submission['sponsored'] = clf.predict_proba(test.drop(['file', 'sponsored'], 1))[:, 1]
    return submission
