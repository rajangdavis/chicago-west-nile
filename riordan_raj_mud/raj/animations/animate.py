# Inspired by https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
# I opted to use ffmpeg for animations
# because that is what matplotlib uses under the hood
# and I can get a printout of the progress of creating the animations

# Import dependencies for generating plots
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Import chart and map data
spray = pd.read_csv("../dsi5/project-4/data/spray.csv").drop_duplicates().dropna()
train = pd.read_csv("../dsi5/project-4/data/train.csv").drop_duplicates().dropna()
mapdata = np.loadtxt("../dsi5/project-4/data/mapdata_copyright_openstreetmap_contributors.txt")

# Clean up data for use in charts
# Set each dataframe to use a datetime index
spray.drop(columns=["Time"], inplace=True)
spray.Date = pd.to_datetime(spray.Date)
spray.set_index('Date',inplace=True)

mosquitos = train[['Longitude', 'Latitude','NumMosquitos','Date']]
mosquitos.Date = pd.to_datetime(mosquitos.Date)
mosquitos_counts = mosquitos.groupby('Date')['NumMosquitos'].sum()
mosquitos.set_index("Date", inplace=True)
mosquitos["Counts"] = mosquitos_counts

west_nile = train[train['WnvPresent'] ==1 ][['Longitude', 'Latitude',"Date","WnvPresent"]]
west_nile.Date = pd.to_datetime(west_nile.Date)
west_nile_counts = west_nile.groupby(['Date'])['WnvPresent'].sum()
west_nile.set_index("Date", inplace=True)
west_nile["Counts"] = west_nile_counts

# Get a list of cleaned up dates
# of all of the datasets
indices = list(spray.index) + list(mosquitos.index) + list(west_nile.index)
dates = list(map(lambda x: str(x).replace(" 00:00:00",""), sorted(list(set(indices)))))

# Need to create unique years, months, days dates
# to loop through like a small clock
years, months, days = [sorted(list(set(map(lambda x: x.split("-")[i], dates)))) for i in range(0,3)]

# Create Legend values
spray_legend = mpatches.Patch(color='blue', label='Spray', alpha=0.5)
num_mosquitos_legend = mpatches.Patch(color='orange', label='Number of Mosquitos', alpha=0.5)
west_nile_legend = mpatches.Patch(color='red', label='West Nile Virus', alpha=0.5)

# Loop through each year, month, and day and create a new plot
# and save for later use
for year in years:
	# We are keeping a track of count
	# because of how ffmpeg will combine images
	# images needed to be ordered numerically
	count = 1
	fig = plt.figure(figsize=(12, 10))
	aspect = mapdata.shape[0] * 1.0 / mapdata.shape[1]
	lon_lat_box = (-88, -87.5, 41.6, 42.1)
	plt.imshow(mapdata, 
		cmap=plt.get_cmap('gray'), 
		extent=lon_lat_box, 
		aspect=aspect,
		animated=True
	)
	plt.legend(handles=[spray_legend, num_mosquitos_legend, west_nile_legend], loc=0, title="Legend")
	for month in months:
		for day in days:
			plt.title(f"{year}-{month}-{day}", fontdict={"fontsize":30})
			# Adding a print statement so I can see what progress I am getting
			print(f"Creating frame for {year}-{month}-{day}")
	        # Skip "31" for June and September
	        # Otherwise we will be out of bounds
			if day == "31" and (month == "06" or month == "09"):
				continue            
			# There is only spray data for 2011 and 2013
			# so don't plot the spray data for 2009 and 2007
			if int(year) > 2009:
				spray_subset = spray[(spray.index <=f"{year}-{month}-{day}") & (spray.index >=f"{int(year) - 1}")]
				spray_mask = (spray_subset['Longitude'] >= -88.0)
				spray_locations = spray_subset[spray_mask][['Longitude', 'Latitude']].dropna().values
				plt.scatter(spray_locations[:,0], spray_locations[:,1], marker='x', color="blue", alpha=0.01)
	        
	        # Mosquitos and Westnile virus have their counts multiplied
	        # This is so the size of plotted points are exaggerated
	        # based on the counts for that day
			mosquitos_subset = mosquitos[(mosquitos.index <=f"{year}-{month}-{day}") & (mosquitos.index >=f"{int(year) - 1}")]
			mosquitos_locations = mosquitos_subset[['Longitude', 'Latitude','NumMosquitos']].dropna().values
			plt.scatter(mosquitos_locations[:,0], mosquitos_locations[:,1], marker='o', color="orange", s=mosquitos_locations[:,2]**2, alpha=0.01)

			west_nile_subset = west_nile[(west_nile.index <=f"{year}-{month}-{day}") & (west_nile.index >=f"{int(year) - 1}")]
			west_nile_locations = west_nile_subset[['Longitude', 'Latitude','WnvPresent']].dropna().values
			plt.scatter(west_nile_locations[:,0], west_nile_locations[:,1], marker='*', color="red", s=west_nile_locations[:,2]*20)
			fig.savefig(f"./pictures/{year}-{count}.png", bbox_inches='tight')
			
			# Once we get to last day,
			# We will reset the count
			# This is so we can combine the images
			# into one year
			if month == 10 and day == 31:
				count = 1
			else:
				count += 1

# Used the following bash command to combine the pictures
# and make a webm video of each year
# for i in {2007,2009,2011,2013}; do ffmpeg -i ./pictures/$i-%d.png -filter:v "setpts=3*PTS" $i.webm; done

# Used the following bash command to convert the videos from webm to mp4
# for i in {2007,2009,2011,2013}; do ffmpeg -i $i.webm -c:v copy $i.mp4; done