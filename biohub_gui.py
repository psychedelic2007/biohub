import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
import streamlit as st
from PIL import Image
from multiapp import MultiApp
from util.pages.home_page import home_page
from util.pages.feature1_calculation import feature1_calc
from util.pages.feature2_calculation import feature2_calc
from util.pages.feature3_calculation import feature3_calc
from util.pages.feature4_calculation import feature4_calc
from util.pages.ml_model import feature_calculation

app = MultiApp()

app.add_app("Home Page", home_page)
app.add_app("Feature 1 Calculation", feature1_calc)
app.add_app("Feature 2 Calculation", feature2_calc)
app.add_app("Feature 3 Calculation", feature3_calc)
app.add_app("Feature 4 Calculation", feature4_calc)
app.add_app("Feature Calculation", feature_calculation)
app.run()
