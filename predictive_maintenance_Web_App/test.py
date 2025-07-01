import pandas as pd

# Proper input structure matching training data
sample_input = pd.DataFrame([{
    'Type': 'M',
    'Air temperature [K]': 300.0,
    'Process temperature [K]': 310.0,
    'Rotational speed [rpm]': 1500.0,
    'Torque [Nm]': 45.0,
    'Tool wear [min]': 120.0
}])

# Make sure the column names are an exact match
print(sample_input.columns)

