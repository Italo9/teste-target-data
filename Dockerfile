FROM python:3.8.13

WORKDIR /app
COPY . /app

RUN python3 -m pip install --upgrade pip
RUN pip install -r dev-requirements.txt
RUN python3 -u "/home/italo/vaga-full-stack/teste-target-data/target/extrair_dados/extrair_dados_csv.py"
EXPOSE 5000
CMD ["flask", "run"]
