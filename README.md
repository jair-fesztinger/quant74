# Interactive - Black Scholes Pricing Model

## Project Overview 

This code is a Streamlit application that visualizes the Black-Scholes option pricing model for both call and put options. It includes user input for model parameters, displays the calculated call and put option prices, and generates 3D interactive models showing how option prices vary with changes in asset prices and volatility. Designed with Python and CSS, it allows users to experiment with parameters to provide practical insight into the model's calculations and outputs. 

## Objectives

a. Exposure to Financial Mathematics: This project aims to deepen understanding of option pricing theory, particularly the Black-Scholes formula, a cornerstone in quantitative finance used to determine the fair value of options. By calculating call and put prices in real-time, users gain hands-on exposure to the assumptions and mathematical elements within financial modeling.

b. Application of Python for Financial Modeling: The project demonstrates the practical use of programming in financial modeling using Python's data processing and scientific libraries (NumPy, SciPy). Implementing these formulas allows users to bridge theory with application, furthering skills in quantitative analysis.

c. Visualization of Market Sensitivities: By providing dynamic 3D visualizations of option prices across a range of volatilities and asset prices, the project helps users explore how options respond to changing market conditions, fostering an intuitive grasp of sensitivities like delta, gamma, and vega.




## Key Features
- Customizable User Inputs: Adjust parameters such as the current asset price, strike price, time to maturity, volatility, and risk-free interest rate directly from the sidebar for tailored option pricing calculations.

- Dynamic 3D Visualization: Interactive 3D surface plots visualize call and put option prices over a range of asset prices and volatilities, offering a detailed look into price sensitivity.

- Elegant Design and Dark Theme: The app utilizes custom CSS for an appealing and easy-to-read interface with a dark theme, making it comfortable for extended use.

- Streamlined Calculations with Black-Scholes Formula: The app’s core leverages the Black-Scholes model, providing accurate theoretical call and put option prices.

- Real-Time Display of Calculated Prices: Results for call and put values are displayed in responsive, styled containers, with values updating immediately based on user inputs.



## Conclusion

This app provides an interactive platform to explore the Black-Scholes model, offering users a deep understanding of how volatility and asset prices impact call-and-put option values. The formula is a pricing model that determines the fair price for a call or put option based on the current price, strike price, time to maturity, volatility, and interest rate. This model is used by options traders who buy options priced below the computed value and sell those priced higher than the calculated value. The assumptions of the Black-Scholes formula are not listed here but can be found online.

I published a short explanation of my code on [Medium](https://medium.com/@napoles.jair/code-sections-explained-project-1-66dfcc975dee).
