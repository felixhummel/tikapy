#!/usr/bin/env python
# encoding: utf-8
"""
    >>> filename = 'example.pdf'
    >>> get_metadata(filename)  # doctest: +ELLIPSIS
    {...'title': 'Apache Tika - Wikipedia, the free encyclopedia'...}
    >>> get_content(filename)  # doctest: +ELLIPSIS
    'Apache Tika - Wikipedia...more than 1400 file types...MIME types...'
    >>> extract(filename)  # doctest: +ELLIPSIS
    {...}
"""
import json
import os
import subprocess


JAVA = os.environ.get('TIKA_JAVA', 'java')
TIKA_JAR = os.environ.get('TIKA_JAR', 'tika-app-1.13.jar')


def run(*args):
    """
    Run tika and capture both stderr and stdout.

    Raises CalledProcessError on error. See
    https://docs.python.org/3/library/subprocess.html#subprocess.run
    """
    cmd = [JAVA, '-jar', TIKA_JAR, '--encoding=utf-8'] + list(args)
    return subprocess.run(
            cmd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)


def get_metadata(filename):
    result = run('--json', filename)
    unicode_stdout = result.stdout.decode('utf-8')
    metadata = json.loads(unicode_stdout)
    return metadata


def get_content(filename):
    result = run('--text-main', filename)
    unicode_stdout = result.stdout.decode('utf-8')
    return unicode_stdout


def extract(filename):
    meta = get_metadata(filename)
    content = get_content(filename)
    return {
        'meta': meta,
        'content': content
    }


if __name__ == "__main__":
    import doctest
    doctest.testmod()
