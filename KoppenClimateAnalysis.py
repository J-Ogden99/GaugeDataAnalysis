import geopandas as gpd
import pandas as pd

map_table = pd.read_csv('KoppenGridCodeMap.csv', header=None)
koppen_file = 'KoppenChartProjected/c2076_2100_A1FI.shp'
koppen_chart = gpd.read_file(koppen_file)
koppen_chart = gpd.GeoDataFrame(koppen_chart.merge(map_table, left_on='GRIDCODE', right_on=0)
                                .drop(columns=0)\
                                .rename(columns={1: 'KOPPENCLASS'}),
                                geometry='geometry')
koppen_chart.to_file('KoppenChart2079.gpkg', driver='GPKG')