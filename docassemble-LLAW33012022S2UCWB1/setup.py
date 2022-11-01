import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012022S2UCWB1',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description="**Connection Zone**\n\nThis application was developed by Flinders University students in collaboration with Uniting*Care* Wesley Bowden Inc. (UCWB).\n\nThe application is designed to provide an easier way for potential clients to understand what UCWB's Financial Health Services can provide, as well as an easier and faster way to assess their eligibility for these services. Clients otherwise tend to contact the UCWB hotline consequently usually delaying the provision of a service to a client, and taking essential resources away from UCWB which could be better used.\n\nThrough this application, users are also provided with details for other service providers to ensure users can still access the support they need, even if it cannot be through UCWB.\n\n**Authors**\nAlison Rahier, Ava Willington, Monique Woltynski, Trevor Morris & Victor Barrientos-Opazo.",
      long_description_content_type='text/markdown',
      author='Alison Rahier',
      author_email='rahi0029@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[''],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012022S2UCWB1/', package='docassemble.LLAW33012022S2UCWB1'),
     )

