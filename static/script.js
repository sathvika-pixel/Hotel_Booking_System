// Welcome Message

console.log("Hotel Booking System Loaded");

// Confirm Booking

function confirmBooking(){

    let result=confirm("Confirm your booking?");

    if(result){

        alert("Booking Successful!");

    }

}

// Cancel Booking

function cancelBooking(){

    let result=confirm("Cancel this booking?");

    if(result){

        alert("Booking Cancelled");

    }

}

// Scroll to Top

function topFunction(){

    window.scrollTo({

        top:0,

        behavior:"smooth"

    });

}