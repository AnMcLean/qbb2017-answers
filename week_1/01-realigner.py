#!/usr/bin/env python

"""
Usage ./01-realigner.py <1000_homologues.fa> <alignment_prot.fa>
"""

import sys
import fasta2
import itertools

dna_df = open( sys.argv[1] )
protein_df = open( sys.argv[2] )
realigned = open( "alignment_nuc.fa", "w" )

from itertools import izip

for ( dnaIdent, dnaSeq ),( aminoIdent, aminoSeq ) in izip( fasta2.FASTAReader( dna_df ), fasta.FASTAReader( protein_df ) ):
    realigned.write( dnaIdent + "\n" )
    for amino in aminoSeq:
       if amino == "-":
           realigned.write( "---" )
       else:
           realigned.write( dnaSeq[:3] )
           dnaSeq = dnaSeq[3:]
    realigned.write( "\n" )
    
print realigned