import unittest
import os
import fastqc
from pathlib import Path


class TestFastQCMethods(unittest.TestCase):
    def setUp(self):
        self.cwd = Path('.')

    def test(self):
        cwd = Path('.')
        test_dir = cwd / 'test_fastq_files'
        self.assertTrue(test_dir.exists() and test_dir.is_dir())

    def test_make_list_of_fastqs(self):
        cwd = Path('.')
        test_dir = cwd.joinpath('test_fastq_files')
        os.chdir(test_dir.resolve())
        
        expected_fastqs = [Path('bad_q_good_l.read1.fq'), Path('bad_q_long_l.read2.fq'), Path('good_q_good_l.read1.fq'), Path('good_q_long_l.read2.fq'),
                           Path('bad_q_good_l.read2.fq'),  Path('bad_q_short_l.read1.fq'),  Path('good_q_good_l.read2.fq'),  Path('good_q_short_l.read1.fq'),
                           Path('bad_q_long_l.read1.fq'),  Path('bad_q_short_l.read2.fq'), Path('good_q_long_l.read1.fq'),  Path('good_q_short_l.read2.fq')]
        testing = fastqc.make_list_of_fastqs()
        expected_fastqs.sort()
        testing.sort()
        
        self.assertEqual(expected_fastqs,testing)

    def test_calculate_average_quality_score(self):
        cwd = Path('.')
        test_dir = cwd.joinpath('test_fastq_files')
        os.chdir(test_dir.resolve())
        table = fastqc.make_list_of_fastqs()
        expected_quals= []

        testing = fastqc.calculate_average_quality_score(table)
        self.assertTrue(True)

    def test_calculate_num_reads(self):
        self.assertTrue(True)

    def test_calculate_len_reads(self):
        self.assertTrue(True)

    def test_create_machine_read_results(self):
        self.assertTrue(True)

    def test_check_quality_cutoffs(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
