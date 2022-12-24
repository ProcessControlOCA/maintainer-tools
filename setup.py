# License AGPLv3 (https://www.gnu.org/licenses/agpl-3.0-standalone.html)
import os
import setuptools


here = os.path.dirname(os.path.abspath(__file__))


setuptools.setup(
    name='processcontrol-maintainers-tools',
    author='ProcessControl',
    description='Set of tools to help managing ProcessControl projects',
    license='AGPL3',
    packages=['tools'],
    include_package_data=True,
    zip_safe=False,
    use_scm_version=True,
    setup_requires=[
        'setuptools_scm',
    ],
    install_requires=[
        'appdirs',
        'click',
        'docutils==0.16.*',
        'ERPpeek',
        'github3.py>=1',
        'inflection',
        'jinja2',
        'PyYAML',
        'polib',
        'pygments',
        'requests',
        'toml>=0.10.0',  # for oca-towncrier
        'towncrier>=21.3',  # for oca-towncrier
        'selenium',
        'twine',
        'wheel',
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: '
        'GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
    ],
    entry_points={
        'console_scripts': [
            'fix-manifest-website = tools.fix_manifest_website:main',
            'fix-manifest-author = tools.fix_manifest_author:main',
            'gen-addon-icon = tools.gen_addon_icon:main',
        ],
    },
)
