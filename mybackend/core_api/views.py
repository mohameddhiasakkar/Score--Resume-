from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cvapp.models import Resume


@api_view(['POST'])
def upload_cv(request):
    file = request.FILES.get('file')
    if not file:
        return Response(
            {'error': 'No file provided. Use the "file" field.'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not file.name.lower().endswith('.pdf'):
        return Response(
            {'error': 'Only PDF files are supported.'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    resume = Resume.objects.create(file=file)

    return Response({
        'message': 'CV uploaded successfully',
        'resume_id': resume.id,
    }, status=status.HTTP_201_CREATED)
