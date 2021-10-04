from celery import shared_task
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
from django.apps import apps


@shared_task
def get_alexa_website_data():
    url = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
    resp = urlopen(url)
    zipfile = ZipFile(BytesIO(resp.read()))
    for line in zipfile.open(zipfile.namelist()[0]).readlines():
        line = line.decode()
        alexa_rank, url = line.split(',')
        url.strip('\n')
        apps.get_model('web.Website').objects.update_or_create(url=url,
            defaults={
                'alexa_rank': alexa_rank,
                'title': url.split('.')[0],
                'meta_description': 'md',
                'category': apps.get_model('web.WebsiteCategory').objects.get(id=1),
                })


