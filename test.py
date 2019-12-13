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
        Path.chmod(test_dir)
        print(Path('.'))
        expected_fastqs = ['bad_q_good_l.read1.fq', 'bad_q_long_l.read2.fq', 'good_q_good_l.read1.fq', 'good_q_long_l.read2.fq',
                           'bad_q_good_l.read2.fq',  'bad_q_short_l.read1.fq',  'good_q_good_l.read2.fq',  'good_q_short_l.read1.fq',
                           'bad_q_long_l.read1.fq',  'bad_q_short_l.read2.fq', 'good_q_long_l.read1.fq',  'good_q_short_l.read2.fq']
        testing = fastqc.make_list_of_fastqs()
        
        self.assertEqual(expected_fastqs,testing)

    def test_calculate_average_quality_score(self):
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
