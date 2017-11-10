#!/usr/bin/env python

"""
Usage:
./CTCF_interactions.py <ctcf_peaks.tsv> <Nora_Primers.bed>
"""
import sys
import numpy as np

def hifive_data():
    data = np.load('Out.heat.npz')
    return data[ '0.forward' ], data[ '0.reverse' ], data[ '0.enrichment' ]

def ctcf_binding():
    ctcf_sites = []
    for line in open(sys.argv[1]):
        line = line.rstrip('\r\n').split('\t')
        if line[0] == 'chrX':
            ctcf_sites.append(line[1])
    return ctcf_sites

def get_primer_dictionary():
    primer_dic = {}
    for line in open(sys.argv[2]):
        line = line.rstrip('\r\n').split('\t')
        if line[0] == '#chr':
            pass
        else:
            primer_dic[line[1] + '_' + line[2]] = line[3]
    return primer_dic

def CTCF_indices(primers, sites):
    indices = []
    for i, each in enumerate(primers):
        start, stop = int(each[0]), int(each[1])
        for site in sites:
            if int(site) >= start and int(site) <= stop:
                indices.append(i)
                break
    return indices

def interaction_pairs(forward, reverse, enrich):
    indices_forward, indices_reverse = [], []
    for j in forward:
        top_reverse, top = None, 0.
        for k in reverse:
            if float(enrich[j][k]) > top:
                top_reverse = k
                top = float(enrich[j][k])
        indices_forward.append((j,top_reverse))
    for k in reverse:
        top_for, top = None, 0.
        for j in forward:
            if float(enrich[j][k]) > top:
                top_forward = j
                top = float(enrich[j][k])
        indices_reverse.append((top_forward,k))
    return indices_forward, indices_reverse

def prints(i, j, pairs, dictionary, direction):
    for ixn in pairs:
        fw_key = str(i[ixn[0]][0]) + '_' + str(i[ixn[0]][1])
        rv_key = str(j[ixn[1]][0]) + '_' + str(j[ixn[1]][1])
        if direction == 'fwd':
            print '%s\t%s' % (dictionary[fw_key], dictionary[rv_key])
        else:
            print '%s\t%s' % (dictionary[rv_key], dictionary[fw_key])

def main(): 
    ctcf_sites = ctcf_binding()
    fwd, rev, enrich = hifive_data()
    dictionary = get_primer_dictionary()
    forward, reverse = CTCF_indices( fwd, ctcf_sites ), CTCF_indices( rev, ctcf_sites )
    indices_forward, indices_reverse = interaction_pairs(forward, reverse, enrich)
    print 'Top interactions with forward primers:'
    prints(fwd, rev, indices_forward, dictionary, 'forward' )
    print '\nTop interactions with reverse primers:'
    prints(fwd, rev, indices_reverse, dictionary, 'reverse' )

main() 