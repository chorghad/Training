import geopandas as gpd
import fiona
 
gdb_path = "C:/Hiraman/AI_ML_Traning/Python_Traning/Python_Training/SAU_RNR_Only.gdb"  # Replace with your GDB file path
 
# List all layer names in the geodatabase
layers = fiona.listlayers(gdb_path)
 
print("Feature classes in the GDB:")
for layer in layers:
    print(layer)
 
# Read a specific layer to a GeoDataFrame
selected_fc = "name_of_feature_class"  # Replace with the desired feature class name
if selected_fc in layers:
    gdf = gpd.read_file(gdb_path, layer=selected_fc)
    print("\nSelected feature class:")
    print(gdf.head())
else:
    print(f"The layer {selected_fc} does not exist in the geodatabase.")