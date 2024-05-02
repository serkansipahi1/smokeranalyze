def functionssmoking(dataset, 'col_name')
    q1=np.percentile(dataset[col_name], 25)
    q3 = np.percentile(dataset[col_name], 75)
    iqr = q3-q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    drop_outliers = np.where((dataset[col_name] < lower_bound) | (dataset[col_name] > upper_bound))[0])

return functionssmoking()



