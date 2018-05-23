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
			with open(os.path.join(folder_name, 'captions.txt'), 'w') as f:
				for fname in os.listdir(folder_name):
					if fname.lower().endswith('jpg') or fname.lower().endswith('jepg'):
						f.write("{}:\n".format(fname))
			