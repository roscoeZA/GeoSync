import os
import csv

class SavedRepos(object):
    def __init__(self):
        """

        :return:
        """
        self.fname = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'saved_repos.csv')
        self.saved_repos_list=[]

    def get_fields(self):
        if os.path.isfile(self.fname):
            with open(self.fname, 'r+b') as csvfile_in:
                reader = csv.reader(csvfile_in, delimiter=',', quotechar='|')
                for line in reader:
                    self.saved_repos_list.append(line[0])#[0]
        else:
            with open(self.fname, 'w+b') as csvfile:
                csv.writer(csvfile)
        return self.saved_repos_list

    def set_fields(self, dir):
        # self.repo_dict.append(new_repo)
        # self.repo_dict.update({new_repo: new_dir})
        #self.repo_dict[new_repo] = [new_dir]
        if dir != "":
            self.saved_repos_list.append(dir)
            with open(self.fname, 'w+b') as csvfile:
                writer = csv.writer(csvfile, delimiter = ",")
                for item in self.saved_repos_list:
                    writer.writerow([item])


    def delete(self, index):
        self.saved_repos_list.pop(index)
        print self.saved_repos_list
        # for index in range(len(saved_repos)):
        #     dlg.ui.txtCurrentRepo.addItem(saved_repos[index])
        with open(self.fname, 'w+b') as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            for item in self.saved_repos_list:
                print 'item: ' + item
                writer.writerow([item])
