import numpy as np
import matplotlib.pyplot as plt


lidar_signal = 0.8
radar_signal = 0.75


current_burn_percent = (lidar_signal * 0.6 + radar_signal * 0.4) * 100

print(f"Estimated Current Burned Area: {current_burn_percent:.2f}%")


time_hours = np.arange(0, 8, 1)
spread_rate_per_hour = 5
predicted_burn_percent = current_burn_percent + spread_rate_per_hour * time_hours
predicted_burn_percent = np.clip(predicted_burn_percent, 0, 100)


plt.figure(figsize=(8, 5))
plt.plot(time_hours, predicted_burn_percent, 'o-r', label='Predicted Burn %')
plt.xlabel('Time (hours)')
plt.ylabel('Burned Area (%)')
plt.title('Forest Fire Burn Prediction over Next 7 Hours')
plt.grid(True)
plt.legend()
plt.show()
