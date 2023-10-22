'''
This file is meant to query DPM related data

To download used libraries:
pip3 install numpy pandas==1.5.3 bokeh hvplot holoviews neuprint-python openpyxl

'''


# Imports
import numpy as np
import pandas as pd
import bokeh
import hvplot.pandas
import holoviews as hv
import bokeh.palettes
from bokeh.plotting import figure, show, output_notebook
from neuprint import NeuronCriteria as NC
from neuprint import fetch_neurons
from neuprint import fetch_adjacencies, NeuronCriteria as NC
from neuprint.utils import connection_table_to_matrix
from neuprint import merge_neuron_properties
from neuprint import fetch_simple_connections

from neuprint import Client

# Set connection to neuprint server

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InppdmJlbnRhbEBnbWFpbC5jb20iLCJsZXZlbCI6Im5vYXV0aCIsImltYWdlLXVybCI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0oxSmhsS3d5Z1o4VVUzTXFZOS1ZSzVGdkY3QkNjWnkxS3ZRcnFjY1c1Sj1zOTYtYz9zej01MD9zej01MCIsImV4cCI6MTg3Nzg4OTY2MX0.4OvL6k47Aj1SOGRbdm3P8nVhm1SGYZKV81teR6BUZVA"
c = Client('neuprint.janelia.org', 'hemibrain:v1.2.1', TOKEN)



# select DPM neuron 
criteria = NC(bodyId=5813105172)


'''
# General properties of DPM neuron
neuron_df, roi_counts_df = fetch_neurons(criteria)
print(neuron_df[list(neuron_df.columns)])

'''



# Fetch all upstream connections TO DPM neuron
dpm_i_neuron_df, dpm_i_conn_df = fetch_adjacencies(None, 5813105172)
dpm_i_conn_df = merge_neuron_properties(dpm_i_neuron_df, dpm_i_conn_df, ['type', 'instance'])

# Fetch all downstream connections FROM DPM neuron
dpm_o_neuron_df, dpm_o_conn_df = fetch_adjacencies(5813105172, None)
dpm_o_conn_df = merge_neuron_properties(dpm_o_neuron_df, dpm_o_conn_df, ['type', 'instance'])

'''
# Export to excel file
with pd.ExcelWriter("output/dpm_query_summary.xlsx") as writer:
    dpm_i_conn_df.sort_values('weight', ascending=False).to_excel(writer, sheet_name="DPM inputs", index=False)
    dpm_o_conn_df.sort_values('weight', ascending=False).to_excel(writer, sheet_name="DPM outputs", index=False)

'''


neuron_df, conn_df = fetch_adjacencies(NC(type='Delta.*'), NC(type='PEN.*'))
conn_df = merge_neuron_properties(neuron_df, conn_df, ['type', 'instance'])
print(conn_df)
matrix = connection_table_to_matrix(conn_df, 'bodyId', sort_by='type')
print(matrix.iloc[:10, :10])
matrix.index = matrix.index.astype(str)
matrix.columns = matrix.columns.astype(str)
matrix.hvplot.heatmap(height=600, width=700, xaxis='top').opts(xrotation=60)
