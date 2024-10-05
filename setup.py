from setuptools import setup, find_packages
import io

# Lê o README.md usando codificação UTF-8
with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="projeto_imc",
    version="1.0.0",
    author="Teophilo Silva",
    author_email="seu.email@exemplo.com",
    description="Um pacote simples para cálculo de IMC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/projeto_imc",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)