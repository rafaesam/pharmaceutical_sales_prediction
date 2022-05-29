import os, sys
sys.path.append(os.path.abspath(os.path.join('..')))
import time
import numpy as np
import pandas as pd
import streamlit as st

import home
import data
import prediction
# import data
# import insights
# import prediction


PAGES = {
  "Home": home,
  "Data": data
#  "Prediction": prediction
}

selection = st.sidebar.radio("Go to page", list(PAGES.keys()))
page = PAGES[selection]
page.app()