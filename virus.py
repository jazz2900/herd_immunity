import pytest

class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

def test_virus_instantiation():
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3


def test_smallpox_virus():
    virus = Virus("smallpox", 0.16, 0.6)
    assert virus.name == "smallpox"
    assert virus.repro_rate == 0.16
    assert virus.mortality_rate == 0.6
