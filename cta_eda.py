import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel(r"E:\City Traffic DA2\Project_dataset_city_traffic_accident.xlsx")


df.head(5)
df.tail(6)

df.shape
df.sample
df.head

df.info()
df.describe()


# Convert these to category — they are ordered labels
df['day_of_week'] = df['day_of_week'].astype('object')
df['hour_of_day'] = df['hour_of_day'].astype('object')

df['location_id'].nunique()
df['season'].nunique()

df.groupby('has_signal')['green_duration_s'].count()
df.groupby('has_signal')['red_duration_s'].count()
df.groupby('has_signal')['yellow_duration_s'].count()




df['accident_occurred'].value_counts()

df.groupby('accident_occurred')['veh_count_at_accident'].describe()


df[['vehicle_count_per_hr','veh_count_at_accident']].corr()


(df['vehicle_count_per_hr'] == df['veh_count_at_accident']).sum()

df[df['vehicle_count_per_hr'] != df['veh_count_at_accident']]

df['vehicle_count_per_hr'] = df['vehicle_count_per_hr'].fillna(df['veh_count_at_accident'])


df['vehicle_count_per_hr'].isnull().sum()


df.drop(columns=['veh_count_at_accident'], inplace=True)

df.shape
df.columns

df['weather'].unique()
df['weather'].nunique()


df.isnull().sum().sort_values(ascending=False)



(df['peak'] == df['is_peak']).sum()


df[df['peak'].isna()]

df.loc[df['peak'].isna(), ['peak','is_peak']]


df[['peak','is_peak']].corr()
(df['peak'] == df['is_peak']).sum()

df.drop(columns=['peak'],inplace=True)

df.shape


pd.crosstab(df['signal_data_quality_flag'], df['accident_occurred'])
df.drop('signal_data_quality_flag', axis=1, inplace=True)

pd.crosstab(df['traffic_data_quality_flag'], df['accident_occurred'])
df.drop('traffic_data_quality_flag', axis=1, inplace=True)

df.shape
df.isnull().sum().sort_values(ascending=False)



(df['timestamp'].dt.hour == df['hour_of_day']).all()
(df['timestamp'].dt.dayofweek == df['day_of_week']).all()
df.groupby('location_id')['timestamp'].count()
    


df['lighting']
df['lighting'].unique()
df['lighting'].nunique()




pd.crosstab(df['lighting'], df['accident_occurred'], normalize='index')
pd.crosstab(df['lighting'], df['accident_occurred'], normalize='index').plot(kind='bar')
plt.show()


pd.crosstab(df['lighting'], df['accident_occurred'], normalize='index').plot(kind='bar')

plt.title("Accident Probability by Lighting Condition")
plt.xlabel("Lighting Condition")
plt.ylabel("Proportion")
plt.legend(title="Accident Occurred")

plt.show()


df[df['lighting'].isna()][['timestamp','hour_of_day','accident_occurred']]

df['lighting'] = df['lighting'].fillna('Day')

df['lighting'].isnull().sum()


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 5))

# Plot histogram for each group
for accident, group in df.groupby('accident_occurred'):
    sns.histplot(
        group['lane_count'].dropna(),
        kde=True,
        label=f'Accident: {accident}',
        alpha=0.5
    )

plt.title("Lane Count Distribution by Accident Occurrence")
plt.xlabel("Lane Count")
plt.ylabel("Frequency")
plt.legend(title="Accident Occurred")
plt.tight_layout()
plt.savefig('histogram_lane_count_by_accident.png', dpi=150, bbox_inches='tight')
plt.show()


df['weather']
df['weather'].unique()
df['weather'].nunique()


df[df['weather'].isna()][['timestamp','hour_of_day','lighting','accident_occurred']]

df['weather'] = df['weather'].fillna('Unknown')
df['weather'].isnull().sum()
pd.crosstab(df['weather'], df['accident_occurred'], normalize='index')

pd.crosstab(df['weather'], df['accident_occurred'], normalize='index').plot(kind='bar')

plt.title("Accident Probability by Weather Condition")
plt.xlabel("Weather")
plt.ylabel("Proportion")
plt.legend(title="Accident Occurred")

plt.show()



df['weather'].value_counts()



df.groupby('weather')['accident_occurred'].mean().plot(kind='bar')

plt.title("Accident Probability by Weather")
plt.ylabel("Accident Probability")
plt.show()



df['avg_speed_kmph'].describe()

df[df['avg_speed_kmph'] < 0]


df[df['avg_speed_kmph'] < 0][['avg_speed_kmph','accident_occurred','vehicle_count_per_hr','timestamp']]
df[df['avg_speed_kmph'] > 150][['avg_speed_kmph','accident_occurred','speed_limit_kmph','vehicle_count_per_hr']]
df[df['avg_speed_kmph'] > 150]['accident_occurred'].value_counts()

df.loc[df['avg_speed_kmph'] < 0, 'avg_speed_kmph'] = None
df.loc[df['avg_speed_kmph'] > 150, 'avg_speed_kmph'] = None

df['avg_speed_kmph'] = df['avg_speed_kmph'].fillna(df['avg_speed_kmph'].median())

df['avg_speed_kmph'].isnull().sum()

import seaborn as sns
sns.boxplot(x=df['avg_speed_kmph'])
sns.boxplot(x='accident_occurred', y='avg_speed_kmph', data=df)
plt.show()


sns.scatterplot(
    x='vehicle_count_per_hr',
    y='avg_speed_kmph',
    hue='accident_occurred',
    data=df
)
plt.show()



df['traffic_bin'] = pd.qcut(df['vehicle_count_per_hr'], 5)

df.groupby('traffic_bin')['accident_occurred'].mean()


df.groupby('traffic_bin')['accident_occurred'].mean().plot(kind='bar')
plt.ylabel("Accident Probability")
plt.title("Accident Probability by Traffic Density")
plt.show()



df.shape
df.columns
df['traffic_bin'].head(3)


df.groupby(pd.qcut(df['vehicle_count_per_hr'], 5))['accident_occurred'].mean()
sns.boxplot(x='traffic_bin', y='avg_speed_kmph', data=df)    
plt.show()

df.drop(columns=['traffic_bin'], inplace=True)


df.groupby('has_signal')[['green_duration_s','red_duration_s']].count()
df.groupby('has_signal')[['green_duration_s','red_duration_s','yellow_duration_s']].count()











df.groupby('has_signal')[['green_duration_s','red_duration_s','yellow_duration_s','cycle_time_s','violations_count']].count()

df['has_signal'].value_counts()


pd.crosstab(df['has_signal'], df['accident_occurred'], normalize='index')



df.groupby('has_signal')['vehicle_count_per_hr'].mean()

df.groupby('has_signal')['avg_speed_kmph'].mean()




df['calc_cycle'] = df['green_duration_s'] + df['yellow_duration_s'] + df['red_duration_s']

df[['cycle_time_s','calc_cycle']].head()


(df['cycle_time_s'] - df['calc_cycle']).describe()

(df['cycle_time_s'] != df['calc_cycle']).sum()
((df['cycle_time_s'] != df['calc_cycle']).sum() / len(df)) * 100

df.groupby('accident_occurred')[['severity','vehicles_involved']].count()

signals = df['has_signal'] == True

((df['cycle_time_s'] != df['calc_cycle']) & signals).sum()
((df['cycle_time_s'] != df['calc_cycle']) & signals).sum() / signals.sum() * 100


df.drop(columns=['calc_cycle'], inplace=True)


# Signal presence vs accident occurrence
# 1️ Numerical comparison
pd.crosstab(df['has_signal'], df['accident_occurred'], normalize='index')

# 2️ Visualize accident probability by signal presence

sns.barplot(
    x='has_signal',
    y='accident_occurred',
    data=df
)

plt.title("Accident Probability by Signal Presence")
plt.xlabel("Signal Present")
plt.ylabel("Accident Probability")
plt.show()

# 3️ Visualize accident counts (another useful view)
sns.countplot(
    x='has_signal',
    hue='accident_occurred',
    data=df
)

plt.title("Accident Counts by Signal Presence")
plt.xlabel("Signal Present")
plt.ylabel("Count")
plt.show()




ax = sns.countplot(
    x='has_signal',
    hue='accident_occurred',
    data=df
)

plt.title("Accident Counts by Signal Presence")
plt.xlabel("Signal Present")
plt.ylabel("Count")

# Add data labels
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{int(height)}',
                (p.get_x() + p.get_width() / 2., height),
                ha='center', va='bottom')

plt.show()  



ax = sns.countplot(
    x='has_signal',
    hue='accident_occurred',
    data=df
)

plt.title("Accident Counts by Signal Presence")
plt.xlabel("Signal Present")
plt.ylabel("Count")

# total number of rows
total = len(df)

# Add count + percentage labels
for p in ax.patches:
    count = int(p.get_height())
    percentage = 100 * count / total
    
    ax.annotate(
        f'{count}\n({percentage:.1f}%)',
        (p.get_x() + p.get_width()/2., count),
        ha='center', va='bottom'
    )

plt.show()



# Traffic density vs speed vs accidents (scatter plot)
sns.scatterplot(
    x='vehicle_count_per_hr',
    y='avg_speed_kmph',
    hue='accident_occurred',
    data=df
)
plt.title("Traffic Density vs Speed vs Accidents")
plt.show()


# Speed distribution by accident occurrence (boxplot)
sns.boxplot(
    x='accident_occurred',
    y='avg_speed_kmph',
    data=df
)
plt.title("Speed Distribution by Accident Occurrence")
plt.show()

#  Hour of day vs accident probability (line chart)


df.groupby('hour_of_day')['accident_occurred'].mean().plot(
    marker='o',
    figsize=(8,4)
)

plt.title("Accident Probability by Hour of Day")
plt.xlabel("Hour of Day")
plt.ylabel("Accident Probability")
plt.grid(True)
plt.show()

# Weather vs accident probability (bar chart)
sns.barplot(
    x='weather',
    y='accident_occurred',
    data=df
)
plt.title("Accident Probability by Weather")
plt.show()

# Lighting vs accidents (stacked bar and bar)
pd.crosstab(
    df['lighting'],
    df['accident_occurred'],
    normalize='index'
).plot(kind='bar', stacked=True)

plt.title("Accidents by Lighting Condition")
plt.show()

pd.crosstab(
    df['lighting'],
    df['accident_occurred'],
    normalize='index'
).plot(kind='bar', )

plt.title("Accidents by Lighting Condition")
plt.show()


# Blackspot score vs accidents (boxplot)
sns.boxplot(
    x='accident_occurred',
    y='blackspot_score',
    data=df
)
plt.title("Blackspot Score vs Accident Occurrence")
plt.show()

# Correlation heatmap (overall relationships)
import seaborn as sns

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True, 
    cmap='coolwarm'
)
plt.title("Correlation Matrix")
plt.show()


# Geographic accident map (if coordinates are useful)
sns.scatterplot(
    x='longitude',
    y='latitude',
    hue='accident_occurred',
    data=df
)
plt.title("Accident Locations")
plt.show()

# Accidents by day of week 
df.groupby('day_of_week')['accident_occurred'].mean().plot(marker='o')

plt.title("Accident Probability by Day of Week")
plt.xlabel("Day")
plt.ylabel("Accident Probability")
plt.show()

#  Traffic density vs accidents
sns.boxplot(
    x='accident_occurred',
    y='vehicle_count_per_hr',
    data=df
)

plt.title("Traffic Density vs Accident Occurrence")
plt.show()

#  Speed vs accidents
sns.boxplot(
    x='accident_occurred',
    y='avg_speed_kmph',
    data=df
)

plt.title("Speed vs Accident Occurrence")
plt.show()


#  infrasructure risk
sns.boxplot(
    x='accident_occurred',
    y='blackspot_score',
    data=df
)
plt.show()



#  Traffic interaction plot
sns.scatterplot(
    x='vehicle_count_per_hr',
    y='avg_speed_kmph',
    hue='accident_occurred',
    data=df
)
plt.show()

#  correlation heatmap
sns.heatmap(df.corr(numeric_only=True), cmap='coolwarm')
plt.show()



df.groupby('hour_of_day')['accident_occurred'].mean().plot(
    marker='o',
    figsize=(8,4)
)

plt.title("Accident Probability by Hour of Day")
plt.xlabel("Hour of Day")
plt.ylabel("Accident Probability")
plt.grid(True)
plt.show()



# Find accident count per location
location_accidents = df[df['accident_occurred'] == True] \
    .groupby('location_id') \
    .size() \
    .sort_values(ascending=False)

location_accidents



# Identify the most dangerous location
top_location = location_accidents.idxmax()
top_location


# Filter data for that location
top_data = df[
    (df['location_id'] == top_location) &
    (df['accident_occurred'] == True)
]

top_data['hour_of_day'].value_counts()
top_data['cause'].value_counts()
top_data['severity'].value_counts()

print("Most dangerous location:", top_location)

print("\nTop accident hours:")
print(top_data['hour_of_day'].value_counts().head())

print("\nTop accident causes:")
print(top_data['cause'].value_counts().head())

df.shape

df.to_excel("E:\City Traffic DA2\Project_dataset_cleaned_data_city_traffic_accident.xlsx",index=False)


df.columns
df.info()


from scipy import stats
import pandas as pd

numeric_cols = df.select_dtypes(include='number').columns

moments = []

for col in numeric_cols:
    data = df[col].dropna()
    moments.append({
        'Column'   : col,
        'Mean'     : round(data.mean(), 2),
        'Median'   : round(data.median(), 2),
        'Mode'     : round(data.mode()[0], 2),  
        'Std Dev'  : round(data.std(), 2),
        'Variance' : round(data.var(), 2),
        'Skewness' : round(data.skew(), 2),
        'Kurtosis' : round(data.kurt(), 2),
        'Min'      : round(data.min(), 2),
        'Max'      : round(data.max(), 2),
    })

moments_df = pd.DataFrame(moments)
print(moments_df.to_string(index=False))


import matplotlib.pyplot as plt
import seaborn as sns
import math

# Automatically calculate grid size based on number of numeric columns
numeric_cols = df.select_dtypes(include='number').columns

n_cols = 3
n_rows = math.ceil(len(numeric_cols) / n_cols)

fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, n_rows * 4))
axes = axes.flatten()

for i, col in enumerate(numeric_cols):
    sns.histplot(df[col].dropna(), kde=True, ax=axes[i], color='steelblue')
    axes[i].set_title(
        f'{col}\nSkew: {df[col].skew():.2f} | Kurt: {df[col].kurt():.2f}',
        fontsize=10
    )
    axes[i].set_xlabel('')

# Hide any empty subplots at the end
for j in range(len(numeric_cols), len(axes)):
    axes[j].set_visible(False)

plt.suptitle(
    "Distribution of Numeric Columns with Skewness & Kurtosis",
    fontsize=14, y=1.02
)
plt.tight_layout()
plt.savefig('all_histograms.png', dpi=150, bbox_inches='tight')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import math

numeric_cols = df.select_dtypes(include='number').columns.tolist()

# Remove latitude and longitude if you don't want them
numeric_cols = [col for col in numeric_cols if col not in ['latitude', 'longitude']]

print(f"Numeric columns to analyze: {numeric_cols}")
print(f"Total: {len(numeric_cols)} columns")


#  histogram

n_cols = 3
n_rows = math.ceil(len(numeric_cols) / n_cols)

fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, n_rows * 4))
axes = axes.flatten()

for i, col in enumerate(numeric_cols):
    sns.histplot(df[col].dropna(), kde=True, ax=axes[i], color='steelblue')
    axes[i].set_title(
        f'{col}\nSkew: {df[col].skew():.2f} | Kurt: {df[col].kurt():.2f}',
        fontsize=10
    )
    axes[i].set_xlabel('')

for j in range(len(numeric_cols), len(axes)):
    axes[j].set_visible(False)

plt.suptitle("Histograms — All Numeric Columns", fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig('histograms_all.png', dpi=150, bbox_inches='tight')
plt.show()


#  boxplot

n_cols = 3
n_rows = math.ceil(len(numeric_cols) / n_cols)

fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, n_rows * 4))
axes = axes.flatten()

for i, col in enumerate(numeric_cols):
    sns.boxplot(x=df[col].dropna(), ax=axes[i], color='lightcoral')
    axes[i].set_title(
        f'{col}\nMedian: {df[col].median():.2f} | IQR: {(df[col].quantile(0.75) - df[col].quantile(0.25)):.2f}',
        fontsize=10
    )
    axes[i].set_xlabel('')

for j in range(len(numeric_cols), len(axes)):
    axes[j].set_visible(False)

plt.suptitle("Boxplots — All Numeric Columns", fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig('boxplots_all.png', dpi=150, bbox_inches='tight')
plt.show()






# scatter plot

scatter_pairs = [
    ('vehicle_count_per_hr', 'avg_speed_kmph'),
    ('blackspot_score',       'avg_speed_kmph'),
    ('vehicle_count_per_hr', 'violations_count'),
    ('avg_speed_kmph',        'blackspot_score'),
    ('green_duration_s',      'violations_count'),
    ('cycle_time_s',          'violations_count'),
]

n_cols = 2
n_rows = math.ceil(len(scatter_pairs) / n_cols)

fig, axes = plt.subplots(n_rows, n_cols, figsize=(14, n_rows * 5))
axes = axes.flatten()

for i, (x_col, y_col) in enumerate(scatter_pairs):
    sns.scatterplot(
        x=x_col,
        y=y_col,
        hue='accident_occurred',
        data=df,
        ax=axes[i],
        alpha=0.5,
        palette={True: 'red', False: 'steelblue'}
    )
    axes[i].set_title(f'{x_col} vs {y_col}', fontsize=10)
    axes[i].legend(title='Accident', fontsize=8)

for j in range(len(scatter_pairs), len(axes)):
    axes[j].set_visible(False)

plt.suptitle("Scatter Plots — Key Variable Pairs vs Accident Occurred", fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig('scatter_plots.png', dpi=150, bbox_inches='tight')
plt.show()

#  correlation heatmap

plt.figure(figsize=(12, 10))

corr = df[numeric_cols].corr()

mask = sns.heatmap(
    corr,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    center=0,
    linewidths=0.5,
    annot_kws={'size': 8}
)

plt.title("Correlation Heatmap — Numeric Columns", fontsize=14)
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=150, bbox_inches='tight')
plt.show()


#  Distribution Comparison (Histogram by Accident)
n_cols = 3
n_rows = math.ceil(len(numeric_cols) / n_cols)

fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, n_rows * 4))
axes = axes.flatten()

for i, col in enumerate(numeric_cols):
    for accident, group in df.groupby('accident_occurred'):
        sns.histplot(
            group[col].dropna(),
            kde=True,
            ax=axes[i],
            label=f'Accident: {accident}',
            alpha=0.5
        )
    axes[i].set_title(f'{col} by Accident Occurred', fontsize=10)
    axes[i].legend(fontsize=7)
    axes[i].set_xlabel('')

for j in range(len(numeric_cols), len(axes)):
    axes[j].set_visible(False)

plt.suptitle("Histograms — Numeric Columns by Accident Occurrence", fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig('histograms_by_accident.png', dpi=150, bbox_inches='tight')
plt.show()

# code for mysql

from sqlalchemy import create_engine

# MySQL connection

username = "root"
password = "YOUR PASSWORD"
host = "localhost"
port = "3306"
database = "city_traffic_db"
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# write dataframe to MySQL
table_name = "traffic_data"
df.to_sql(table_name,engine,if_exists="replace",index = False)

pd.read_sql("select * from traffic_data limit 5;",engine)

