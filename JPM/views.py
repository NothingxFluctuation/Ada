import xlwt
from .models import JobPost

from django.http import HttpResponse

import datetime
import time


def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    cd = 'attachment; filename="jobs_fetched_{}.xlsx"'.format(time.strftime("%Y_%m_%d-%H_%M_%S"))
    response['Content-Disposition'] = cd

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Job Posts')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Title', 'Company Name', 'URL']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    from_date = datetime.datetime.now() - datetime.timedelta(days=1)
    # rows = JobPost.objects.filter(created_at__gte=from_date, bgc=False, garbage=False).values_list('title','company_name','url','bgc')
    rows = JobPost.objects.filter(created_at__gte=from_date, bgc=False, garbage=False, downloaded=False).values_list('title','company_name','url')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    for job in JobPost.objects.all():
        job.downloaded = True
        job.save()
    return response