#!/bin/bash

app_name='app'

cd ${app_name}
npm ci
npm run build
npm run dev