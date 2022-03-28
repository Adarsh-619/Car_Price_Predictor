import streamlit as st
import pickle
from datetime import date
# from joblib import load

# Loading the model
model = pickle.load(open('Car_Predictor.pkl', 'rb'))
# model = load('Car_Predict.joblib') 

def main():
    title = "Car Price Predictor"
    st.set_page_config(page_title=title, page_icon="🏎️")
    st.title("🏎️ Car Price Predictor 🏎️")
    st.markdown("#### Are you planning to sell you car ?\n#### Use me to know your best worth!!!")
    st.image("./assets/image.png")
    st.write('')
    st.write('')

    Years = st.number_input("In which year the car was purchased?", 1990, date.today().year, step=1, key='year')
    
    Present_Price = st.number_input('What is the current ex-showroom price of the car ?  (In ₹lakhs)', 0.00, 50.00, step=0.5, key ='present_price')
    
    Kms_Driven  = st.number_input("What is the distance completed by the car in Kilometers?", )
    
    Owner  = st.radio("The number of owners the car previously had? ", (0, 1, 2), key="owner")

    Fuel_Type = st.selectbox("What is the fuel type of the car? ", ("Petrol", "Diesel", "CNG"), key='fuel_type')
    if(Fuel_Type == "Petrol"):
        Fuel_Type = 0
    elif(Fuel_Type == "Diesel"):
        Fuel_Type = 1
    else:
        Fuel_Type = 2

    Seller_Type = st.selectbox("What is the Seller type of the car? ", ("Dealer", "Individual"), key='seller_type')
    if(Seller_Type == "Dealer"):
        Seller_Type = 0
    else:
        Seller_Type = 1

    Transmission = st.selectbox("What is the Transmission Type of the car? ", ("Manual", "Automatic"), key="transmission")
    if (Transmission == "Manual"):
        Transmission = 0
    else:
        Transmission = 1


    if(st.button("Estimate Price", key="predict")):
        try:
            prediction = model.predict([[Years, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner]])
            output = round(prediction[0], 2)
            if output < 0:
                st.warning("Sorry! You won't be able to sell this car...")
            else:
                st.success(f"You can sell this car for ₹{str(output)} Lakhs 🙌")

        except:
            st.warning("Oops🙄 Something went wrong\nPlease Try Again")



if __name__ == "__main__":
    main()