from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
	publishKey = settings.STRIPE_PUBLISHABLE_KEY
	if request.method == 'POST':
		token = request.POST['stripeToken']
		customer = stripe.Customer.create(
           email="paying.user@example.com",
           source=token,
        )

# Charge the Customer instead of the card:
        charge = stripe.Charge.create(
           amount=1000,
           currency="usd",
           customer=customer.id,
        )

# YOUR CODE: Save the customer ID and other info in a database for later.

# YOUR CODE (LATER): When it's time to charge the customer again, retrieve the customer ID.
        charge = stripe.Charge.create(
            amount=1500, # $15.00 this time
            currency="usd",
            customer=customer.id, # Previously stored, then retrieved
        )
	context = {'publishKey': publishKey}
	template = 'checkout.html'
	return render(request,template,context)	
