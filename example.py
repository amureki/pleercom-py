# -*- coding: utf-8 -*-
from pleer_api import PleerApi


def main():
    app_id, app_key = 'YOUR_APPLICATION_ID', 'YOUR_APPLICATION_SECRET_KEY'

    pleer = PleerApi(app_id, app_key)

    params = {'query': 'Linkin Park'}
    response = pleer.tracks_search(params=params)
    print response


if __name__ == '__main__':
    main()