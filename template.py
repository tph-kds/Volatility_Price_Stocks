import os
from pathlib import Path

package_name = "volatility_price_stocks"

list_of_files = [
    # Root folder
    ".github/workflows/ci.yaml",
    ".github/workflows/python_publish.yaml",
    ".github/workflows/tests.yaml",
    "src/__init__.py",
    f"src/params/__init__.py",
    f"src/params/configuaration.py",
    f"src/params/constants.py",
    f"src/{package_name}/__init__.py",
    # Config folder
    f"src/{package_name}/config/__init__.py",
    # Inference folder
    f"src/{package_name}/inference/__init__.py",
    # Components folder
    f"src/{package_name}/components/__init__.py",
    # Data folder
    f"src/{package_name}/components/data_ingestion/__init__.py",
    f"src/{package_name}/components/data_processing/__init__.py",
    f"src/{package_name}/components/feature_engineering/__init__.py",

    # Exception folder
    f"src/{package_name}/exception/__init__.py",
    # Logger folder
    f"src/{package_name}/logger/__init__.py",
    # Models folder
    f"src/{package_name}/models/__init__.py",
    f"src/{package_name}/models/base_model.py",

    # Pipeline folder
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/pipeline/predict_pipeline.py",

    # evaluation folder
    f"src/{package_name}/evaluation/__init__.py",

    # Utils folder
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/utils/config.py",
    f"src/{package_name}/utils/logger.py",
    f"src/{package_name}/utils/exception.py",

    # Main folder 
    # Inference folder
    "serving/flask_app/app.py",
    "serving/streamlit_app/app.py",
    
    # Tests folder
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    # Init folder
    "init_setup.sh",
    "requirements.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "Dockerfile",
    "docker-compose.yaml",
    "Makefile",
    # Experiments folder
    "experiments/experiment.ipynb",

]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass # Create a empty file