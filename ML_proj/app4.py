import streamlit as st
import pickle
from PIL import Image


def main():
    st.title("HOTEL RESERVATION STATUS :red[ PREDICTION]")
    st.markdown("___")
    image=Image.open("hotel.jpg")
    st.image(image,width=800)
    st.write("")
    Booking_id=st.text_input("Booking_id","")
    no_of_adults=st.text_input("no_of_adults","")
    no_of_children=st.text_input("no_of_children","")
    no_of_weekend_nights=st.text_input("no_of_weekend_nights","")
    no_of_week_nights=st.text_input("no_of_week_nights","")
    type_of_meal_plan=st.radio("type_of_meal_plan",['Meal Plan 1','Not Selected','Meal Plan 2','Meal Plan 3'])
    if type_of_meal_plan=='Meal Plan 1':
        type_of_meal_plan=0
    elif type_of_meal_plan=='Not Selected':
        type_of_meal_plan=3
    elif type_of_meal_plan=='Meal Plan 2':
        type_of_meal_plan=1
    else:
        type_of_meal_plan=2
    required_car_parking_space=st.text_input("required_car_parking_space","")
    room_type_reserved=st.radio("room_type_reserved",['Room Type 1','Room Type 2','Room Type 3','Room Type 4','Room Type 5','Room Type 6','Room Type 7'])
    if room_type_reserved=='Room Type 1':
        room_type_reserved=0
    elif room_type_reserved=='Room Type 2':
        room_type_reserved=1
    elif room_type_reserved=='Room Type 3':
        room_type_reserved=2
    elif room_type_reserved=='Room Type 4':
        room_type_reserved=3
    elif room_type_reserved=='Room Type 5':
        room_type_reserved=4
    elif room_type_reserved=='Room Type 6':
        room_type_reserved=5
    else:
        room_type_reserved=6
    lead_time	=st.text_input("lead_time","")
    arrival_year=st.text_input("arrival_year","")
    arrival_month=st.text_input("arrival_month","")
    arrival_date=st.text_input("arrival_date","")
    market_segment_type= st.radio("market_segment_type", ["online", "offline"])
    if market_segment_type == "online":
        market_segment_type = 4
    else:
        market_segment_type = 3
    repeated_guest= st.text_input("repeated_guest", "")
    no_of_previous_cancellations=st.text_input("no_of_previous_cancellations", "")
    no_of_previous_bookings_not_canceled=st.text_input("no_of_previous_bookings_not_canceled", "")
    avg_price_per_room=st.text_input("avg_price_per_room", "")
    no_of_special_requests=st.text_input("no_of_special_requests", "")
    features=[Booking_id,no_of_adults,no_of_children,no_of_weekend_nights,no_of_week_nights,type_of_meal_plan,required_car_parking_space,room_type_reserved,lead_time,arrival_year,arrival_month,arrival_date,market_segment_type
              ,repeated_guest, no_of_previous_cancellations, no_of_previous_bookings_not_canceled,avg_price_per_room,no_of_special_requests]
    models=pickle.load(open('models.sav','rb'))
    scaler=pickle.load(open('scaler (1).sav','rb'))
    pred=st.button('PREDICT')
    if pred:
        prediction=models.predict(scaler.transform([features]))
        if prediction==0:
            st.write("Booking will not cancel")
        else:
            st.write("Booking will cancel")
main()
