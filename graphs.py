from data import AvgCountry
import streamlit as st

class PisaGraphs():
    def __init__(self) -> None:
        self.grahps = AvgCountry().df_avg_contry

    # bar chart showing average PISA scores by location
    def bar_average_country(self):
        data = self.grahps
        st.bar_chart(data, x='LOCATION', y='PISAMATH',x_label="Country", y_label="Pisa score")

    # def bar_medals_athlete_top10(self):
    #     data = self.swe_medals.per_athlete.iloc[:10]
    #     st.bar_chart(data, x_label="athlete", y_label="medals per athlete")