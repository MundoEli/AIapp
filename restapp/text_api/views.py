from .models import TextModel
from .serializers import TextModelSerializer
import requests
from rest_framework import generics
from rest_framework.permissions import AllowAny


class FetchTextView(generics.CreateAPIView):
    serializer_class = TextModelSerializer
    permission_classes = [AllowAny]


    def perform_create(self, serializer):
        # Fetch text from an external API
        external_api_url = 'https://www.howellsstudio.com/?ref=onepagelove'
        response = requests.get(external_api_url)
        external_text = response

        # Save the text to the model
        serializer.save(data=external_text)


class EditTextAPIView(generics.RetrieveUpdateAPIView):
    queryset = TextModel.objects.all()
    serializer_class = TextModelSerializer

