import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px
import math
from graphs import PisaGraphs


# from components.metrics import Metrics, MedalsCountry
from data import GetBasics, AvgCountry
from graphs import PisaGraphs

pisa = GetBasics()
#graph1 = PisaGraphs()
mygraphs = PisaGraphs()
myobj = AvgCountry()



def layout():
    st.markdown("# Pisa data")
    st.markdown(
        """
        This dashboard shows Pisa results data.
        The source of the dataset comes from here https://www.kaggle.com/datasets/thedevastator/pisa-performance-scores-by-country
        
        """
    )

    st.markdown("## Basic data")
    st.write(f"Thu number of records {pisa.therows}, number of contries {pisa.numbcontries}, and number of subjects {pisa.subjects}")

    st.markdown("## Sample data")
    st.dataframe(pisa.data.reindex())

    st.header("Bar chart Pisa scores by country")

    st.dataframe(myobj.score_contry)
    #mygraphs.bar_average_country()

    st.bar_chart(data=myobj.score_contry, y=['PISAMATH', 'PISAREAD','PISASCIENCE'], stack=False)
    
    #PisaGraphs.bar_average_country

    # read_css()

# def read_css():
    # css_path = Path(__file__).parent / "style.css"

    # with open(css_path) as css:
    #     st.markdown(
    #         f"<style>{css.read()}</style>",
    #         unsafe_allow_html=True,
    #     )

if __name__ == "__main__":
    # print(read_data())
    layout()
