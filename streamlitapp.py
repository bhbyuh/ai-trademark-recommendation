import streamlit as st
import pandas as pd
import requests
import json

endpoint="https://patent-recommendation-542808340038.us-central1.run.app/query"

st.set_page_config(layout="centered")

st.title("Trademark System")

text = st.text_area("Search query")

# Create a container to center the button
col1, col2, col3 = st.columns([2.3,2,1])

with col2:
    # Centered submit button
    submit_button = st.button('Submit')

if submit_button:
    with st.spinner('Generating Response..'):
        # Prepare the payload
        payload = {"query": text}
        
        # Make the POST request
        response = requests.post(endpoint, json=payload)
        data = response.content
        
        data_str = data.decode('utf-8')

        data = json.loads(data_str)
        data = data["data"]
        
        # Prepare lists for DataFrame
        class_name = []
        class_id = []
        
        for classs in data:
            class_name.append(classs)
            class_id.append(data[classs]["class id"])

        df = pd.DataFrame({
            "Class ID": class_id,
            "Class Name": class_name
        })
        
        df = df.applymap(lambda x: f"{int(x)}" if isinstance(x, (int, float)) else x)
        st.dataframe(df.reset_index(drop=True), use_container_width=True)
