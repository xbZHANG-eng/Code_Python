# import system modules 
import arcpy
import os
#作成したいフォルダーのパス
folder_path = r"C:/GIS_temp/"
#フォルダーが存在しない場合に作成
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    
#プロジェクトとマップの取得
aprx = arcpy.mp.ArcGISProject("CURRENT")
map=aprx.activeMap

for lyr in map.listLayers():
    if lyr.name== "test":
        print(f"dataSource: {lyr.dataSource}")

shp_path = folder_path + "verPont.shp"
if arcpy.Exists(shp_path):
    arcpy.management.Delete(shp_path)

# Set local variables

#inFeatures = r"C:/data/test.shp"
inFeatures = arcpy.GetParameterAsText(0)

outFeatureClass = shp_path

# Execute FeatureVerticesToPoints
inputLayer = arcpy.FeatureVerticesToPoints_management(inFeatures, outFeatureClass, "ALL")

#れいやーをマップに追加
symbollyr = "symbolC.lyrx"
shp_path1=folder_path + symbollyr
symbologyLayer = arcpy.mp.LayerFile(shp_path1)

map.addLayer(symbologyLayer)

