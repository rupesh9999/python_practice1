import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('/home/ubuntu/python_practice1/projects/chapter_16/the_csv_file_format/data/death_valley_2018_full.csv')
print(df.columns)

# Strip spaces from column names
df.columns = df.columns.str.strip()

# Convert DATE to datetime and set as index
df['DATE'] = pd.to_datetime(df['DATE'])
df.set_index('DATE', inplace=True)

# Extract station information (constant across all rows)
station_info = df.iloc[0][['STATION', 'NAME', 'LATITUDE', 'LONGITUDE', 'ELEVATION']]

# Create a figure with 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle(f"Weather Data for {station_info['NAME']} ({station_info['STATION']})\n"
             f"Lat: {station_info['LATITUDE']}°N, Lon: {station_info['LONGITUDE']}°W, Elev: {station_info['ELEVATION']} m",
             fontsize=16)

# Plot 1: Temperature Data (TAVG, TMAX, TMIN, TOBS)
axs[0, 0].plot(df.index, df['TAVG'], label='Average Temp')
axs[0, 0].plot(df.index, df['TMAX'], label='Max Temp')
axs[0, 0].plot(df.index, df['TMIN'], label='Min Temp')
axs[0, 0].plot(df.index, df['TOBS'], label='Observed Temp')
axs[0, 0].set_title('Temperature')
axs[0, 0].set_ylabel('Temperature (°F)')
axs[0, 0].legend()
axs[0, 0].grid(True)

# Plot 2: Precipitation and Snow Depth (PRCP and SNWD) with dual y-axes
ax1 = axs[0, 1]
ax2 = ax1.twinx()
ax1.bar(df.index, df['PRCP'], label='Precipitation', color='blue', alpha=0.5)
ax2.plot(df.index, df['SNWD'], label='Snow Depth', color='red')
ax1.set_title('Precipitation and Snow Depth')
ax1.set_ylabel('Precipitation (inches)', color='blue')
ax2.set_ylabel('Snow Depth (inches)', color='red')
ax1.tick_params(axis='y', labelcolor='blue')
ax2.tick_params(axis='y', labelcolor='red')
# Combine legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
ax1.grid(True)

# Plot 3: Wind Speed (AWND and WSFI)
axs[1, 0].plot(df.index, df['AWND'], label='Average Wind Speed')
axs[1, 0].plot(df.index, df['WSFI'], label='Fastest Wind Speed')
axs[1, 0].set_title('Wind Speed')
axs[1, 0].set_ylabel('Speed (mph)')
axs[1, 0].legend()
axs[1, 0].grid(True)

# Plot 4: Water Equivalent of Snow Depth (WESD)
axs[1, 1].plot(df.index, df['WESD'], label='Water Equiv. Snow Depth', color='green')
axs[1, 1].set_title('Water Equivalent of Snow Depth')
axs[1, 1].set_ylabel('Inches')
axs[1, 1].legend()
axs[1, 1].grid(True)

# Set x-labels and rotate dates for readability
for ax in axs.flat:
    ax.set_xlabel('Date')
    ax.tick_params(axis='x', rotation=45)

# Adjust layout to prevent overlap and display the plot
plt.tight_layout()
plt.show()