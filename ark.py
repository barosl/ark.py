#!/usr/bin/env python

import os

execfile('cfg.py')

for ark in arks:
	print '* copying %s ...' % ark['from']

	ret = os.system('rsync -a --delete --copy-unsafe-links %s %s' % (ark['from'], ark['to']))
	sig_no, ex_st = ret & 0xFF, (ret >> 8) & 0xFF

	if sig_no: raise RuntimeError, 'killed: %d' % sig_no
	elif ex_st: raise SystemExit, ex_st
