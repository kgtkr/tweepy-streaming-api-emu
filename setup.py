from setuptools import setup

setup(
    name='tweepy-streaming-api-emu',
    version='0.4',
    description='emulate streaming api',
    url='https://github.com/kgtkr/tweepy-streaming-api-emu',
    author='kgtkr',
    author_email='kgtkr.jp@gmail.com',
    license='MIT',
    keywords='twitter',
    packages=["tsae"],
    install_requires=["tweepy>=3.6.0", "schedule>=0.5.0"],
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)
