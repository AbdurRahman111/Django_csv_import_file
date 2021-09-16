from django.shortcuts import render, HttpResponse


from .models import name_database
from .resources import name_database_y
from tablib import Dataset




# Create your views here.

def first(request):
    return render(request, 'index.html')

def save_the_csv_file(request):
    if request.method == 'POST':
        name_database_yooo = name_database_y()
        dataset = Dataset()
        files_are = request.FILES['thefile']
        import_data_to_model = dataset.load(files_are.read(), format='xlsx')
        for data in import_data_to_model:
            value = name_database(
                data[0],
                data[1],
                data[2],

            )
            value.save()
    return render(request, 'index.html')

