import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px
import math



def read_data():
    data_path = Path(__file__).parents[0] 
    df = pd.read_csv(data_path / "Data" / "IceCreamData.csv")
    return df

def layout():

    df = read_data()
    st.title("Icecream Revenue Predictor")

    st.write("This is prediction of the Icecream revenue")

    X=df[['Temperature']]
    y=df['Revenue']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=44)
    regressor = RandomForestRegressor(n_estimators=10, random_state=0,oob_score=True)

    regressor.fit(X, y)
   
    #oob_score = regressor.oob_score_
    predictions = regressor.predict(X)
    mse = mean_squared_error(y, predictions)



    st.write("The root mean squared error score on dataset is ", math.sqrt(mse))

    number = st.number_input("Insert a number", step=0.5)
    st.write("The current temperature is: ", number)

    myval=[[number]]

    pred=regressor.predict(myval)
    
    st.write("Revenue prediction is: ", pred[0])

    st.header("Raw data")
    st.write("This shows the raw data that is the basis for the prediction")
    st.dataframe(df)
    read_css()

def read_css():
    css_path = Path(__file__).parent / "style.css"

    with open(css_path) as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True,
        )

if __name__ == "__main__":
    # print(read_data())
    layout()
