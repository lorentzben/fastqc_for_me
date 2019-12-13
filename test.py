import unittest
import os
import fastqc


class TestFastQCMethods(unittest.TestCase):
    def setUp(self):
        os.chdir('test_fastq_files')

    def test(self):
        self.assertTrue(os.cwd(), 'test_fastq_files')

    def test_make_list_of_fastqs(self):
        expected_fastqs = ['bad_q_good_l.read1.fq', 'bad_q_long_l.read2.fq', 'good_q_good_l.read1.fq', 'good_q_long_l.read2.fq',
                           'bad_q_good_l.read2.fq',  'bad_q_short_l.read1.fq',  'good_q_good_l.read2.fq',  'good_q_short_l.read1.fq',
                           'bad_q_long_l.read1.fq',  'bad_q_short_l.read2.fq', 'good_q_long_l.read1.fq',  'good_q_short_l.read2.fq']
        self.assertTrue(True)

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
