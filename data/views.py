from django.shortcuts import render
from .fusioncharts import FusionCharts
from .models import Crime, Clearance, Ccctv, Rate
from .models import YongsanBylocation, GangnamBylocation, DongjakBylocation

def arrest(request):
    Crime_data = Crime.objects.all()
    Clearance_data = Clearance.objects.all()
    chart1_data = {
        "chart": {
            "caption": "서울시 지역구별 범죄 발생 수",
            'xAxisName': '지역구',
            'theme': 'candy'
        },
        "categories": [{
            "category": [{"label": Crime.district} for Crime in Crime_data]
        }],
        "dataset": [
            {
                "seriesname": "Murder",
                "data": [{"value": Crime.murder} for Crime in Crime_data]
            },
            {
                "seriesname": "Robbery",
                "data": [{"value": Crime.robbery} for Crime in Crime_data]
            },
            {
                "seriesname": "Rape",
                "data": [{"value": Crime.rape} for Crime in Crime_data]
            },
            {
                "seriesname": "Theft",
                "data": [{"value": Crime.theft} for Crime in Crime_data]
            },
            {
                "seriesname": "Violence",
                "data": [{"value": Crime.violence} for Crime in Crime_data]
            }
        ]
    }
    chart2_data = {
        "chart": {
            "caption": "서울시 지역구별 범죄 검거 수",
            'xAxisName': '지역구',
            'theme': 'candy'
        },
        "categories": [{
            "category": [{"label": Clearance.district} for Clearance in Clearance_data]
        }],
        "dataset": [
            {
                "seriesname": "Murder",
                "data": [{"value": Clearance.murder} for Clearance in Clearance_data]
            },
            {
                "seriesname": "Robbery",
                "data": [{"value": Clearance.robbery} for Clearance in Clearance_data]
            },
            {
                "seriesname": "Rape",
                "data": [{"value": Clearance.rape} for Clearance in Clearance_data]
            },
            {
                "seriesname": "Theft",
                "data": [{"value": Clearance.theft} for Clearance in Clearance_data]
            },
            {
                "seriesname": "Violence",
                "data": [{"value": Clearance.violence} for Clearance in Clearance_data]
            }
        ]
    }
    chartObj1 = FusionCharts('dragcolumn2d', 'ex1', '1000', '450', 'chart-1', 'json', chart1_data)
    chartObj2 = FusionCharts('dragcolumn2d', 'ex2', '1000', '450', 'chart-2', 'json', chart2_data)
    rate_data = Rate.objects.all()
    return render(request, 'data/arrest.html', {'output1': chartObj1.render(), 'output2': chartObj2.render(), 'rate_data' : rate_data})
    
def safemap(request):
    cctv_data = Ccctv.objects.all()
    return render(request, 'data/safemap.html', {'cctv_data' : cctv_data})

def region(request) :
    return render(request, 'data/region.html')

def yongsan(request):
    yongsan_data = YongsanBylocation.objects.all()
    return render(request, 'data/yongsan.html', {'yongsan_data': yongsan_data})

def gangnam(request):
    gangnam_data = GangnamBylocation.objects.all()
    return render(request, 'data/gangnam.html', {'gangnam_data': gangnam_data})

def dongjak(request):
    dongjak_data = DongjakBylocation.objects.all()
    return render(request, 'data/dongjak.html', {'dongjak_data': dongjak_data}) 