FROM python:3.9

# System deps:
RUN pip install "poetry==1.3.2"

# Copy only requirements to cache them in docker layer
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# Project initialization:
RUN poetry config virtualenvs.create false 
RUN poetry install --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . .

EXPOSE 5000
CMD [ "poetry", "run", "task", "start", "-u" ]

# fails if linting fails