import sys
import os

if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise ValueError('Usage is python scriptname folder_name')
	else:
		folder_name = sys.argv[1]
		if not os.path.exists(folder_name):
			raise ValueError('The folder {} could not be found in this directory.'.format(folder_name))
		else:
			path_to_captions = os.path.join(folder_name, 'captions.txt')
			if os.path.exists(path_to_captions):
				# read existing keys
				lines = open(path_to_captions).readlines()
				existing_captions = dict((l[:l.find(':')], l[l.find(':')+1:]) for l in lines)
				# write new file
				with open(path_to_captions, 'w') as f:
					for fname in os.listdir(folder_name):
						if fname.lower().endswith('jpg') or fname.lower().endswith('jpeg'):
							if fname in existing_captions:
								f.write("{}:{}".format(fname, existing_captions[fname]))
							else:
								f.write("{}:\n".format(fname))
			else:
				with open(path_to_captions, 'w') as f:
					for fname in os.listdir(folder_name):
						if fname.lower().endswith('jpg') or fname.lower().endswith('jpeg'):
							f.write("{}:\n".format(fname))
				