import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

def run_ml(df):
    X = df[['Rating', 'Reviews', 'Price']]
    y = df['Installs']

    X = X.fillna(X.median())
    y = y.fillna(y.median())

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    mlr = LinearRegression()
    mlr.fit(X_train, y_train)
    mlr_pred = mlr.predict(X_test)

    # Random Forest 
    rf = RandomForestRegressor(random_state=42)
    rf.fit(X_train, y_train)
    rf_pred = rf.predict(X_test)

    results = pd.DataFrame({
        "Model": ["Multiple Linear Regression", "Random Forest"],
        "MAE": [
            mean_absolute_error(y_test, mlr_pred),
            mean_absolute_error(y_test, rf_pred)
        ],
        "R2 Score": [
            r2_score(y_test, mlr_pred),
            r2_score(y_test, rf_pred)
        ]
    })

    return results
