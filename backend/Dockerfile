FROM continuumio/miniconda3

WORKDIR /app

COPY ./environment.yml ./

RUN conda env create -f environment.yml
RUN pip install uvicorn

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]