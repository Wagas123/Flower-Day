{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c8de2d13-b84f-401a-a2fc-e8c183f695f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Streamlit title\n",
    "st.title(\"🌸 Flower Day for Ms. Lorraine 🌸\")\n",
    "st.write(\"A special flower just for you! 💐\")\n",
    "\n",
    "# Message\n",
    "st.markdown(\"## Happy Flower's Day 'Bunny' Ms. Lorraine!! 💐\")\n",
    "st.markdown(\"### From J 💖\")\n",
    "\n",
    "# Flower Selector\n",
    "n_flowers = st.slider(\"Select number of flowers to display\", 1, 5, 1)\n",
    "\n",
    "# Function to generate flower plot\n",
    "def generate_flower(n_petals):\n",
    "    k = n_petals / 2  # Controls the number of petals\n",
    "    r_max = 10  # Maximum radius\n",
    "\n",
    "    # Generate theta values\n",
    "    theta = np.linspace(0, 2 * np.pi, 1000)\n",
    "\n",
    "    # Compute the radius as a function of theta\n",
    "    r = r_max * np.cos(k * theta)\n",
    "\n",
    "    # Convert to Cartesian coordinates\n",
    "    x = r * np.cos(theta)\n",
    "    y = r * np.sin(theta)\n",
    "\n",
    "    # Plot the flower\n",
    "    fig, ax = plt.subplots(figsize=(6, 6))\n",
    "    ax.plot(x, y, color='purple', linewidth=2)\n",
    "    ax.fill(x, y, color='pink', alpha=0.6)\n",
    "    ax.set_aspect('equal')\n",
    "    ax.axis('off')\n",
    "    ax.set_title(f\"Flower with {n_petals} Petals 🌸\")\n",
    "    \n",
    "    return fig\n",
    "\n",
    "# Display selected number of flowers\n",
    "for i in range(n_flowers):\n",
    "    st.write(f\"Flower {i+1}\")\n",
    "    fig = generate_flower(6)  # You can change the number of petals if desired\n",
    "    st.pyplot(fig)\n",
    "\n",
    "st.write(\"Share this flower with someone special! 💖\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
