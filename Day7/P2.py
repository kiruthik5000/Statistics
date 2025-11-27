import os
import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def main():
    file_name = input().strip()
    file_path = os.path.join(sys.path[0], file_name)

    if not os.path.exists(file_path):
        print(f"File '{file_name}' not found at path: {file_path}")
        sys.exit(1)

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        sys.exit(1)

    df.fillna(df.mean(numeric_only=True), inplace=True)
    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    y = np.array(df_scaled['PremiumPrice'])

    # Model 2: Two features 'Age', 'AnyTransplants'
    X_2 = df_scaled[['Age', 'AnyTransplants']].values
    X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X_2, y, test_size=0.3, random_state=200)
    model_2 = LinearRegression().fit(X_train_2, y_train_2)
    y_pred_2 = model_2.predict(X_test_2)

    print('Model 2 (Age, AnyTransplants):')
    print('Intercept:', model_2.intercept_)
    print('Slopes:', model_2.coef_)
    MSE_2 = mean_squared_error(y_test_2, y_pred_2)
    MAE_2 = mean_absolute_error(y_test_2, y_pred_2)
    RMSE_2 = MSE_2 ** 0.5
    print('MSE =', MSE_2)
    print('RMSE =', RMSE_2)
    print('MAE =', MAE_2)
    print('R2 score =', r2_score(y_test_2, y_pred_2))

    # Model 3a: Three features 'Age', 'AnyTransplants', 'NumberOfMajorSurgeries'
    X_3a = df_scaled[['Age', 'AnyTransplants', 'NumberOfMajorSurgeries']].values
    X_train_3a, X_test_3a, y_train_3a, y_test_3a = train_test_split(X_3a, y, test_size=0.3, random_state=200)
    model_3a = LinearRegression().fit(X_train_3a, y_train_3a)
    y_pred_3a = model_3a.predict(X_test_3a)

    print('\nModel 3a (Age, AnyTransplants, NumberOfMajorSurgeries):')
    print('Intercept:', model_3a.intercept_)
    print('Slopes:', model_3a.coef_)
    MSE_3a = mean_squared_error(y_test_3a, y_pred_3a)
    MAE_3a = mean_absolute_error(y_test_3a, y_pred_3a)
    RMSE_3a = MSE_3a ** 0.5
    print('MSE =', MSE_3a)
    print('RMSE =', RMSE_3a)
    print('MAE =', MAE_3a)
    print('R2 score =', r2_score(y_test_3a, y_pred_3a))

    # Model 3b: Three features 'Age', 'AnyTransplants', 'AnyChronicDiseases'
    X_3b = df_scaled[['Age', 'AnyTransplants', 'AnyChronicDiseases']].values
    X_train_3b, X_test_3b, y_train_3b, y_test_3b = train_test_split(X_3b, y, test_size=0.3, random_state=200)
    model_3b = LinearRegression().fit(X_train_3b, y_train_3b)
    y_pred_3b = model_3b.predict(X_test_3b)

    print('\nModel 3b (Age, AnyTransplants, AnyChronicDiseases):')
    print('Intercept:', model_3b.intercept_)
    print('Slopes:', model_3b.coef_)
    MSE_3b = mean_squared_error(y_test_3b, y_pred_3b)
    MAE_3b = mean_absolute_error(y_test_3b, y_pred_3b)
    RMSE_3b = MSE_3b ** 0.5
    print('MSE =', MSE_3b)
    print('RMSE =', RMSE_3b)
    print('MAE =', MAE_3b)
    print('R2 score =', r2_score(y_test_3b, y_pred_3b))

    # Model 4: Four features 'Age', 'AnyTransplants', 'AnyChronicDiseases', 'BloodPressureProblems'
    X_4 = df_scaled[['Age', 'AnyTransplants', 'AnyChronicDiseases', 'BloodPressureProblems']].values
    X_train_4, X_test_4, y_train_4, y_test_4 = train_test_split(X_4, y, test_size=0.3, random_state=200)
    model_4 = LinearRegression().fit(X_train_4, y_train_4)
    y_pred_4 = model_4.predict(X_test_4)

    print('\nModel 4 (Age, AnyTransplants, AnyChronicDiseases, BloodPressureProblems):')
    print('Intercept:', model_4.intercept_)
    print('Slopes:', model_4.coef_)
    MSE_4 = mean_squared_error(y_test_4, y_pred_4)
    MAE_4 = mean_absolute_error(y_test_4, y_pred_4)
    RMSE_4 = MSE_4 ** 0.5
    print('MSE =', MSE_4)
    print('RMSE =', RMSE_4)
    print('MAE =', MAE_4)
    print('R2 score =', r2_score(y_test_4, y_pred_4))


if __name__ == "__main__":
    main()
--------------------------------------------- 2 -------------------------------------------
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import sys
import os 

def perform_data_analysis_and_modeling(filepath):


    df = pd.read_csv(os.path.join(sys.path[0], filepath))
   

    print("First 5 Rows:")
    print(df.head())
    print("\n")

    print("Dataset Info:")
    print(df.info())
    print("\n")

    print("Missing Values:\n ",end='')
    print(df.isnull().sum())
    print("\n")

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    for col in numeric_cols:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].mean(), inplace=True)

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])
        df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])
    print("Outlier treatment (IQR Winsorization) done.\n")

    df_processed = df.copy()

    scaler = StandardScaler()
    df_processed[numeric_cols] = scaler.fit_transform(df_processed[numeric_cols])

    print("First 5 Rows After Scaling:")
    print(df_processed.head())
    print("\n")

    X = df_processed[['Age']]
    y = df_processed['PremiumPrice']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=200)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Model 1 (Age):")
    print(f"Intercept: {model.intercept_}")
    print(f"Slope: {model.coef_}")
    print(f"MSE = {mse}")
    print(f"RMSE = {rmse}")
    print(f"MAE = {mae}")
    print(f"R2 score = {r2}")


if __name__ == "__main__":
    filename = input().strip()
    perform_data_analysis_and_modeling(filename)