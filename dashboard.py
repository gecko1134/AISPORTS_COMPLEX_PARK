import streamlit as st
import altair as alt
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models.booking import Booking, Facility
from datetime import datetime, timedelta
import pandas as pd
import uuid

DATABASE_URL = "postgresql+psycopg2://user:password@host:port/dbname"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

st.title("Tenant Dashboard")
tenant_id = st.text_input("Enter your Tenant ID")

if tenant_id:
    with engine.connect() as conn:
        conn.execute(text(f"SET search_path TO {tenant_id}"))

    with SessionLocal() as db:
        st.subheader("📅 Upcoming Bookings (Next 7 Days)")
        now = datetime.now()
        future = now + timedelta(days=7)

        bookings = db.query(Booking).filter(
            Booking.start_time >= now,
            Booking.start_time <= future
        ).all()

        booking_data = [{
            "Facility": b.facility_id,
            "Start": b.start_time,
            "End": b.end_time,
            "Status": b.status
        } for b in bookings]

        df = pd.DataFrame(booking_data)
        if not df.empty:
            st.dataframe(df)

            st.subheader("📈 Bookings by Facility")
            chart = alt.Chart(df).mark_bar().encode(
                x="Facility",
                y="count()",
                color="Status"
            ).properties(width=600)
            st.altair_chart(chart, use_container_width=True)
        else:
            st.info("No bookings in the next 7 days.")

        st.subheader("➕ Create a New Booking")

        facilities = db.query(Facility).all()
        facility_map = {f.name: f.id for f in facilities}

        selected_facility_name = st.selectbox("Select Facility", list(facility_map.keys()))
        user_id = st.text_input("User ID")
        start_time = st.datetime_input("Start Time", value=now)
        end_time = st.datetime_input("End Time", value=now + timedelta(hours=1))
        if st.button("Submit Booking"):
            new_booking = Booking(
                id=str(uuid.uuid4()),
                facility_id=facility_map[selected_facility_name],
                user_id=user_id,
                start_time=start_time,
                end_time=end_time,
                status="confirmed"
            )
            db.add(new_booking)
            db.commit()
            st.success("Booking created successfully!")

        st.subheader("🏟️ Facility Summary")
        for f in facilities:
            st.markdown(f"- **{f.name}** – Capacity: {f.capacity}")
