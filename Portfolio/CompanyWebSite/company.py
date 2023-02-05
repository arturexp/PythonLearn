import streamlit as st
import pandas

about = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut viverra, augue ac molestie iaculis, 
tellus ipsum mattis erat, quis feugiat nulla libero id odio. Quisque feugiat vestibulum lacus, 
sit amet vulputate risus auctor gravida. Maecenas ornare eu purus at dapibus. Sed bibendum viverra augue, 
vitae auctor ante egestas ac. Nullam ornare pulvinar augue in eleifend. Proin scelerisque metus non massa pharetra tristique. 
Maecenas vitae consectetur nibh. Mauris ut quam commodo, elementum purus a, interdum urna. Lorem ipsum dolor sit amet, 
'''
col1, col2 = st.columns(2)
st.subheader("The Best Company")
st.write(about)
st.header('Our Team')

col3, col4, col5 = st.columns(3)

df = pandas.read_csv("CompanyWebSite/data2.csv")

with col3:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("CompanyWebSite/images/" + row["image"])

with col4:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("CompanyWebSite/images/" + row["image"])

with col5:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("CompanyWebSite/images/" + row["image"])
