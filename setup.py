from setuptools import setup, find_packages

setup(
    name='smart_city_traffic_management',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'pandas',
        'scikit-learn',
        'docker',
        'safety',
        'bandit'
    ],
    entry_points={
        'console_scripts': [
            'run-server=deployment.api.api_endpoints:app.run',
        ],
    },
)
