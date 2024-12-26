import streamlit as st 

import pandas as pd

data1 = {
    'Task':['Extract','Transform','Load'],
    'Status':['Completed','Inprogress','Pending']
}

df = pd.DataFrame(data1)
st.write('ETL Pipelineexecution Status',df)