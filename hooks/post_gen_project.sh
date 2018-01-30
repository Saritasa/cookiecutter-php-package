#!/usr/bin/env bash

git init

git add .
git remote add origin {{ cookiecutter.repo_ssh }}
