from tinydb import TinyDB, Query
import re


db = TinyDB('db.json').table('requirements')

#Stores the property of each requirement
class Requirement:
    def __init__(self, definition = "", sources = [], dimensions = [], processes = [], structures = [], constraints = []):
        self.definition = definition
        self.sources = sources
        self.dimensions = dimensions
        self.processes = processes
        self.structures = structures
        self.constraints = constraints


    @staticmethod
    def fromDict(dictionary):
        self = Requirement()
        self.__dict__.update(dictionary)
        if not hasattr(self, 'id'):
            self.id = db.get(Query().definition == self.definition).doc_id
        return self

#Function to insert a new requirement in the db.json file
    def insert(self):
        self.id = len(db) + 1
        db.insert(self.__dict__)
#Function to update the existing requirements of th db.josn file
    def update(self, definition = "", sources = "", dimensions = "", processes = [], structures = [], constraints = [], implementations = [], constraints_links = [], criteria = []):
        self.definition = definition
        self.sources = sources
        self.dimensions = dimensions
        self.processes = re.sub(r'[A-Z]\d+.\d\s:\s', '', processes).split("\n")
        self.structures = re.sub(r'[A-Z]\d+.\d\s:\s', '', structures).split("\n")
        self.constraints = re.sub(r'[A-Z]\d+.\d\s:\s', '', constraints).split("\n")
        links = Link(implementations, constraints_links, criteria).__dict__
        self.links = links
        db.update(self.__dict__, doc_ids=[self.id])
#Function to delete a requirement
    def delete(self):
        db.remove(doc_ids=[self.id])

    def format_property(self, prop):
        arr = self.__dict__[prop]
        return "\n" + "\n".join([f"{prop[0].upper()}{self.id}.{(arr.index(el)) + 1} : {el}" for el in arr])

class Link:
    def __init__(self, implementations = [], constraints = [], criteria = []):
        self.implementations = implementations
        self.constraints = constraints
        associations = AssociationLink(criteria).__dict__
        self.associations = associations


class AssociationLink:
    def __init__(self, criteria = []):
        self.criteria = criteria

def get_requirements():
    return db.all()

def get_processes():
    processes = [req['processes'] for req in get_requirements()]
    return [{f"{processes.index(sublist) + 1}.{sublist.index(proc) + 1}" : proc} for sublist in processes for proc in sublist]

def get_links():
    links_list = [req['links'].values() for req in get_requirements()]
    links_list =  [links for sublist in links_list for links in sublist]
    return list(set([links for sublist in links_list for links in sublist]))

# print(get_links())