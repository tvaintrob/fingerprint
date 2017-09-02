from setuptools import setup

setup(name='fingerprint',
      version='0.0.1',
      description='fingerprint a video file using opensubtitles hash search and tmdb',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7'
      ],
      install_requires=[
          'tmdbsimple',
          'python-opensubtitles'
      ],
      author='Tal Vintrob',
      license='MIT',
      packages=['fingerprint'],
      scripts=['bin/fingerprint'],
      zip_safe=True)
