
st.title("Stock Risk Prediction")

st.write("Welcome to the Stock Risk Prediction App!")

model = joblib.load("stock_prediction_model.pkl")

st.success("Model loaded successfully!")
