from setuptools import setup

setup(
    name='tweepy-streaming-api-emu',
    version='0.1',
    description='emulate streaming api',
    url='https://github.com/kgtkr/tweepy-streaming-api-emu',
    author='kgtkr',
    author_email='kgtkr.jp@gmail.com',
    license='MIT',
    keywords='twitter',
    packages=[
        "src"
    ],
    install_requires=["tweepy>=3.6.0"],
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)
