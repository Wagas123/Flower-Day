#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit app
st.title("🌸 Flower Simulation 🌸")
st.write("A beautiful flower just for you! 😊")

# Special Message
st.markdown("## Happy Flower's Day 'Bunny' Ms. Lorraine!! 💐")
st.markdown("### From J 💖")

# Define parameters for the flower
n_petals = st.slider("Number of Petals", min_value=3, max_value=12, value=6)
k = n_petals / 2  # Controls the number of petals
r_max = 10  # Maximum radius

# Generate theta values
theta = np.linspace(0, 2 * np.pi, 1000)

# Compute the radius as a function of theta
r = r_max * np.cos(k * theta)

# Convert to Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot the flower
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, y, color='purple', linewidth=2)
ax.fill(x, y, color='pink', alpha=0.6)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title("A Flower for You 🌸")

# Display the plot in Streamlit
st.pyplot(fig)

st.write("Share this flower with someone special! 💖")

