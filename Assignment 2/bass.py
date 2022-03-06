"""
Python model 'bass.py'
Translated using PySD
"""

from pathlib import Path

from pysd.py_backend.statefuls import Integ

__pysd_version__ = "2.2.1"

__data = {"scope": None, "time": lambda: 0}

_root = Path(__file__).parent

_subscript_dict = {}

_namespace = {
    "Time": "time",
    "potential customer concentration": "potential_customer_concentration",
    "new customers": "new_customers",
    "contacts of noncustomers with customers": "contacts_of_noncustomers_with_customers",
    "contacts with customers": "contacts_with_customers",

    "Cont: Our Clients": "customers",
    "Cont: Potential Clients": "potential_customers",
    "Cont: Competitor's Clients": "competitor_customers",

    "Const: Efficiency word of mouth": "efficiency_word_of_mouth",
    "Const: Efficiency of marketing": "efficiency_marketing",
    "Const: Rate": "sociability",

    "Var: Total population": "total_market",
    "Var: Word of Mouth Demand": "word_of_mouth_demand",
    "Var: Marketing Demand": "marketing_demand",

    "P: Satisfied (Customers Cont.)": "p11",
    "P: Disappointed (Customers Cont.)": "p13",
    "P: Satisfied (Competitor's Cont.)": "p21",
    "P: Disappointed (Competitor's Cont.)": "p23",

    "TIME": "time",
    "FINAL TIME": "final_time",
    "INITIAL TIME": "initial_time",
    "SAVEPER": "saveper",
    "TIME STEP": "time_step",
}

_dependencies = {
    "potential_customer_concentration": {"potential_customers": 1, "total_market": 1},
    "new_customers": {"word_of_mouth_demand": 1},
    "contacts_of_noncustomers_with_customers": {
        "contacts_with_customers": 1,
        "potential_customer_concentration": 1,
    },
    "contacts_with_customers": {"customers": 1, "sociability": 1},
    "customers": {"_integ_customers": 1},
    "efficiency_word_of_mouth": {},
    "potential_customers": {"_integ_potential_customers": 1},
    "sociability": {},
    "total_market": {"customers": 1, "potential_customers": 1},
    "word_of_mouth_demand": {
        "contacts_of_noncustomers_with_customers": 1,
        "efficiency_word_of_mouth": 1,
    },
    "final_time": {},
    "initial_time": {},
    "saveper": {"time_step": 1},
    "time_step": {},
    "_integ_customers": {"initial": {}, "step": {"new_customers": 1}},
    "_integ_potential_customers": {"initial": {}, "step": {"new_customers": 1}},
}

##########################################################################
#                            CONTROL VARIABLES                           #
##########################################################################

_control_vars = {
    "initial_time": lambda: 0,
    "final_time": lambda: 100,
    # TODO: scale rate accordingly
    "time_step": lambda: 1,
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
    Original Eqn: 100
    Units: Month
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
    Units: Month
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
    Units: Month
    Limits: (None, None)
    Type: component
    Subs: None

    The frequency with which output is stored.
    """
    return __data["time"].saveper()


def time_step():
    """
    Real Name: TIME STEP
    Original Eqn: 1
    Units: Month
    Limits: (None, None)
    Type: constant
    Subs: None

    The time step for the simulation.
    """
    return __data["time"].time_step()


##########################################################################
#                             MODEL VARIABLES                            #
##########################################################################

def our_customers():
    return Integ(lambda: our_gain(), lambda: 1000, "_integ_customers")


def potential_customers():
    return Integ(lambda: potential_gain(), lambda: 1e05, "_integ_potential_customers")


def competitor_customers():
    return  Integ(lambda: competitor_gain(), lambda: 1000, "_integ_customers")


def our_gain():
    return 


def potential_gain():
    return 


def competitor_gain():
    return 


def pc_cl():
    marketing_demand = efficiency_marketing() * potential_customers()
    satisfied_customers = our_customers() * p11()
    potential_customers_concentration = potential_customers() / total_market()
    contacts_with_customers = satisfied_customers * sociability()
    contacts_of_noncustomers_with_customers = contacts_with_customers * potential_customers_concentration 
    word_of_mouth_demand = efficiency_word_of_mouth() * contacts_of_noncustomers_with_customers
    return marketing_demand + word_of_mouth_demand


def pc_comp():
    marketing_demand = efficiency_marketing() * potential_customers()
    satisfied_customers = competitor_customers() * p21()
    potential_customers_concentration = potential_customers() / total_market()
    contacts_with_customers = satisfied_customers * sociability()
    contacts_of_noncustomers_with_customers = contacts_with_customers * potential_customers_concentration 
    word_of_mouth_demand = efficiency_word_of_mouth() * contacts_of_noncustomers_with_customers
    return marketing_demand + word_of_mouth_demand


def cl_pc():
    return our_customers() * p13() * k()


def comp_pc():
    return competitor_customers() * p23() * k()


def cl_comp():
    return tr() * efficiency_word_of_mouth() * sociability() * competitor_customers() * p21() * our_customers() * (1 - p11() - k() * p13()) / total_market()


def comp_cl():
    return tr() * efficiency_word_of_mouth() * sociability() * our_customers() * p11() * competitor_customers() * (1 - p21() - k() * p23()) / total_market()


def p11():
    return 0.5


def p13():
    return 0.5


def p21():
    return 0.5


def p23():
    return 0.5


def total_market():
    return our_customers() + potential_customers() + competitor_customers()


def efficiency_word_of_mouth():
    return 0.011


def efficiency_marketing():
    return 0.015


def sociability():
    return 100


def k():
    return 2 * efficiency_marketing() / (2 * efficiency_marketing() + 2 * efficiency_word_of_mouth())


def tr():
    return 2 * efficiency_word_of_mouth() / (2 * efficiency_marketing() + 2 * efficiency_word_of_mouth())
