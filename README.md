
# Forest Fire Burn Prediction using Sensor Fusion

## Overview

This project demonstrates a simple forest fire monitoring and burn prediction model developed using Python. The system estimates the current percentage of burned area by combining simulated LiDAR and Radar sensor measurements through a weighted sensor fusion approach.

Based on the estimated burn percentage, the model predicts how the fire may spread over the next several hours using a constant spread rate and visualizes the prediction using Matplotlib.

The project introduces fundamental concepts of environmental monitoring, sensor fusion, and predictive modeling that are commonly used in wildfire management and autonomous monitoring systems.

---

## Features

- Sensor fusion using LiDAR and Radar data
- Burn area estimation
- Fire spread prediction
- Time-based forecasting
- Data visualization using Matplotlib
- Lightweight simulation
- Easy-to-understand implementation

---

## Technologies Used

- Python 3
- NumPy
- Matplotlib

---

## Project Structure

```text
Forest-Fire-Burn-Prediction/
│
├── fire_prediction.py
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Kaushal1525/Forest-Fire-Burn-Prediction.git
```

### Navigate to the project directory

```bash
cd Forest-Fire-Burn-Prediction
```

### Install the required packages

```bash
pip install -r requirements.txt
```

or

```bash
pip install numpy matplotlib
```

---

## Running the Project

Execute the following command:

```bash
python fire_prediction.py
```

The application will:

1. Estimate the current burned area using simulated sensor inputs.
2. Predict fire spread over the next seven hours.
3. Display a graph illustrating the projected increase in burned area.

---

## Working Principle

The simulation follows these steps:

1. Simulate LiDAR sensor measurements.
2. Simulate Radar sensor measurements.
3. Combine both signals using weighted sensor fusion.
4. Estimate the current burned area percentage.
5. Predict fire spread using a constant hourly spread rate.
6. Limit predictions to a maximum of 100%.
7. Visualize the prediction as a time-series graph.

---

## Sensor Fusion Model

The current burned area is estimated using a weighted average:

```text
Burn Percentage =
(LiDAR × 0.6) + (Radar × 0.4)
```

The result is converted into a percentage representing the estimated area affected by the fire.

---

## Fire Spread Prediction

The model assumes a constant hourly spread rate.

Prediction formula:

```text
Predicted Burn Area =
Current Burn Area + (Spread Rate × Time)
```

The predicted values are constrained between 0% and 100%.

---

## Output

The program displays:

- Estimated current burned area
- Predicted burned area for each hour
- Time-series graph of fire spread

---

## Future Enhancements

- Real LiDAR sensor integration
- Thermal camera support
- Satellite imagery analysis
- UAV-based fire monitoring
- Weather data integration
- Wind speed and direction modeling
- Machine learning-based fire prediction
- Geographic Information System (GIS) integration
- Real-time wildfire monitoring dashboard
- IoT sensor network deployment
- Multi-sensor fusion using Kalman Filters
- Autonomous drone surveillance

---

## Applications

- Wildfire Monitoring
- Forest Fire Prediction
- Environmental Monitoring
- Disaster Management
- Remote Sensing
- Smart Forestry
- Autonomous Environmental Monitoring
- UAV Fire Surveillance
- Sensor Fusion Research
- Artificial Intelligence in Environmental Science

---

## Requirements

- Python 3.8 or later
- NumPy
- Matplotlib

---

## Dependencies

- numpy
- matplotlib

---

## Author

Kaushal Reddy

AI & Autonomous Systems Engineer

GitHub: https://github.com/Kaushal1525
````
