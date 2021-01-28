from django.shortcuts import render, redirect
from .models import CheckLinksResult
import requests
import sqlite3
import pandas as pd


# Create your views here.
def render_main_page(request):
    return render(request, 'main_page.html')


def show_result(request):

    links_content = request.GET['links_input']
    if len(links_content) == 0:
        links_content = 'Вы не ввели ссылки'

    links_content = links_content.split('\n')

    for link in links_content:
        link = link.replace('\r', '')
        try:
            req = requests.get(link)
            check_results = CheckLinksResult(
                original_link_url=link,
                history=req.history,
                final_link_url=req.url,
                final_link_status=req.status_code
            )
            check_results.save()

        except:
            check_results = CheckLinksResult(
                original_link_url=link,
                history='N/A',
                final_link_url='N/A',
                final_link_status='N/A'
            )
            check_results.save()

    # Обращаемся к базе данных для вывода результата в DataFrame
    con = sqlite3.connect('db.sqlite3')
    cursor = con.cursor()

    query = '''
    SELECT 
    check_date, original_link_url, history, final_link_url, final_link_status 
    FROM check_my_links_checklinksresult
    '''

    query_results = cursor.execute(query).fetchall()
    df = pd.DataFrame(query_results)
    columns = ['check_date', 'original_link_url', 'history', 'final_link_url', 'final_link_status']
    df.columns = columns
    links_content = df.to_html(index=False)

    return render(request, 'show_result.html', {
        'links_content': links_content,
    })


def clear_db(request):

    # Чистим БД от прошлых запросов
    CheckLinksResult.objects.all().delete()
    return redirect('main_page')

# РАБОТАЕТ!!!!!
