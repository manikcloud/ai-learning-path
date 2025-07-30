# 🐍 Session 1: Python Fundamentals (Hands-on)

## 🎯 Session Overview
**Duration**: 8-10 hours  
**Type**: Practical Workshop  
**Trainer**: Delhi-based AI Expert  
**Focus**: Hands-on Python programming with AI/ML context  

## 📚 Learning Objectives

By the end of this session, you will:
- ✅ Master Python fundamentals with practical examples
- ✅ Work confidently with essential Python libraries
- ✅ Build 3 real-world projects
- ✅ Understand Python's role in AI/ML ecosystem
- ✅ Set up a complete Python development environment

## 🛠️ Session Content

### Part 1: Python Fundamentals (3 hours)

#### 1.1 Python Basics
- **Variables and Data Types**
  ```python
  # Indian context examples
  student_name = "Rahul Sharma"
  age = 25
  cgpa = 8.5
  is_placed = True
  skills = ["Python", "Machine Learning", "Data Science"]
  ```

- **Control Structures**
  ```python
  # Salary calculation for Indian IT industry
  experience = 3
  if experience < 2:
      salary = 400000  # 4 LPA
  elif experience < 5:
      salary = 800000  # 8 LPA
  else:
      salary = 1200000  # 12 LPA
  ```

- **Functions and Classes**
  ```python
  class IndianStudent:
      def __init__(self, name, city, course):
          self.name = name
          self.city = city
          self.course = course
      
      def introduce(self):
          return f"Namaste! I'm {self.name} from {self.city}, studying {self.course}"
  ```

#### 1.2 File Handling and Exception Management
```python
# Reading Indian census data
try:
    with open('indian_cities.csv', 'r') as file:
        cities_data = file.read()
        print("Data loaded successfully!")
except FileNotFoundError:
    print("Census data file not found!")
except Exception as e:
    print(f"Error occurred: {e}")
```

### Part 2: Essential Libraries (3 hours)

#### 2.1 NumPy - Numerical Computing
```python
import numpy as np

# Indian stock market data analysis
nifty_prices = np.array([15000, 15200, 14800, 15100, 15300])
daily_returns = np.diff(nifty_prices) / nifty_prices[:-1] * 100
print(f"Daily returns: {daily_returns}")

# Multi-dimensional arrays for image processing
image_array = np.random.randint(0, 255, (100, 100, 3))  # RGB image
print(f"Image shape: {image_array.shape}")
```

#### 2.2 Pandas - Data Manipulation
```python
import pandas as pd

# Indian e-commerce data
sales_data = pd.DataFrame({
    'product': ['Smartphone', 'Laptop', 'Tablet', 'Headphones'],
    'price': [25000, 65000, 35000, 5000],
    'city': ['Mumbai', 'Delhi', 'Bangalore', 'Chennai'],
    'sales': [150, 80, 120, 200]
})

# Data analysis
city_sales = sales_data.groupby('city')['sales'].sum()
print("Sales by city:")
print(city_sales)
```

#### 2.3 Matplotlib/Seaborn - Data Visualization
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Visualizing Indian IT industry growth
years = [2018, 2019, 2020, 2021, 2022, 2023]
revenue = [180, 191, 194, 227, 245, 260]  # in billion USD

plt.figure(figsize=(10, 6))
plt.plot(years, revenue, marker='o', linewidth=2, markersize=8)
plt.title('Indian IT Industry Revenue Growth', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Revenue (Billion USD)')
plt.grid(True, alpha=0.3)
plt.show()
```

### Part 3: AI/ML Libraries Introduction (2 hours)

#### 3.1 TensorFlow Basics
```python
import tensorflow as tf

# Simple neural network for Indian house price prediction
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])
print("Model created for house price prediction!")
```

#### 3.2 PyTorch Introduction
```python
import torch
import torch.nn as nn

# Simple linear regression for crop yield prediction
class CropYieldPredictor(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(3, 1)  # rainfall, temperature, fertilizer -> yield
    
    def forward(self, x):
        return self.linear(x)

model = CropYieldPredictor()
print("Crop yield prediction model created!")
```

## 🚀 Hands-on Projects

### Project 1: Data Analysis Dashboard
**Objective**: Build a complete data analysis tool for Indian startup ecosystem

**Features**:
- Load and clean startup funding data
- Analyze funding trends by city and sector
- Create interactive visualizations
- Generate insights and reports

**Files**:
- `notebooks/startup_analysis.ipynb`
- `projects/startup_dashboard.py`
- `resources/indian_startups.csv`

### Project 2: API Integration Project
**Objective**: Create a weather data aggregator for Indian cities

**Features**:
- Fetch weather data from multiple APIs
- Store data in structured format
- Create weather comparison tool
- Build simple CLI interface

**Files**:
- `projects/weather_aggregator.py`
- `resources/indian_cities.json`

### Project 3: Basic ML Model
**Objective**: Implement a simple prediction system for Indian context

**Features**:
- Predict house prices in Indian metros
- Use multiple regression techniques
- Compare model performance
- Create prediction interface

**Files**:
- `notebooks/house_price_prediction.ipynb`
- `projects/price_predictor.py`
- `resources/house_prices_india.csv`

## 📁 Session Structure

```
Session-1-Python-Fundamentals/
├── README.md (this file)
├── notebooks/
│   ├── 01_python_basics.ipynb
│   ├── 02_libraries_intro.ipynb
│   ├── 03_startup_analysis.ipynb
│   └── 04_house_price_prediction.ipynb
├── projects/
│   ├── startup_dashboard.py
│   ├── weather_aggregator.py
│   └── price_predictor.py
└── resources/
    ├── indian_startups.csv
    ├── indian_cities.json
    ├── house_prices_india.csv
    └── setup_guide.md
```

## 🔧 Setup Instructions

### 1. Python Environment Setup
```bash
# Install Python 3.8+ (if not already installed)
python --version

# Create virtual environment
python -m venv ai_learning_env

# Activate virtual environment
# On Windows:
ai_learning_env\Scripts\activate
# On macOS/Linux:
source ai_learning_env/bin/activate

# Install required packages
pip install -r requirements.txt
```

### 2. Required Libraries
```txt
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=1.0.0
tensorflow>=2.8.0
torch>=1.11.0
requests>=2.25.0
jupyter>=1.0.0
```

### 3. IDE Setup
- **Recommended**: VS Code with Python extension
- **Alternative**: PyCharm Community Edition
- **Jupyter**: For interactive notebooks

## 🎯 Learning Outcomes

After completing this session:

### Technical Skills:
- ✅ **Python Proficiency**: Write clean, efficient Python code
- ✅ **Library Mastery**: Use NumPy, Pandas, Matplotlib effectively
- ✅ **Data Handling**: Load, clean, and analyze real-world datasets
- ✅ **Visualization**: Create meaningful charts and graphs
- ✅ **ML Basics**: Understand TensorFlow and PyTorch fundamentals

### Practical Skills:
- ✅ **Project Development**: Build complete Python applications
- ✅ **Problem Solving**: Apply Python to real-world problems
- ✅ **Code Organization**: Structure projects professionally
- ✅ **Documentation**: Write clear, maintainable code

### Indian Context Understanding:
- ✅ **Local Applications**: Apply skills to Indian business scenarios
- ✅ **Cultural Relevance**: Use examples from Indian context
- ✅ **Industry Awareness**: Understand Python's role in Indian IT industry

## 📊 Assessment Criteria

### Project Evaluation (70%):
- **Code Quality**: Clean, readable, well-commented code
- **Functionality**: All features working as expected
- **Innovation**: Creative solutions and additional features
- **Documentation**: Clear README and code comments

### Practical Skills (30%):
- **Live Coding**: Solve problems during session
- **Debugging**: Identify and fix code issues
- **Explanation**: Explain code logic and decisions
- **Best Practices**: Follow Python coding standards

## 🔗 Additional Resources

### Online Resources:
- [Python.org Official Tutorial](https://docs.python.org/3/tutorial/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/)

### Indian Context Resources:
- [Indian Government Open Data](https://data.gov.in/)
- [Reserve Bank of India Data](https://www.rbi.org.in/Scripts/Statistics.aspx)
- [Indian Stock Market Data](https://www.nseindia.com/)
- [Startup India Database](https://www.startupindia.gov.in/)

### Books (Recommended):
- "Automate the Boring Stuff with Python" by Al Sweigart
- "Python for Data Analysis" by Wes McKinney
- "Hands-On Machine Learning" by Aurélien Géron

## 🎓 Next Steps

After mastering Python fundamentals:
1. **Session 2**: Dive into AI/ML theoretical concepts
2. **Practice**: Continue building projects with Indian datasets
3. **Community**: Join Python India community groups
4. **Specialization**: Choose focus area (Web Dev, Data Science, AI/ML)

---

## 👨‍🏫 Trainer Notes

### Session Delivery Tips:
- **Interactive Coding**: Live code with students following along
- **Indian Examples**: Use relatable examples from Indian context
- **Practical Focus**: Emphasize real-world applications
- **Error Handling**: Show common mistakes and how to fix them
- **Q&A Sessions**: Regular breaks for questions and clarification

### Common Student Challenges:
1. **Environment Setup**: Help with Python installation and IDE setup
2. **Syntax Errors**: Common beginner mistakes and solutions
3. **Library Confusion**: Clear explanation of when to use which library
4. **Project Scope**: Guide students to manageable project sizes

---

**🚀 Ready to master Python for AI? Let's start coding!**

*Designed by AI trainers in Delhi for practical, hands-on learning* 🇮🇳
