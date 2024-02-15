import plotly.graph_objects as go
#aaaaa
# Importar streamlit
import streamlit as st
import pandas as pd
import numpy as np
with open("styles.css") as f:
        st.markdown(f"""<style>{f.read()}</style>""",unsafe_allow_html=True)

df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
#aa
st.table(df)

st.markdown('''
<style> table.edTable { width: 100%; font-family: 'Segoe UI Light'; font-size: 16px; } table, table.edTable th, table.edTable td { border: solid 1px #9b58b5; border-collapse: collapse; padding: 7px 3px; text-align: center; } table.edTable td { background-color: #a963c6; color: #ffffff; font-size: 16px; } table.edTable th { background-color : #9b58b5; color: #ffffff; } tr:hover td { background-color: #9b58b5; color: #dddddd; } </style>

<table class="edTable" id="eDnaTab">
<tbody>
  <tr>
	<th>Header</th>
	<th>Header</th>
	<th>Header</th>
  </tr>
  <tr>
	<td>row 1 [cell 1]</td>
	<td>row 1 [cell 2]</td>
	<td>row 1 [cell 3]</td>
  </tr>
  <tr>
	<td>row 2 [cell 1]</td>
	<td>row 2 [cell 2]</td>
	<td>row 2 [cell 3]</td>
  </tr>
  <tr>
	<td>row 3 [cell 1]</td>
	<td>row 3 [cell 2]</td>
	<td>row 3 [cell 3]</td>
  </tr>
  <tr>
	<td>row 4 [cell 1]</td>
	<td>row 4 [cell 2]</td>
	<td>row 4 [cell 3]</td>
  </tr>
  <tr>
	<td>row 5 [cell 1]</td>
	<td>row 5 [cell 2]</td>
	<td>row 5 [cell 3]</td>
  </tr>
</tbody>
</table>

''',unsafe_allow_html=True)