import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title('Streamlit Sample App')

# Text input widget
name = st.text_input('Enter your name', '')

# Display a personalized greeting
if name:
    st.write(f'Hello, {name}! Welcome to the Streamlit app.')

# Slider widget
number = st.slider('Select a number', 0, 100, 25)

# Display the number selected by the slider
st.write(f'You selected: {number}')

# Checkbox widget
if st.checkbox('Show chart'):
    # Generate some data
    data = pd.DataFrame({
        'x': np.arange(10),
        'y': np.random.randint(0, 100, size=10)
    })
    
    # Create a simple line chart
    st.line_chart(data.set_index('x'))
    
    # Alternatively, you can use matplotlib for more customization
    fig, ax = plt.subplots()
    ax.plot(data['x'], data['y'], marker='o')
    ax.set_title('Sample Line Chart')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    
    st.pyplot(fig)
