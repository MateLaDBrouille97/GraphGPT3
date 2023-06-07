
import os
import streamlit as st
import pandas as pd
from langchain.llms import OpenAI
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI



# word='histogram'or'Histogram'or 'bar'or'Bar' or 'chart'or'Chart'or'bar chart'or'Bar chart'or'Bar Chart'
# word1='line'or'Line'or 'chart'or'Chart'or'line chart'or'Line chart'or'Line Chart'
# word2='pie'or'Pie'or 'chart'or'Chart'or'pie chart'or'Pie chart'or'Pie Chart'
# word3='chart'or "Chart"or'plot'or'Plot'or'histogram'or'Graph'or'graph'or'Histogram'
# word4='heat'or'Heat'or'map'or'Map'or'heat map'or'Heat map'or 'Heat Map'
# word5="Plot"

with st.sidebar:
  st.header("CSV")
  csv = st.file_uploader("Upload your CSV", type=['csv'])

    
  st.header("API KEY")
  openaikey = st.text_input("Your openai key", value="", type="password",placeholder="openai key")



st.markdown(f"""
    ## \U0001F60A! Question Answering with your CSV file
    1) Upload a CSV. 
    2) Enter OpenAI API key. This costs $. Set up billing at [OpenAI](https://platform.openai.com/account).
    3) Type a question and Press 'Run'.
    4) You can plot your data with the good prompt🎈 """)

st.header("Ask your CSV 💬")

user_question = st.text_input("Ask a question about your CSV:")


def qg(csv_reader2,user_question):
    if openaikey is not None:
          os.environ["OPENAI_API_KEY"] = openaikey
    if csv is not None:
          prompt_text = user_question
          if prompt_text:
             llm = OpenAI()
             pandas_ai = PandasAI(llm)
             result=pandas_ai.run(csv_reader2=csv_reader2, prompt=prompt_text)
             
    return (result)



def main():
    
   if csv:
      csv_reader2 = pd.read_csv(csv)
      csv_reader2.columns = csv_reader2.columns.str.strip()
      # py_file = 'dataframe.py'
      # columns_names = csv_reader2.columns.tolist()
      
      # csv_reader2.to_csv("filename.csv", header=True, index=False, index_label='Index', sep='\t', encoding='utf-8', columns=csv_reader2.columns[1:])
      # csv_reader2.to_csv("data.csv", header=True, index=False, index_label='Index', sep='\t', encoding='utf-8', columns=csv_reader2.columns[1:])
      # csv_reader3 = pd.read_csv("filename.csv")
      # with open(py_file, 'w') as f:
      #    f.write('dataframe2 = {\n')
      #    for column_name in columns_names:
      #       f.write(f"'{column_name}': {csv_reader2[column_name].tolist()},\n")
      #    f.write('}\n')

      # data_fr=pd.DataFrame(dataframe2)
      # data_fr.columns = data_fr.columns.str.strip()

      dataf=csv_reader2.head()
      with st.expander('Dataframe'):
           st.subheader(csv.name)
           st.dataframe(csv_reader2)
      
   if st.button("Run", type="primary"):   
    if user_question:
      result=qg(csv_reader2=csv_reader2,user_question=user_question)
      st.write(result)
      st.set_option('deprecation.showPyplotGlobalUse', False)
      st.pyplot(print(result))
          

    
if __name__ == '__main__':
    main()
  