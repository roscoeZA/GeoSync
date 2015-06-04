import os
import csv
from Ui_GeoSync import _fromUtf8
from PyQt4.Qt import *
from Controller import connect2repo
from SavedRepos import SavedRepos


class RepoDialog(QDialog):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Manage Repositories')
        self.repos_config = SavedRepos()
        self.initUI()
        self.btnOk.clicked.connect(self.hide)
        self.btnRemove.clicked.connect(self.delete_repo)
        self.btnAdd.clicked.connect(self.add_repo)

    def initUI(self):
        self.h_box = QHBoxLayout(self)
        self.v_box = QVBoxLayout(self)
        self.v_box.addStretch(1)
        self.h_box.addStretch(1)

        self.lstRepos = QListWidget(self)
        self.lstRepos.setObjectName('lstRepos')
        self.btnAdd = QPushButton(self)
        self.btnAdd.setText('+')
        self.btnRemove = QPushButton(self)
        self.btnRemove.setText('-')
        self.btnRemove.setStyleSheet('QPushButton {color: red; font-weight: bold; font-size: 20px}')
        font = QFont(self)
        font.setFamily(_fromUtf8("Arial Black"))
        self.btnAdd.setStyleSheet('QPushButton {color: green; font-weight: bold; font-size: 20px}')
        self.btnOk = QPushButton(self)
        self.btnOk.setText("Ok")
        self.btnOk.setObjectName(_fromUtf8('btnOk'))

        self.h_box.addWidget(self.lstRepos)

        self.h_box.addLayout(self.v_box)
        self.v_box.addWidget(self.btnAdd)
        self.v_box.addWidget(self.btnRemove)
        self.v_box.addWidget(self.btnOk)

        repo_list = self.repos_config.get_fields()
        for item in repo_list:
            self.lstRepos.addItem(item)

    def delete_repo(self):
        index = self.lstRepos.row(self.lstRepos.currentItem())
        self.repos_config.delete(index)
        self.reload_repos()

    def add_repo(self):
        self.current_repo_dir = str(QFileDialog.getExistingDirectory(None, "Select a directory"))
        self.repos_config.set_fields(self.current_repo_dir)
        self.reload_repos()

    def reload_repos(self):
        self.lstRepos.clear()
        for repo in self.repos_config.get_fields():
            self.lstRepos.addItem(repo)

