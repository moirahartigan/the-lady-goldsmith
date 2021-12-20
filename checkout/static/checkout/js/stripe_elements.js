/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// get the stripe public key.
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
// The card element can also accept a style argument. So get some basic styles direct from the stripe js Docs. (copy)
var style = {
    base: {
        color: '#000', // update is the default colour of the element to black
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545' // change the invalid colour to match bootstraps text danger class
    }
};
// create a card element
var card = elements.create('card', {style: style});
// and mount the card element to the div we created 
card.mount('#card-element');