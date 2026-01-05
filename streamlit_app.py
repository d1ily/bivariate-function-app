import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Interactive Visualization of Bivariate Functions")

st.write(
    "This interactive application helps visualize **bivariate functions** "
    "by allowing users to adjust parameters and observe changes in 3D surfaces."
)

function_type = st.selectbox(
    "Choose a bivariate function:",
    ["f(x, y) = x^2 + y^2", "f(x, y) = x^2y - y^3"]
)

x_range = st.slider("Range of x and y", 1, 5, 3)
resolution = st.slider("Graph resolution", 30, 100, 60)

x = np.linspace(-x_range, x_range, resolution)
y = np.linspace(-x_range, x_range, resolution)
X, Y = np.meshgrid(x, y)

if function_type == "f(x, y) = x^2 + y^2":
    Z = X**2 + Y**2
else:
    Z = X**2 * Y - Y**3

fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z)])
fig.update_layout(
    scene=dict(
        xaxis_title="x",
        yaxis_title="y",
        zaxis_title="z"
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

st.plotly_chart(fig, use_container_width=True)

st.write("### Explanation")
st.write(
    "- This surface represents a **bivariate function** where two inputs (x, y) "
    "determine one output (z).\n"
    "- Adjusting the sliders allows users to explore how the function behaves "
    "over different domains."
)
