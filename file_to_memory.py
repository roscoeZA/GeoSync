__author__ = 'roscoe'
from qgis.core import QgsVectorLayer
from qgis.core import QgsMapLayerRegistry
from qgis.core import QgsFeature, QgsField
import os

def geojson_to_memory(path, name):
    my_WkbType = {
        'Unknown': 0,
         'Point': 1,
         'LineString': 2,
         'Polygon': 3,
         'MultiPoint': 4,
         'MultiLineString': 5,
         'MultiPolygon': 6,
         'NoGeometry': 7,
         'Point25D': 8,
         'LineString25D': 9,
         'Polygon25D': 10,
         'MultiPoint25D': 11,
         'MultiLineString25D': 12,
         'MultiPolygon25D': 13}

    # for i,j in my_WkbType.items():
    #     #print i + " : " + str(j)

    my_rev_WkbType = {v: k for k, v in my_WkbType.items()}
    # for i,j in my_WkbType.items():
    #     #print i + " : " + str(j)
    #print 'Path to geojson: %s' % path
    input_layer=QgsVectorLayer(path,
                               "input_layer", "ogr")
    print 'path: %s' % path
    print 'input_layer %s' % input_layer.name()
    dp = input_layer.dataProvider()
    QGisWKBType = dp.geometryType()
    #print 'QGisWKBType: ' + str(QGisWKBType)
    EPSG_code = int(dp.crs().authid().split(":")[1])
    print str(EPSG_code)

    destination_layer = QgsVectorLayer(
        my_rev_WkbType[QGisWKBType] + '?crs=epsg:' + str(EPSG_code) + '&index=yes',
        name,
        'memory')
    destination_layer_data_provider = destination_layer.dataProvider()

    input_layer_attrib_names = input_layer.dataProvider().fields()

    oldattributeList = input_layer.dataProvider().fields().toList()
    newattributeList = []
    for attrib in oldattributeList:
        if destination_layer.fieldNameIndex(attrib.name()) == -1:
            newattributeList.append(QgsField(attrib.name(), attrib.type()))

    destination_layer_data_provider.addAttributes(newattributeList)
    destination_layer.updateFields()

    destination_layer.startEditing()
    # cfeature = QgsFeature()
    cfeatures = []
    xfeatures = input_layer.getFeatures()
    for xfeature in xfeatures:
        xgeometry = xfeature.geometry()
        cfeature_Attributes = []
        cfeature_Attributes.extend(xfeature.attributes())
        cfeature = QgsFeature()
        cfeature.setGeometry(xgeometry)
        cfeature.setAttributes(cfeature_Attributes)
        cfeatures.append(cfeature)

    destination_layer.addFeatures(cfeatures)
    destination_layer.commitChanges()
    return destination_layer

    # #print details of the feature.
    # f = QgsFeature()
    # features = destination_layer.getFeatures()
    # for f in features:
    #     #print "F:", f.id(), f.attributes(), f.geometry().asPoint()
