# CI/CD Final Project - OpenShift & Tekton Pipeline

## Project Name: Account Management CI/CD Pipeline

This repository contains the CI/CD pipeline automation for the Account Management microservice. It demonstrates continuous integration with GitHub Actions and continuous delivery using Tekton Pipelines on an OpenShift cluster.

### Pipeline Features
- **Continuous Integration**: Linting with `flake8` and unit testing with `nose` (or pytest) using GitHub Actions.
- **Continuous Delivery**: Tekton pipeline deployed on Red Hat OpenShift, including cleanup, cloning, linting, testing, and deployment.
- **Artifact Management & Storage**: OpenShift PersistentVolumeClaim (PVC) integration for pipeline workspace sharing.
