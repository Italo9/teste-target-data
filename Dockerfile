FROM python:3.8.13

ADD . /app
WORKDIR /app
COPY . /app

RUN python3 -m pip install --upgrade pip
RUN pip install -r dev-requirements.txt

CMD python -u target/extrair_dados/extrair_dados_csv.py && python -u target/aplicacao/aplicacao.py
