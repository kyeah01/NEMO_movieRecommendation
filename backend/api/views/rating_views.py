from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Rating
from api.serializers import RatingSerializer
from rest_framework.response import Response

@api_view(['POST'])
def ratings(request):
    if request.method == 'POST':
        ratings = request.data.get('ratings', None)

        for rate in ratings:
            userid = rate.get('userid', None)
            movieid = rate.get('movieid', None)
            rating = rate.get('rating', None)
            timestamp = rate.get('timestamp', None)
            
            Rating(movie_id=movieid, user_id=userid, rating=rating, rating_date=timestamp).save()

        return Response(status=status.HTTP_200_OK)