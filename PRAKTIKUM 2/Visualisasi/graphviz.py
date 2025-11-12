import streamlit as st
import graphviz as graphviz

st.title("Graphviz Chart")
st.write("**Kelompok 23**")
st.markdown("""
    - Amru Abdurrahman Azzam - 0110122322
    - Hayatunnisa - 0110222118
    - Nurul Maedatul Awaliah - 0110122222
""")

("========================================================================================")

st.graphviz_chart('''
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Results Forecasting"
        "New Data" -> "Model" 
    }
''')


#import streamlit as st
#import graphviz as graphviz

#st.title("Graphviz")


#membuat graphlib grab objek

#graph = graphviz.Digraph()
#graph.edge('Training Data', 'ML Algorithm')
#graph.edge('ML Algorithm', 'Model')
#graph.edge('Model', 'Result Forecasting')
#graph.edge('New Data', 'Model')
#st.graphviz_chart(graph)
