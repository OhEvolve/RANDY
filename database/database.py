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
from sample.buffer import Buffer 

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
            if key == 'buffers':
                return Buffer(
                        value, 
                        *args,
                        contents=[self.load(d['name'],None,d) for d in value['reagents']],
                        **kwargs)
            # TODO: add buffer and element support

    def sync_local(self,names = None,overwrite = False):

        """ Sync local database to cloud database """ 

        if overwrite == True:
            if not self.silent: print 'Overwriting local database...'
            for key in self.db.keys():
                if not self.silent: print 'Deleting {} entries in {}'.format(
                        len(self.db[key]),key)
                self.db[key] = {}
            
        # 
        if isinstance(names,str): 
            names = [names]
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
                
                # makes modifications to dictionary based on which database
                # current: only buffers needs element changes 
                row_dict = _modify_dict(row_dict,name) 
                

                # treatment of rows without row names
                if not 'name' in row_dict: # if missing a name (i.e. blank line)
                    # buffers could have additional lines tho... join with previous entry
                    if name == 'buffers' and row_dict['reagents']:
                        self.db[name][last_row_name]['reagents'] += row_dict['reagents']
                    continue  # skip empty entries otherwise
                    

                try: # first try to access value
                    if self.db[name][row_dict['name']] == row_dict:
                        continue
                    else: # assign updated value
                        self.db[name][row_dict['name']] = row_dict
                        update_count += 1

                except KeyError:
                    self.db[name][row_dict['name']] = row_dict
                    add_count += 1 

                last_row_name = row_dict['name'] # store last name, if its multiline entry 

            # dump resulting file
            pickle.dump(self.db[name],open('./database/{}.p'.format(name),'wb'))
            
            if not self.silent:
                statement = [
                        "Database - {} sync'ed ({} updated, {} added, {} total)".format(
                            name,update_count,add_count,len(self.db[name]))
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

def _list_check(maybe_str):
    """ Turns argument into list/tuple"""
    if not isinstance(type(maybe_str),(list,tuple)):
        return [maybe_str]
    return maybe_str

def _clean_dict(my_dict):
    """ Remove empty entries from dictionary """
    return dict((k, v) for k, v in my_dict.iteritems() if v)

def _delete_keys(my_dict,keys):
    """ Delete keys safely from dictionary """
    for key in keys:
        try:
            del my_dict[key]
        except:
            continue

def _modify_dict(my_dict,name):
    my_dict = _clean_dict(my_dict)
    if name == 'buffers':
        # list of keys
        special_keys = ['volume','mass','concentration']

        # summarize variables here 
        if 'reagents' in my_dict:
            # create dictionary with key values, rename reagents

            my_dict['reagents'] = [dict((('name',my_dict['reagents']),) + 
                tuple((k,v) for k,v in my_dict.items() if k in special_keys))]

        # remove these lingering keys (makes things cleaner)
        _delete_keys(my_dict,special_keys) 

    return my_dict








