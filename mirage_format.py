#! /usr/bin/env python
#
"""
This code takes the ouput file from niriss_magnitude_converter.py and writes
out mirage-style star list files.
"""
from __future__ import print_function
import numpy
import sys
filename = sys.argv[-2]
name_fragment = sys.argv[-1]
f1 = open(filename,'r')
line = f1.readline()
f1.close()
line = line.strip('\n')
line = line.strip('#')
values = line.split('|')
inds = []
filter_names = []
raind = -10
decind = -10
for loop in range(len(values)):
    if 'RA' in values[loop]:
        raind = loop
    if 'Dec' in values[loop]:
        decind = loop
    if 'NIRISS' in values[loop]:
        filter = values[loop].strip(' ')
        filter = filter.replace('NIRISS','')
        filter=filter.strip(' ')
        inds.append(loop)
        filter_names.append(filter)
if (raind < 0) | (decind < 0) | len(inds) < 1:
    print('Error parsing the header line in file %s.  Exiting' % (filename))
    sys.exit()
values = numpy.loadtxt(filename,comments='#')
s1=values.shape
if len(inds) == 12:
    outname = 'stars_' + name_fragment + '_allfilters.txt'
    outfile = open(outname,'w')
    print('# \n# vegamag\n# \n# \n   index x_or_RA y_or_Dec niriss_f090w_magnitude niriss_f115w_magnitude niriss_f140m_magnitude niriss_f150w_magnitude niriss_f158m_magnitude niriss_f200w_magnitude niriss_f277w_magnitude niriss_f356w_magnitude niriss_f380m_magnitude niriss_f430m_magnitude niriss_f444w_magnitude niriss_f480m_magnitude',file=outfile)
    for ind1 in range(s1[0]):
        print('%8d %13.8f %13.8f %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f' % (ind1+1,values[ind1,raind],values[ind1,decind],values[ind1,2],values[ind1,3],values[ind1,4],values[ind1,5],values[ind1,6],values[ind1,7],values[ind1,8],values[ind1,9],values[ind1,10],values[ind1,11],values[ind1,12],values[ind1,13]),file=outfile)
    outfile.close()
else:
    for loop in range(len(inds)):
        outname = 'stars_' + name_fragment + '_' + filter_names[loop] + '.txt'
        outfile = open(outname,'w')
        print('# \n# vegamag\n# \n# \nx_or_RA y_or_Dec magnitude',file=outfile)
        for ind1 in range(s1[0]):
            print('%13.8f %13.8f %9.5f' % (values[ind1,raind],values[ind1,decind],values[ind1,inds[loop]]),file=outfile)
        outfile.close()
