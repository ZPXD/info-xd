import os
import paramiko
import sys


'''

'''



def search_id():
    pass

def places():
    search_folder = 'search'
    this_search_folder = search_id()

def prepare_search_phrases(what):
    # A. Input - one
    # B. Arg - one
    # C. Arg - list
    # D. Arg - file_path
    search_phrases = what
    return search_phrases

def przebicie_do_srodmiescia(self, search_phrases, other_config=None):
	'''
    https://www.youtube.com/watch?v=PiqK7DN8zXA

	other_config: path to file written in ssh_config style.
	'''
    search_command = 'bash search.sh {} {} {}'
    get_results_command = 'scp {}:{} {}'

    #bash_script = ''''''

	# Open ssh config file and load it's values to config.
	config = SSHConfig()
	if other_config:
		config.parse(open(other_config))
	else:
		config.parse(open(self.ssh_config))

	# For every config hostnames.
	hostnames = config.get_hostnames()
	for host in hostnames:
		try:
            command = search_command.format(host, flaga, searches)
            os.system(command)
            time.sleep(10)
            # response - get here
            while
            try:
                x = check_status()
                if x:
                    command = get_results.format(host, flaga, searches)
                    os.system(command)
                    print('if cool')   
         except:
            re
            os.system(command)
            # ---------------------------------------------
            
   		except:
			print('Could not finish creating the key for host {}.'.format(host))
			print('Read script requirements.')
		continue        
	print('Done. Protect your ssh folder. Protect your private key. Connect by ssh key now.')

def read_results():
    results = []
    for result_file in os.listdir(files):
    
       
if __name__ == "__main__":
    if '-l' in sys.argv:
        what = sys.argv[sys.argv.find('-l')+1]
    elif len(sys.argv) > 1:
        what = ' '.join(sys.argv[1:])
    else:
        what = input('What?')
    search_phrases = prepare_search_phrases(what)
    przebicie_do_srodmiescia(search_phrases, other_config=None)





