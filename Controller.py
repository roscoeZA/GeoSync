from qgis.utils import iface
from qgis.core import QgsMapLayerRegistry
from geogigpy.repo import Repository
from geogigpy.geogigexception import GeoGigException
import os
import file_to_memory
#import pydevd

def connect2repo(path, remote='localhost', repo_type='local'):
    print 'connect 2 repo %s' % path
    if os.path.isdir(os.path.join(path, '.geogig')):
        print "Set to existing repo"
        repos = Repository(path)
        return repos
    else:
        if repo_type == "remote":
            repos = Repository.newrepofromclone(remote, path)
            print "New repo from clone"
        else:
            repos = Repository(path, init=True)
            print "New repo initialized at : %s" % path
    return repos


def export_to_geojson(repos, filepath):
    # export files to geojson
    for t in repos.trees:
        if t.path not in ("layer_statistics", "views_layer_statistics", "virts_layer_statistics"):

            geojson_path=os.path.join(filepath, t.path + '.geojson')
            try:
                repos.exportgeojson('HEAD', t.path, os.path.join('HEAD', t.path,
                                                                 geojson_path))
            except GeoGigException, e:
                'Error in exporting: %s' % e
                continue
    # all_geojson_to_memory('/tmp/b')


def all_geojson_to_memory(dirpath):
    for f in os.listdir(dirpath):
        if f.endswith(".geojson"):
            filename = os.path.splitext(f)[0]
            geojson_path = os.path.join(dirpath, f)
            memory_layer=file_to_memory.geojson_to_memory(geojson_path, filename)
            QgsMapLayerRegistry.instance().addMapLayer(memory_layer)


def delete_file(filepath):
    print "F: " + filepath
    os.remove(filepath)


def save_geojson_changes(filepath):
    filepath = "somewhere"
    print filepath


def all_legend_layers():
    legend = iface.legendInterface()
    layers = legend.layers()
    list_layers = []
    for each_layer in layers:
        list_layers.append(each_layer.name())
    return list_layers


def get_map_layers():
    layer_list = []
    for layer in QgsMapLayerRegistry.instance().mapLayers():
        layer_list.append(layer)
    return layer_list