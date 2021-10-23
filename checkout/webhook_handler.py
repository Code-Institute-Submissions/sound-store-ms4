from django.http import HttpResponse


class StripeWH_Handler:
    """Class for handling Stripe Web Hooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle an unknown or unexpected or generic webhook event"""
        return HttpResponse(
            content=f'Unhandled {event["type"]} Webhook was received',
            status=200,)
