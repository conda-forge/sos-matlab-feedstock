import unittest
import sys
import shutil

from sos_notebook.test_utils import sos_kernel
from ipykernel.tests.utils import execute, wait_for_idle, assemble_output

@unittest.skipIf(shutil.which('octave') is None, 'skip test if octave is not available')
class TestSoSKernel(unittest.TestCase):
    def testKernel(self):
        with sos_kernel() as kc:
            execute(kc=kc, code='a = 1')
            stdout, stderr = assemble_output(kc.get_iopub_msg)
            self.assertEqual(stdout.strip(), '', f'Stdout is not empty, "{stdout}" received')
            self.assertEqual(stderr.strip(), '', f'Stderr is not empty, "{stderr}" received')
            execute(kc=kc, code='%use Octave\n%get a')
            stdout, stderr = assemble_output(kc.get_iopub_msg)
            self.assertEqual(stderr.strip(), '', f'Stderr is not empty, "{stderr}" received')
            execute(kc=kc, code='a')
            stdout, stderr = assemble_output(kc.get_iopub_msg)
            self.assertTrue('a = 1' in stdout, f'"{stdout}" received')

if __name__ == '__main__':
    unittest.main()
