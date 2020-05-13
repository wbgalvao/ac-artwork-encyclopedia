#!/bin/bash

if [ "${BUILD_DATABASE}" = true ]; then
    flask init-db;
fi

flask run;
