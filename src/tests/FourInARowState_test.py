from unittest import TestCase, main
from .. import FourInARowState

class Test_FourInARowState(TestCase):
  def test_is_column_full(self):
    state = FourInARowState(width=2, height=2)
    self.assertEqual(False, state.is_column_full(0))

if __name__ == '__main__':
  main()
