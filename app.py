import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Recipe Finder", page_icon="🍴")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://4kwallpapers.com/images/wallpapers/ios-13-stock-ipados-dark-green-black-background-amoled-ipad-2560x1440-794.jpg");
        background-attachment: fixed;
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Recipe Finder")

def get_recipes(ingredients, diet):
    # api_key = "<your-api-key"
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": st.secrets["api_key"],
        "query": ingredients,
        "diet": diet,
        "number": 10,
        "addRecipeInformation": True
    }
    response = requests.get(url, params=params)
    return response.json()

def main():
    ingredients = st.text_input("Enter comma-separated ingredients (e.g. chicken, rice, broccoli): ")
    diet = st.selectbox("Dietary restrictions", ["None", "Vegetarian", "Vegan", "Gluten-Free", "Ketogenic"])

    if st.button("Find Recipes"):
        if ingredients:
            response = get_recipes(ingredients, diet)
            results = response["results"]
            if len(results) == 0:
                st.write("No recipes found.")
            else:
                df = pd.DataFrame(results)
                df = df[["title", "readyInMinutes", "servings", "sourceUrl"]]
                st.write(df)
        else:
            st.write("Enter at least one ingredient")

if __name__ == "__main__":
    main()
