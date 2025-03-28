import React from 'react';
import FlightSearch from './components/FlightSearch';
import BookingForm from './components/BookingForm';
import Payment from './components/Payment';
import Confirmation from './components/Confirmation';

function App() {
    return (
        <div>
            <h1>Airline Booking App</h1>
            <FlightSearch />
            <BookingForm />
            <Payment />
            <Confirmation />
        </div>
    );
}

export default App;
