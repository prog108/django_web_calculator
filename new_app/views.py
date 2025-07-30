from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'new_app/index.html')

from django.shortcuts import render

def konverter(request):
    result = None
    if request.method == 'POST':
        value = float(request.POST.get('value'))
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')
        
        # jednostavan konvertor
        if from_unit == 'cm' and to_unit == 'm':
            result = value / 100
        elif from_unit == 'm' and to_unit == 'cm':
            result = value * 100
        elif from_unit == 'mm' and to_unit == 'cm':
            result = value / 10
        elif from_unit == 'mm' and to_unit == 'm':
            result = value / 1000
        elif from_unit == 'cm' and to_unit == 'mm':
            result = value * 10
        elif from_unit == 'm' and to_unit == 'cm':
            result = value * 1000

        else:
            result = value  # if the units are same: cm -> cm, mm -> mm

    context = {
        'result': result,
    }
    return render(request, 'new_app/converter.html', context)





'''def sample_view(request):
    return render(request, 'new_app/sample.html')'''