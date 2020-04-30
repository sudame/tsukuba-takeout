#!/bin/bash

# build typescript files
cd typescript \
    && yarn install \
    && yarn build;

# collect static files to `/static/`
cd ../ \
    && poetry install \
    && poetry run ./manage.py collectstatic --clear "--ignore=*.scss" --no-input;
