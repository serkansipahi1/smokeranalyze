def drop_outliers(dataset, column_name):
    q1 = dataset[column_name].quantile(0.25)
    q3 = dataset[column_name].quantile(0.75)
    IQR = q3 - q1


    lower_bound = q3 - 1.5 * IQR
    upper_bound = q3 + 1.5 * IQR
    dataset = dataset[(dataset[column_name] >= lower_bound) & (dataset[column_name] <= upper_bound)]
    print(lower_bound, upper_bound)
    return dataset



