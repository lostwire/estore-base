import setuptools

setuptools.setup(
    name='estore.base',
    version='0.0.1',
    description='Event Store Base Classes',
    author='Jnxy',
    author_email='jnxy@lostwire.net',
    license='BSD',
    zip_safe=False,
    include_package_data=True,
    packages=setuptools.find_namespace_packages(include=['estore.*']))
