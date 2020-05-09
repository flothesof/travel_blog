import glob
import os.path as op
import subprocess

files = glob.glob('content/*.md')
splitter = lambda fname: op.splitext(op.split(fname)[1])[0].split('_')[0]
files = sorted(files, key=splitter)

slugs = []
for f in files:
	lines = open(f).readlines()
	for line in lines:
		if line.startswith('Slug:'):
			slugs.append(line.split('Slug:')[1].strip())
			break

article_names = [slug + '.html' for slug in slugs]

article_paths = [op.join('output', article_name) for article_name in article_names]


OUTPUT_PATH = 'output-tex'
if not op.exists(OUTPUT_PATH):
	os.makedirs(OUTPUT_PATH)

output_paths = [op.join(OUTPUT_PATH, slug + '.tex') for slug in slugs]

for article_path, output_path in zip(article_paths, output_paths):
	subprocess.call(f"pandoc {article_path} -o {output_path}",
		shell=True)

print("\n".join(["\\include{" + slug + "}" for slug in slugs]))