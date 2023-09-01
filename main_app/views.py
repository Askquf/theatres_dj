from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from lab_3.serializer import TheatreSerializer, DistrictSerializer, PerfomanceSerializer
from lab_3.models import Theatre, Perfomance, District
from django.shortcuts import redirect
from rest_framework.response import Response

# data = {
#    'theatres':
#        [
#            {'path': 'mal', 'name': 'Малый театр', 'image_source': 'mal.jpg', 'information': 'Какая-то информация о малом театре'},
#            {'path':'sovremennik', 'name': 'Современник', 'image_source': 'sovremennik.jpg', 'information': 'Какая-то информация о театре "Современник"'},
#            {'path':'bol', 'name': 'Большой театр', 'image_source': 'bol.jpg', 'information': 'Какая-то информация о большом театре'},
#            {'path':'mht', 'name': 'МХТ им. А.П. Чехова', 'image_source': 'mht.jpg', 'information': 'Какая-то информация об МХТ'},
#            {'path':'lenkom', 'name': 'Ленком', 'image_source': 'lenkom.jpg', 'information': 'Какая-то информация о Ленкоме'}
#        ]
# }

def home(request):
    data_number = len(Theatre.objects.all())
    number_of_records = data_number if 'text' not in request.POST or \
                                       (not request.POST['text'].isdigit() or \
                                        0 >= int(request.POST['text']) \
                                        or int(request.POST['text']) >= data_number) else int(request.POST['text'])
    return render(request, "index.html", {'theatres': Theatre.objects.all().values()[0:number_of_records]})


def get_theatre(request, theatre_name):
    if 'url' not in request.POST:
        theatre = Theatre.objects.filter(url=theatre_name).values()
        return render(request, "theatre.html", theatre[0]) if len(theatre) > 0 else redirect(
            to='/')  # if len(theatre) > 0 else redirect(to='/')
    else:
        Theatre.objects.get(url=theatre_name).delete()
        return redirect(to='/')


class TheatreViewSet(viewsets.ModelViewSet):
    queryset = Theatre.objects.all().order_by('id')
    serializer_class = TheatreSerializer


class TheatreCount(APIView):
    def get(self, request, id):
        return Response({'number of theatres in this district': Theatre.objects.filter(district=id).count()})


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all().order_by('id')
    serializer_class = DistrictSerializer



class PerfomanceViewSet(viewsets.ModelViewSet):
    queryset = Perfomance.objects.all().order_by('id')
    serializer_class = PerfomanceSerializer


class AllApiLinks(APIView):
    def get(self, request):
        return Response({'All theatres': 'theatres/', 'All districts': 'districts/', 'All perfomances': 'perfomances/',
                         'Theatres by districts id': 'theatres/<id>'})





    #def get(self, request):
    #    return Response(self.queryset.all())