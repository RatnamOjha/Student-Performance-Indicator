# Student Performance Analysis & Prediction

Welcome! 👋 I'm Ratnam, and this project is my hands-on exploration into understanding and predicting student performance using real-world data. My goal was to build a transparent, reproducible process for tackling a regression problem from scratch—starting with raw data and ending with a trained model, all while learning and documenting each step along the way.

## Why This Project?

As someone passionate about data science, I wanted to challenge myself to go beyond just running models in a notebook. I wanted to:
- Practice structuring a real project, not just a one-off script.
- Learn how to break down the workflow: from data cleaning, to feature engineering, to model selection.
- Make my work reproducible and modular, so I (or anyone else) can revisit or extend it later.

## My Approach

1. **Exploratory Data Analysis (EDA):**
   - I started by diving into the data (see `data/EDA.ipynb`), asking questions like: What features matter? Are there missing values? What patterns can I spot?

2. **Data Preparation:**
   - I wrote scripts to handle missing values, encode categories, and scale features. I wanted to make sure the data was clean and ready for modeling.

3. **Model Building:**
   - I experimented with several regression models, comparing their performance and learning about their strengths and weaknesses. The code for this is in both the notebooks and the `src/components/` directory.

4. **Pipelines & Modularity:**
   - To avoid "notebook soup," I refactored my code into reusable components. This way, I could easily rerun the process or swap out parts as I learned more.

5. **Logging & Error Handling:**
   - I added custom logging and exception handling to make debugging easier and to learn best practices for production-level code.

## Project Structure

```
DS-ML/
├── artifacts/           # Where data splits, models, and preprocessors are saved
├── data/                # Notebooks for EDA and manual experiments
├── src/                 # All the core Python code
│   ├── components/      # Data ingestion, transformation, and model training
│   ├── pipeline/        # (To be expanded) Scripts for running the full process
│   ├── utils.py         # Helper functions
│   ├── logger.py        # Logging setup
│   └── exceptions.py    # Custom error handling
├── requirements.txt     # Everything you need to install
├── setup.py             # For installing as a package
└── README.md            # This file
```

## How to Use

1. **Clone the repo and install dependencies:**
   ```bash
   git clone https://github.com/yourusername/DS-ML.git
   cd DS-ML
   pip install -r requirements.txt
   ```
2. **(Optional) Install as a package:**
   ```bash
   pip install .
   ```
3. **Run the process step by step:**
   - Data ingestion:
     ```python
     from src.components.data_ingestion import DataIngestion
     di = DataIngestion()
     train_path, test_path, raw_path = di.initiate_data_ingestion()
     ```
   - Data transformation:
     ```python
     from src.components.data_transform import DataTransformation
     dt = DataTransformation()
     train_arr, test_arr, preprocessor_path = dt.initiate_data_transformation(train_path, test_path)
     ```
   - Model training:
     ```python
     from src.components.model_trainer import ModelTrainer
     mt = ModelTrainer()
     r2 = mt.initiate_model_trainer(train_arr, test_arr)
     print(f'Best model R2 score: {r2}')
     ```

## What I Learned
- The importance of clean, modular code (especially when things break!)
- How different models behave on real data
- The value of logging and error handling for debugging
- That structuring a project well saves a ton of time in the long run

## Next Steps
- Automate the full pipeline (see `src/pipeline/`—work in progress!)
- Experiment with more advanced feature engineering
- Try deploying the model as an API

---

If you're curious, want to collaborate, or have feedback, feel free to reach out! 

*Ratnam Ojha (<ratnamojha71@gmail.com>)*
