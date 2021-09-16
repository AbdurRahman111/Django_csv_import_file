1. install package:
	 pip install django-import-export==2.5.0


2. add install app in settings.py:
	'import_export',

3. make a simple table

4. in admin.py add:
	from import_export.admin import ImportExportModelAdmin
	from .models import table

	class Bran(ImportExportModelAdmin):
    		pass
	admin.site.register(name_database, Bran)


continue for import export from templete otherwise step 1-4 is enough for admin penal import
5. add the resources.py

6. in views.py :
	from .resources import name_database_y
	from tablib import Dataset
	from .models import table 

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















