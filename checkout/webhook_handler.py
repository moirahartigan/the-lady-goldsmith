from django.http import HttpResponse


class StripeWH_Handler:
    """
    A class to handle Stripe webhooks
    """

    def __init__(self, request):
        """
        Initilisation of handler
        Args:
            request (object): Request object
        Returns:
            Request
        """
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        Args:
            self (object): Self object
            event: event
        Returns:
            HttpResponse object
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
