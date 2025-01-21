# import streamlit as st
# st.title("python🏡")
# st.header("Full stack")
# st.write("### My text")
# st.write("- _My text 2_")
# st.code("""
#         include<stdio.h>
#         int main(){
#         printf("hello world");
#         return 0;
#         }
# """,language="c")
# col1,col2,col3 = st.columns(3)
# with col1:
#     st.metric("python","full stack",-20)
# with col2:
#     st.metric("python","full stack",-20)
# with col3:
#     st.metric("python","full stack",-20)
import streamlit as st
from streamlit_option_menu import option_menu
with st.sidebar:
      selected = option_menu (
      menu_title ="internship",
      options=["home","about","contact"],
      icons=["house fill","fil-person","person-line-fill"]
      )
    if selected =="home":
      st.title("home page":)
elif selected == ("about"):
      st.title("")
elif selected =="contact":



# with st.sidebar:
#     name = st.text_input("Enter your name")
#     st.button("click ")
#     st.write(name)
#     st.balloons()