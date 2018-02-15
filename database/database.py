# update_local_database.py

""" Syncs local/remote databases """

# standard libraries
import os
import pickle

# nonstandard libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# homegrown libraries
from sample.sample import Sample
from sample.sequence import Sequence
from sample.cell import Cell
from sample.solute import Solute
from sample.solution import Solution

""" Main Method """

class Database(object):

    def __init__(self,key='client_secret.json',fname='RANDY-database',silent=False):

        """ Initialization of google document client """

        # load google sheets file
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name(key,scope)
        client = gspread.authorize(creds)
        self.database_file = client.open(fname)
        
        # transfer parameters
        self.silent = silent

        # load all local databases
        self.local_database_names = ['sequences','cells','solutions','solutes','buffers','elements']
        self.db = {} 

        # load local database
        for name in self.local_database_names:
            self.db[name] = _load_db(name) 

        # heads-up
        if not self.silent: print 'Database loaded!'
        
    
    def load(self,name,dbname=None,*args,**kwargs):
        
        """ Searches for data """
        if dbname == None:
            dbname = self.local_database_names 
        elif isinstance(dbname,str):
            dbname = [dbname]
        else:
            raise TypeError('Passed dbname argument not <str>')

        # for database in dbname
        matches = {}
        for db in dbname:
            try: matches[db] = self.db[db][name] 
            except KeyError: continue

        # depending on the number of matches...
        if len(matches) > 1:
            print '{} matches found, rejecting assignment...'.format(len(matches))
        elif len(matches) == 0:
            print '0 matches found, rejecting assignment...'.format(len(matches))

        # choose correct object depending on object type
        for key,value in matches.items():
            if key == 'sequences':
                return Sequence(value,*args,**kwargs)
            if key == 'cells':
                return Cell(value,*args,**kwargs)
            if key == 'solutions':
                return Solution(value,*args,**kwargs)
            if key == 'solutes':
                return Solute(value,*args,**kwargs)
            # TODO: add buffer and element support

    def sync_local(self,names = None):

        """ Sync local database to cloud database """ 
            
        #
        if isinstance(names,str): 
            self.db[name] = _load_db(names) 
        if names == None:
            names = self.local_database_names

        # pull data 
        for name in names:
            # load worksheet by name
            sheet = self.database_file.worksheet(name)

            # try to pull information, catch if it doesn't exist
            try: all_data = sheet.get_all_records()
            except IndexError: all_data = []
            
            # create counters
            update_count,add_count = 0,0

            # iterate through available lines
            for row_dict in all_data:
                
                try: # first try to access value
                    if self.db[name][row_dict['name']] == row_dict:
                        continue
                    else: # assign updated value
                        self.db[name][row_dict['name']] = row_dict
                        update_count += 1

                except KeyError:
                    self.db[name][row_dict['name']] = row_dict
                    add_count += 1 

            # dump resulting file
            pickle.dump(self.db[name],open('./database/{}.p'.format(name),'wb'))
            
            if not self.silent:
                statement = [
                        "Database - {} sync'ed:".format(name),
                        " > {} entries updated".format(update_count),
                        " > {} entries added".format(add_count),
                        " > {} entries total".format(len(self.db[name]))
                        ]
                print "\n".join(statement)


#------------------------------------------------------------------------------#


""" Internal methods """ 

def _load_db(target):
    """ Load database file from pickle, create new if not present """

    # if a pickled file doesn't exist
    if not os.path.isfile('./database/{}.p'.format(target)):
        db = {}
        pickle.dump(db,open('./database/{}.p'.format(target),'wb'))
    else:
        db = pickle.load(open('./database/{}.p'.format(target),'rb'))

    return db














