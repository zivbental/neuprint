import numpy as np
import pandas as pd

import bokeh
import hvplot.pandas
import holoviews as hv

import bokeh.palettes

from bokeh.plotting import figure, show, output_notebook

from neuprint import Client

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InppdmJlbnRhbEBnbWFpbC5jb20iLCJsZXZlbCI6Im5vYXV0aCIsImltYWdlLXVybCI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0oxSmhsS3d5Z1o4VVUzTXFZOS1ZSzVGdkY3QkNjWnkxS3ZRcnFjY1c1Sj1zOTYtYz9zej01MD9zej01MCIsImV4cCI6MTg3Nzg4OTY2MX0.4OvL6k47Aj1SOGRbdm3P8nVhm1SGYZKV81teR6BUZVA"

c = Client('neuprint.janelia.org', 'hemibrain:v1.2.1', TOKEN)