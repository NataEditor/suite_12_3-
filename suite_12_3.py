import unittest
import runner
import run_and_tournament

runnST = unittest.TestSuite()

runnST.addTest(unittest.TestLoader().loadTestsFromTestCase(runner.RunnerTest))
runnST.addTest(unittest.TestLoader().loadTestsFromTestCase(run_and_tournament.TournamentTest))


testy_runner = unittest.TextTestRunner(verbosity=2)
testy_runner.run(runnST)