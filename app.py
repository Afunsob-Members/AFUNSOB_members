import streamlit as st
import pandas as pd

st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://www.un.org/en/">
            <img src="app/static/UN.png" width="200">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.text(" ")

st.markdown("<h1 style='text-align: center;'>AFUNSOB Members Info</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>As of  29 August 2024</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Total Members: 358</h3>", unsafe_allow_html=True)

df = pd.read_excel('Members_List.xlsx', engine = "openpyxl")
df['UID No.'] = df['UID No.'].astype(str).str.zfill(9)

st.text(" ")

photos = []
for i in range(1,359):
    str = f"app/static/{i}.jpeg"
    photos.append(str)

df_photo = pd.DataFrame({"photo_key":photos})

df_merged = pd.concat([df_photo,df], axis=1)

st.data_editor(
  df_merged,
  column_config ={
    "photo_key":st.column_config.ImageColumn('Image', help = "Employee Photo")
  },
  hide_index = True,
  row_height=75
)


text_search = st.text_input("Search Employee by name:")


if text_search:
    filtered_df = df_merged[df_merged['Name of member'].str.contains(text_search)]

    st.data_editor(
      filtered_df,
      column_config ={
        "photo_key":st.column_config.ImageColumn('Image', help = "S.App open Image")
      },
      hide_index = True,
      row_height=75
    )

for i in range(0,30):
    st.text(" ")



