# Recipe Finder using Python Streamlit

## Overview
This repository contains code for a Recipe Finder app built using Python and Streamlit. The app allows users to search for recipes based on ingredients and dietary restrictions. It makes an API call to the Spoonacular API to retrieve recipe information and displays the results in a user-friendly interface.

## Installation
To run the Recipe Finder app, follow these steps:
1. Clone the repository to your local machine.
2. Install the required packages listed in the `requirements.txt` file using pip. Run `pip install -r requirements.txt`.
3. Create a free account on [Spoonacular](https://spoonacular.com/food-api) to obtain an API key.
4. Create a `secrets.toml` file in the root directory and add your Spoonacular API key to the file as follows:
```python
[api_key]
api_key = "YOUR_API_KEY_HERE"
```
5. Run the app by executing the command `streamlit run recipe_finder.py` in your terminal.

## Usage
To use the [Recipe Finder](https://deepankarvarma-recipe-finder-using-python-app-ihx7iy.streamlit.app/) app, follow these steps:
1. Enter comma-separated ingredients (e.g. chicken, rice, broccoli) into the input field.
2. Select any dietary restrictions you want to apply from the dropdown menu.
3. Click the "Find Recipes" button to retrieve a list of recipes.
4. The app displays the recipe titles, preparation time, serving size, and source link for each recipe in a table format.

## Technologies Used
* Python
* Streamlit
* Spoonacular API

## Links
* [Streamlit Share Link](https://deepankarvarma-recipe-finder-using-python-app-ihx7iy.streamlit.app/)
* [Spoonacular API](https://spoonacular.com/food-api)
