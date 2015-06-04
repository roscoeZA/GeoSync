import csv
from qgis.utils import iface
from qgis.core import QgsMapLayerRegistry
from datetime import datetime
from geogigpy import geogig
from geogigpy.repo import Repository
from geogigpy.geogigexception import GeoGigException
import os
import file_to_memory
from CommitDialog import CommitDialog

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
    for t in repos.trees:
        print "t: %s" % t.path
        if t.path not in ("layer_statistics", "views_layer_statistics", "virts_layer_statistics"):
            geojson_path=os.path.join(filepath, t.path + '.geojson')
            try:
                repos.exportgeojson('HEAD', t.path, os.path.join('HEAD', t.path,
                                                                 geojson_path))
            except GeoGigException, e:
                'Error in exporting: %s' % e
                continue
    # all_geojson_to_memory('/tmp/b')

def import_all_geojosn(repos, dirpath):
    for f in os.listdir(dirpath):
        if f.endswith(".geojson"):
            geojson_path = os.path.join(dirpath, f)
            try:
                # geojsonfile, add = False, dest = None, idAttribute = None, geomName = None, force=False
                repos.importgeojson(geojson_path, dest=os.path.splitext(f)[0], force=True)
            except GeoGigException, e:
                print e
                continue


def all_geojson_to_memory(dirpath):
    for f in os.listdir(dirpath):
        if f.endswith(".geojson"):
            filename = os.path.splitext(f)[0]
            geojson_path = os.path.join(dirpath, f)
            memory_layer=file_to_memory.geojson_to_memory(geojson_path, filename)
            QgsMapLayerRegistry.instance().addMapLayer(memory_layer)


def delete_files(dirpath):
    for f in os.listdir(dirpath):
        if f.endswith(".geojson"):
            print 'Deleted: %s' % f
            os.remove(os.path.join(dirpath,f))


def add_commit(repos, name, email, message):
    name, email, message = ["","",""]
    message += " " + str(datetime.now())
    repos.config(geogig.USER_NAME, name)
    repos.config(geogig.USER_EMAIL, email)
    repos.addandcommit(message)


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


def get_map_layers():#list type is wrong
    layer_list = []
    legend = iface.legendInterface()
    layers = legend.layers()
    for layer in layers:
        # layer_list.append(layer.name())
        layer_list.append(layer)
    return layer_list

class ConfigRepos(object):
    def get_recent_repos():
        # dirpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "saved_repos.csv")
        saved_repos = os.path.join(os.path.dirname(os.path.realpath(__file__)), "saved_repos.csv")

        if os.path.isfile(saved_repos):
            with open(saved_repos, 'r+b') as csvfile_in:
                reader = csv.reader(csvfile_in)
                repo_dict = dict(row[:2] for row in reader if row)

        else:
            with open(saved_repos, 'w+b') as csvfile:
                fieldnames = ['dir', 'remotes']
                writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
                writer.writerow({'dir': '/tmp/test', 'remotes': 'localhost'})
                reader = csv.reader(csvfile)
                repo_dict = dict(row[:2] for row in reader if row)
        print saved_repos
        print repo_dict
        return repo_dict

    def set_recent_repos(self):
        new_repo = self.txtRemote.text()
        new_dir = self.txtDir.text()
        # self.repo_dict.append(new_repo)
        self.repo_dict.update({new_repo: new_dir})
        #self.repo_dict[new_repo] = [new_dir]
        self.save()
        self.reload()

    def save_recent_repos(self):
        with open(self.fname, 'w+b') as csvfile:
            writer = csv.writer(csvfile)
            for key, value in self.repo_dict.items():
                writer.writerow([key, value])

    def reload_recent_repos(self):
        self.listRepos.clear()
        self.repo_dict = {}
        self.get_fields()
        for item in self.repo_dict:
            self.listRepos.addItem(item + " : " + self.repo_dict[item])