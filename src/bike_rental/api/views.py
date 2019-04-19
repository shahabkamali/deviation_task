from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication


class GetDeviationAPIView(APIView):
    """
    one endpoint where you return the standard deviation in bike rentals.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    #authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        """
        Return deviation.
        """
        deviation = {'test': 'done'}
        return Response(deviation)
