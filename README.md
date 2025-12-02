# DataRobot API Workshop

This repository contains example scripts for interacting with the DataRobot API to automate machine learning workflows. It demonstrates how to create projects, configure advanced options (like bias and fairness), and run both supervised and unsupervised modeling.

## Prerequisites

-   Python 3.13 or higher
-   DataRobot Python Client (`datarobot`)
-   A DataRobot account and API Key
-   A configured `datarobot.yaml` file or environment variables for authentication.

## Installation

This project uses `uv` for dependency management, but can also be installed via `pip`.

### Using uv (Recommended)

```bash
uv sync
```

### Using pip

```bash
pip install -r pyproject.toml
```
*(Or simply `pip install datarobot`)*

## Configuration

Ensure you have your DataRobot endpoint and API token configured. You can do this by creating a `~/.config/datarobot/drconfig.yaml` file (or `datarobot.yaml` in the current directory) with the following content:

```yaml
endpoint: https://app.datarobot.com/api/v2
token: YOUR_API_TOKEN
```

Alternatively, you can set environment variables:
-   `DATAROBOT_ENDPOINT`
-   `DATAROBOT_API_TOKEN`

## Scripts

### 1. Classification with Fairness (`classification.py`)

This script demonstrates how to:
-   Connect to an existing Data Source in DataRobot.
-   Create a new project for churn prediction.
-   Configure **Bias and Fairness** settings (e.g., protected features, fairness metrics).
-   Start Autopilot to build classification models.

**Usage:**
```bash
python classification.py
```

### 2. Unsupervised Clustering (`clustering.py`)

This script demonstrates how to:
-   Connect to the same Data Source.
-   Create a new project for clustering.
-   Configure the project for **Unsupervised Learning**.
-   Specify the number of clusters (e.g., 10) and start Autopilot.

**Usage:**
```bash
python clustering.py
```

### 3. Main Helper (`main.py`)

A simple entry point that prints a welcome message.

```bash
python main.py
```

