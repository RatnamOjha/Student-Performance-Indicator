# End-to-End Data Science & Machine Learning Project

This repository contains an end-to-end pipeline for a Data Science and Machine Learning project, including data ingestion, preprocessing, model training, and evaluation. The project is structured for modularity and reproducibility, making it easy to extend or adapt to new datasets.

## Project Structure

```
DS-ML/
├── artifacts/           # Generated artifacts (data splits, models, preprocessors)
├── data/                # Notebooks and scripts for EDA and manual runs
├── src/                 # Source code for the pipeline
│   ├── components/      # Core pipeline components (ingestion, transform, training)
│   ├── pipeline/        # (To be implemented) Scripts for running full pipelines
│   ├── utils.py         # Utility functions
│   ├── logger.py        # Logging setup
│   └── exceptions.py    # Custom exception handling
├── requirements.txt     # Python dependencies
├── setup.py             # Project install script
└── README.md            # Project documentation
```

## Dataset

The project uses the [Students Performance dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) (CSV format) with the following columns:
- gender
- race/ethnicity
- parental level of education
- lunch
- test preparation course
- math score
- reading score
- writing score

## Features
- **Data Ingestion:** Reads raw CSV data, splits into train/test, and saves artifacts.
- **Data Transformation:** Handles missing values, encodes categorical features, scales numerical features, and saves the preprocessor.
- **Model Training:** Trains multiple regression models, evaluates them, and saves the best model.
- **Utilities:** Custom logging and exception handling for robust pipelines.

## Notebooks
- `data/EDA.ipynb`: Exploratory Data Analysis.
- `data/model training.ipynb`: Manual model training and evaluation.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DS-ML.git
   cd DS-ML
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Install as a package:
   ```bash
   pip install .
   ```

## Usage
- **Data Ingestion:**
  Run the data ingestion component to generate train/test splits:
  ```python
  from src.components.data_ingestion import DataIngestion
  di = DataIngestion()
  train_path, test_path, raw_path = di.initiate_data_ingestion()
  ```
- **Data Transformation:**
  ```python
  from src.components.data_transform import DataTransformation
  dt = DataTransformation()
  train_arr, test_arr, preprocessor_path = dt.initiate_data_transformation(train_path, test_path)
  ```
- **Model Training:**
  ```python
  from src.components.model_trainer import ModelTrainer
  mt = ModelTrainer()
  r2 = mt.initiate_model_trainer(train_arr, test_arr)
  print(f'Best model R2 score: {r2}')
  ```

## Customization
- Update the data path in `src/components/data_ingestion.py` to point to your dataset.
- Extend the pipeline scripts in `src/pipeline/` for full automation (currently placeholders).

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)

---
*Author: Ratnam Ojha (<ratnamojha71@gmail.com>)*
