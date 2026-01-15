
# Create your views here.
from django.shortcuts import render
from matplotlib import text
from rest_framework.views import APIView
from .models import Resume, JobDescription
from .analyzer import extract_text, calculate_score

class ResumeRankView(APIView):
    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request):
        role = request.POST.get('role')
        description = request.POST.get('description')
        resumes = request.FILES.getlist('resumes')

        JobDescription.objects.create(role=role, description=description)

        results = []

        for resume in resumes:
            r = Resume.objects.create(file=resume)
            text = extract_text(r.file.path)
            score = calculate_score(description, text)
            r.score = score
            r.save()

            results.append({
                'resume': r.file.name,
                'score': score
            })

        ranked = sorted(results, key=lambda x: x['score'], reverse=True)

        for i, r in enumerate(ranked):
            r['rank'] = i + 1

        return render(request, 'result.html', {'results': ranked})
