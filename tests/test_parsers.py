# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

         
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    seq_record=FastaParser('/data/test.fa')
    first_record=list(seq_record)[0]
    assert (first_record[0]=='seq0') and (first_record[1]=='TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA')


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    seq_record=FastqParser('/data/test.fq')
    first_record=list(seq_record)[0]
    assert (first_record[0]=='seq0') and (first_record[1]=='TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG')



def test_FastaParser_2():
    seq_record=FastaParser('/data/test.fa')
    num_seqs=len(list(seq_record))
    assert num_seqs == 100


def test_FastqParser_2():
    seq_record=FastqParser('/data/test.fq')
    num_seqs=len(list(seq_record))
    assert num_seqs == 100

