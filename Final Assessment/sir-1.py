"""
Python model 'sir.py'
Translated using PySD
"""

from pathlib import Path
import math

from pysd.py_backend.statefuls import Integ

__pysd_version__ = "2.2.4"

__data = {"scope": None, "time": lambda: 0}

_root = Path(__file__).parent

_subscript_dict = {}

_namespace = {
    "TIME": "time",
    "Time": "time",
    "Initial Susceptible": "initial_susceptible",
    "Total Population": "total_population",
    "Initial Infected": "initial_infected",
    "Susceptible": "susceptible",
    "Contact Rate": "contact_rate",
    "Infected": "infected",
    "Infection": "infection",
    "Infectivity": "infectivity",
    "Period of Infection": "period_of_infection",
    "Recovered": "recovered",
    "Recovery": "recovery",
    "FINAL TIME": "final_time",
    "INITIAL TIME": "initial_time",
    "SAVEPER": "saveper",
    "TIME STEP": "time_step",
}

_dependencies = {
    "initial_susceptible": {"total_population": 1, "initial_infected": 1},
    "total_population": {},
    "initial_infected": {},
    "susceptible": {"_integ_susceptible": 1},
    "contact_rate": {},
    "infected": {"_integ_infected": 1},
    "infection": {
        "susceptible": 1,
        "contact_rate": 1,
        "infected": 1,
        "total_population": 1,
        "infectivity": 1,
    },
    # 1. CHANGES
    "infectivity": {"infected": 1, "recovered": 1},
    # 1. END OF CHANGES
    "period_of_infection": {},
    "recovered": {"_integ_recovered": 1},
    "recovery": {"infected": 1, "period_of_infection": 1},
    "final_time": {},
    "initial_time": {},
    "saveper": {"time_step": 1},
    "time_step": {},
    "_integ_susceptible": {
        "initial": {"initial_susceptible": 1},
        "step": {"infection": 1},
    },
    "_integ_infected": {"initial": {}, "step": {"infection": 1, "recovery": 1}},
    "_integ_recovered": {"initial": {}, "step": {"recovery": 1}},
}

##########################################################################
#                            CONTROL VARIABLES                           #
##########################################################################

_control_vars = {
    "initial_time": lambda: 0,
    # 1. CHANGES
    "final_time": lambda: final_time(),
    # 1. END OF CHANGES
    "time_step": lambda: 0.03125,
    "saveper": lambda: time_step(),
}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


def time():
    return __data["time"]()


def final_time():
    """
    Real Name: FINAL TIME
    Original Eqn: 50
    Units: Day
    Limits: (None, None)
    Type: constant
    Subs: None

    The final time for the simulation.
    """
    return __data["time"].final_time()


def initial_time():
    """
    Real Name: INITIAL TIME
    Original Eqn: 0
    Units: Day
    Limits: (None, None)
    Type: constant
    Subs: None

    The initial time for the simulation.
    """
    return __data["time"].initial_time()


def saveper():
    """
    Real Name: SAVEPER
    Original Eqn: TIME STEP
    Units: Day
    Limits: (0.0, None)
    Type: component
    Subs: None

    The frequency with which output is stored.
    """
    return __data["time"].saveper()


def time_step():
    """
    Real Name: TIME STEP
    Original Eqn: 0.0625
    Units: Day
    Limits: (0.0, None)
    Type: constant
    Subs: None

    The time step for the simulation.
    """
    return __data["time"].time_step()


##########################################################################
#                             MODEL VARIABLES                            #
##########################################################################


def initial_susceptible():
    """
    Real Name: Initial Susceptible
    Original Eqn: Total Population - Initial Infected
    Units: 
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return total_population() - initial_infected()


def total_population():
    """
    Real Name: Total Population
    Original Eqn: 1e+05
    Units: Persons
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1e05


def initial_infected():
    """
    Real Name: Initial Infected
    Original Eqn: 1
    Units: Persons
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1


def susceptible():
    """
    Real Name: Susceptible
    Original Eqn: INTEG ( -Infection, Initial Susceptible)
    Units: Persons
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_susceptible()


def contact_rate():
    """
    Real Name: Contact Rate
    Original Eqn: 5
    Units: Contacts/Person/Day
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 5


def infected():
    """
    Real Name: Infected
    Original Eqn: INTEG ( Infection-Recovery, 1)
    Units: Persons
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_infected()


def infection():
    """
    Real Name: Infection
    Original Eqn: Susceptible * Contact Rate * (Infected / Total Population) * Infectivity
    Units: Persons/Day
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        susceptible()
        * contact_rate()
        * (infected() / total_population())
        * infectivity()
    )


def infectivity():
    """
    Real Name: Infectivity
    Original Eqn: 0.05
    Units: Persons/Contact
    Limits: (None, None)
    Type: component
    Subs: None


    """
    # 1. CHANGES
    return 0.1 * math.exp(-recovered() / (infected() + 1e-7))
    # 1. END OF CHANGES


def period_of_infection():
    """
    Real Name: Period of Infection
    Original Eqn: 15
    Units: Days
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 15


def recovered():
    """
    Real Name: Recovered
    Original Eqn: INTEG ( Recovery, 0)
    Units: Persons
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_recovered()


def recovery():
    """
    Real Name: Recovery
    Original Eqn: Infected/Period of Infection
    Units: Persons/Day
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return infected() / period_of_infection()


_integ_susceptible = Integ(
    lambda: -infection(), lambda: initial_susceptible(), "_integ_susceptible"
)


# 1. CHANGES
_integ_infected = Integ(lambda: infection() - recovery(), lambda: initial_infected(), "_integ_infected")
# 1. END OF CHANGES


_integ_recovered = Integ(lambda: recovery(), lambda: 0, "_integ_recovered")
