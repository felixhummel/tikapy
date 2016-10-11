#!/usr/bin/env python
# encoding: utf-8
"""
Expects the Tika Server to be running on `http://localhost:9998`. To
override this::

    TIKA_SERVER_URL=http://tika.felixhummel.de

Usage::

    >>> filename = 'example.pdf'
    >>> with open('example.pdf', mode='rb') as f:
    ...     data = f.read()
    >>> info = extract(data)
    >>> info['meta']['Content-Type']
    'application/pdf'
    >>> info['meta']['title']
    'Apache Tika - Wikipedia, the free encyclopedia'
    >>> info['content']  # doctest: +ELLIPSIS
    '...Developer(s) Apache Software...more than 1400 file types...Apache Tika - Wikipedia...'

Please note that the binary mode is essential when opening files.
"""
import json
import os
import requests


TIKA_SERVER_URL = os.environ.get('TIKA_SERVER_URL', 'http://localhost:9998').rstrip('/')
meta_url = TIKA_SERVER_URL + '/meta'
tika_url = TIKA_SERVER_URL + '/tika'


def get_metadata(data):
    return requests.put(meta_url, data, headers={'Accept': 'application/json'}).json()


def get_content(content_type, data):
    # we need to supply the Content-Type to /tika
    headers = {'Content-Type': content_type, 'Accept-Encoding': 'utf-8'}
    content = requests.put(tika_url, data, headers=headers).content
    return content.decode('utf-8')


def extract(data):
    """
    :param data: Anything requests can use for put, i.e. dictionary, bytes,
                 or file-like object.
    """
    meta = get_metadata(data)
    if hasattr(data, 'seek'):
        data.seek(0)
    content = get_content(meta['Content-Type'], data)
    return {
        'meta': meta,
        'content': content
    }


if __name__ == "__main__":
    import doctest
    doctest.testmod()
