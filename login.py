import streamlit as st 

import pandas as pd

data = {
    'Task':['Extract','Transform','Load'],
    'Status':['Completed','Inprogress','Pending']
}

df = pd.DataFrame(data)
st.write('ETL Pipelineexecution Status',df)