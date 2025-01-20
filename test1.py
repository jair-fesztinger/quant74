#Import required libraries
import streamlit as st
import pandas as pd
from scipy.stats import norm
from numpy import log, sqrt, exp
import numpy as np


#Page configuration 
st.set_page_config(
    page_title="Black-Scholes Option Pricing Model",
    layout="wide",
    initial_sidebar_state="expanded"
    )


# Custom CSS to inject into Streamlit
st.markdown("""
<style>   
/* Set background color for the entire page */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: RGB(6, 6, 15); /* Dark raisin background */
}
            
 /* Set background color for the sidebar */
    [data-testid="stSidebar"] {
        background-color: RGB(28, 28, 74); /* Dark orange background */           
                              
/* Adjust the size and alignment of the CALL and PUT value containers */ 
.metric-container {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 8px; /* Adjust the padding to control height */
    width: auto; /* Auto width for responsiveness, or set a fixed width if necessary */
    margin: 0 auto; /* Center the container */
}

/* Custom classes for CALL and PUT values */
.metric-call {
    background-color: #748E54; /* Light green background */
    color: black; /* Black font color */
    margin-right: 10px; /* Spacing between CALL and PUT */
    border-radius: 10px; /* Rounded corners */
}

.metric-put {
    background-color: #ffcccb; /* Light red background */
    color: black; /* Black font color */
    border-radius: 10px; /* Rounded corners */
}            

/* Style for the value text */
.metric-value {
    font-size: 1.5rem; /* Adjust font size */
    font-weight: bold;
    margin: 0; /* Remove default margins */
}           

/* Style for the label text */
.metric-label {
    font-size: 1rem; /* Adjust font size */
    margin-bottom: 4px; /* Spacing between label and value */
}

</style>
""", unsafe_allow_html=True)


#Main page for output display
st.title("Black-Scholes Pricing Model")
st.info("The Black-Scholes model is a mathematical formula that attempts to quantify the theoretical fair value of an option price based on five variable inputs:")

#Black Scholes Class Definition
class BlackScholes:
    def __init__(
        self,
        time_to_maturity: float,
        strike: float,
        interest_rate: float,
        volatility: float,
        current_price: float,
       
    ):
        self.time_to_maturity = time_to_maturity
        self.strike = strike
        self.interest_rate = interest_rate
        self.volatility = volatility
        self.current_price = current_price
    
    def calculate_call_price(
        self, volatility, current_price
    ):
        time_to_maturity = self.time_to_maturity
        strike = self.strike
        interest_rate = self.interest_rate

        d1 = (
            log(current_price / strike) +
             (interest_rate + 0.5 * volatility ** 2 * time_to_maturity)
             ) / (
                 volatility * sqrt(time_to_maturity)
            )
        d2 = d1 - volatility * sqrt(time_to_maturity)

        call_price = current_price * norm.cdf(d1) - (
            strike * exp(-(interest_rate * time_to_maturity)) * norm.cdf(d2)
        )

        self.call_price = call_price

        return call_price
    
    def calculate_put_price(
        self, volatility, current_price    
    ):
       time_to_maturity = self.time_to_maturity
       strike = self.strike
       interest_rate = self.interest_rate
       
       d1 = (
            log(current_price / strike) +
             (interest_rate + 0.5 * volatility ** 2) * time_to_maturity
             ) / (
                 volatility * sqrt(time_to_maturity)
             )
       
       d2 = d1 - volatility * sqrt(time_to_maturity)
    
       put_price = (
            strike * exp(-(interest_rate * time_to_maturity)) * norm.cdf(-d2)
        ) - current_price * norm.cdf(-d1) 
       
       self.put_price = put_price

       return put_price 

    
#Sidebar for user inputs
with st.sidebar:
    st.write("Created by: Jonathan Napoles")
    linkedin_url = "https://www.linkedin.com/in/jonathannapoles777/"
    st.markdown(
        f'''
        <a href="{linkedin_url}" target="_blank" style="text-decoration: none;">
            <button style="background-color: #0a66c2; color: white; padding: 10px 15px; border: none; border-radius: 5px; cursor: pointer;">
                LinkedIn
            </button>
        </a>
        ''',
        unsafe_allow_html=True
    )
    st.markdown("---")
    
    st.title("Parameters")
    current_price = st.number_input("Current Asset Price", value=100.0)
    strike = st.number_input("Strike Price", value=100.0)
    time_to_maturity = st.number_input("Time to Maturity (Years)", value=1.0)
    volatility = st.number_input("Volatility (Sigma)", value=.2)
    interest_rate = st.number_input("Risk-Free Interest Rate", value=.05)

    st.markdown("---")
    st.title('3D Model Range')
    vol_min = st.slider('Min Volatility', min_value = .01, max_value = 1.0, step=.01)
    vol_max = st.slider('Max Volatility', min_value = .01, max_value = 1.0, step=.01)
    
    #define the range for asset prices
    vol_range = np.linspace(vol_min, vol_max, 10)

    st.markdown("")

    asset_price_min = st.number_input('Min Asset Price', value=0.1)
    asset_price_max = st.number_input('Max Asset Price', value=200)

    #define the range for asset prices
    asset_price_range = np.linspace(asset_price_min, asset_price_max, 50)

#table of inputs
input_data = {
    'Current Asset Price': [f"{current_price:.2f}"], #format numerical values with up to two decimal places
    'Strike Price': [f"{strike: .2f}"], 
    'Time to Maturity': [f"{time_to_maturity: .2f}"], 
    'Volatility': [f"{volatility: .2f}"], 
    'Interest Rate': [f"{interest_rate: .2f}"],
}

input_df = pd.DataFrame(input_data)

#hide index column of our dataframe inputs table
st.dataframe(input_df, use_container_width=True, hide_index=True)



#Black Scholes model instance and compute call price 
bs_model = BlackScholes(time_to_maturity, strike, interest_rate, volatility, current_price) 
call_price = bs_model.calculate_call_price(volatility, current_price)

#display call value in colored box
col1, col2 = st.columns([1,1])

with col1:
    st.write(f"""
        <div style="
            background-color: RGB(242, 239, 233); 
            color: black; 
            padding: 8px; 
            border-radius: 10px; 
            text-align: center;
            font-weight: bold;
            ">
            <div style="font-size: 1.2rem; margin-bottom: 4px;">CALL Value</div>
            <div style="font-size: 1.5rem;">${call_price:.2f}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("")
st.title("Call Pricing - 3D Model")

#import library for interactive 3D model
import plotly.graph_objs as go

#calculate call option price
Z = np.array([[bs_model.calculate_call_price(volatility, current_price) for volatility in vol_range] for current_price in asset_price_range])

#create the 3d surface 
fig_call = go.Figure(data=[go.Surface(z=Z, x=vol_range, y=asset_price_range, colorscale='RdYlGn')])

# Update layout for better visualization
fig_call.update_layout(scene=dict(
    xaxis_title='Volatility',
    yaxis_title='Asset Price',
    zaxis_title='Call Option Price'
), 
width=800, 
height=800,
paper_bgcolor= "black" # Color for the plot background
)

# Display the interactive 3D plot in Streamlit
st.plotly_chart(fig_call)

#Black Scholes model instance and compute put price 
bs_model = BlackScholes(time_to_maturity, strike, interest_rate, volatility, current_price) 
put_price = bs_model.calculate_put_price(volatility, current_price)

st.markdown("---")

#display put value in colored box
col3, col4 = st.columns([1,1])

with col4:
    st.write(f"""
        <div style="
            background-color: RGB(242, 239, 233); 
            color: black; 
            padding: 8px; 
            border-radius: 10px; 
            text-align: center;
            font-weight: bold;
            ">
            <div style="font-size: 1.2rem; margin-bottom: 4px;">PUT Value</div>
            <div style="font-size: 1.5rem;">${put_price:.2f}</div>
        </div>
    """, unsafe_allow_html=True)

st.title("Put Pricing - 3D Model")

#calculate call option price
Z_2 = np.array([[bs_model.calculate_put_price(volatility, current_price) for volatility in vol_range] for current_price in asset_price_range])

# Create the 3D surface plot for put prices using Plotly
fig_put = go.Figure(data=[go.Surface(z=Z_2, x=vol_range, y=asset_price_range, colorscale='RdYlGn')])

# Update layout for better visualization
fig_put.update_layout(scene=dict(
    xaxis_title='Volatility',
    yaxis_title='Asset Price',
    zaxis_title='Put Option Price'
), 
width=800, 
height=800,
paper_bgcolor= "black" # Color for the plot background
)

# Display the interactive Put 3D plot in Streamlit
st.plotly_chart(fig_put)
