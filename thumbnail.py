#
#

import json
import sys
import os
import subprocess

## Figure out where we are
SCRIPTROOT = os.path.dirname(os.path.realpath(__file__))

## Put in the path to the PhantomJS binary
PHANTOMJS = os.path.join(SCRIPTROOT,'phantomjs')

## Directory where page thumbnails will be stored
MEDIAROOT = os.path.join(SCRIPTROOT, 'page_thumbnail')

## JavaScript to feed to PhantomJS to make thumbnails of pages
THUMBNAILSCRIPT = os.path.join(SCRIPTROOT, 'thumbnail.js')


if len(sys.argv) < 2:
    sys.exit('Usage: %s <file-name>' % sys.argv[0])

if not os.path.exists(sys.argv[1]):
    sys.exit('ERROR: File %s was not found!' % sys.argv[1])

with open(sys.argv[1], 'r') as f:
	record=json.loads(f.read())

dpla_id = record[0]['id']
source_url = record[0]['doc']['source']
outfile = os.path.join(MEDIAROOT, '{}.png'.format(dpla_id))

# print '{} at {} to {}'.format(dpla_id, source_url, outfile)

params = [PHANTOMJS, THUMBNAILSCRIPT, source_url, outfile]

output = subprocess.check_call(params,stderr=subprocess.STDOUT)
# print output
