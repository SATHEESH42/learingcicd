name: Python Build, Test, and Package

on:
  push:
    branches: [main]
  pull_request:

jobs:
  build-test-package:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pip install pytest
          pytest

      - name: Build package
        run: |
          pip install build
          python -m build

      - name: Upload built package
        uses: actions/upload-artifact@v4
        with:
          name: dist-files
          path: dist/
