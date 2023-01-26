from django.shortcuts import render

from .csv_converter import get_list_dicts_from_csv
from .models import MainPageEls, DemandPageEls, GeographyPageEls, KeySkillsPageEls
from .apihh import HH_Data


def main(request):
    data = list(MainPageEls.objects.filter(draft=False))[0]
    return render(request, 'mainapp/main_page.html', {'data': data})


def demand(request):
    data = list(DemandPageEls.objects.filter(draft=False))[0]
    table = get_list_dicts_from_csv(data.table.file.name)
    titles = list(table[0].keys())
    return render(request, 'mainapp/demend_page.html', {'data': data,
                                                        'table': table,
                                                        'titles': titles})


def geography(request):
    data = list(GeographyPageEls.objects.filter(draft=False))[0]
    table2 = get_list_dicts_from_csv(data.slr_table.file.name)
    titles2 = list(table2[0].keys())
    table3 = get_list_dicts_from_csv(data.count_vac_table.file.name)
    titles3 = list(table3[0].keys())
    return render(request, 'mainapp/geo_page.html', {'data': data,
                                                     'table2': table2,
                                                     'table3': table3,
                                                     'titles2': titles2,
                                                     'titles3': titles3})


def skills(request):
    data = list(KeySkillsPageEls.objects.filter(draft=False))[0]
    return render(request, 'mainapp/skills_page.html', {'data': data})


def vacancies(request):
    data = HH_Data('Тех. поддержка').get_data_vacancies('2022-12-12', 10)
    return render(request, 'mainapp/vacancies_page.html', {'data': data})




