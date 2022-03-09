# importing pandas as pd
import pandas as pd

# Create the series
series = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])

newSeries = series.map(lambda x: x[0].upper() + x[1:-1] + x[-1])

print(newSeries)
