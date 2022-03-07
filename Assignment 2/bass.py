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
    "TIME": "time",
    "FINAL TIME": "final_time",
    "INITIAL TIME": "initial_time",
    "SAVEPER": "saveper",
    "TIME STEP": "time_step",
    "Time": "time",

    "Our Customers": "our_customers",
    "Potential Customers": "potential_customers",
    "Competitor Customers": "competitor_customers",

    "New Customers": "our_gain",
    "New Potential Customers": "potential_gain",
    "New Competitor Customers": "competitor_gain",

    "Potential Customers -> Our Customers": "potential2our",
    "Potential Customers -> Competitor Customers": "potential2competitor",
    "Our Customers -> Potential Customers": "our2potential",
    "Competitor Customers -> Potential Customers": "competitor2potential",
    "Our Customers -> Competitor Customers": "our2competitor",
    "Competitor Customers -> Our Customers": "competitor2our",
    "Demand from Marketing": "marketing_demand",
    "Concentration of Potential Customers": "potential_customers_concentration",
    "Total population (actual)": "total_market",

    "P11": "p11",
    "P13": "p13",
    "P21": "p21",
    "P23": "p23",
    "Word of Mouth impact": "efficiency_word_of_mouth",
    "Marketing impact": "efficiency_marketing",
    "Rate": "sociability",
    "Share of Dissatisfied": "k",
    "Luring Threshold": "tr"
}

_dependencies = {
    "final_time": {},
    "initial_time": {},
    "saveper": {"time_step": 1},
    "time_step": {},

    "our_customers": {"_integ_our_customers": 1},
    "potential_customers": {"_integ_potential_customers": 1},
    "competitor_customers": {"_integ_competitor_customers": 1},

    "_integ_our_customers": {"initial": {}, "step": {"our_gain": 1}},
    "_integ_potential_customers": {"initial": {}, "step": {"potential_gain": 1}},
    "_integ_competitor_customers": {"initial": {}, "step": {"competitor_gain": 1}},

    "our_gain": {
        "potential2our": 1,
        "competitor2our": 1,
        "our2potential": 1,
        "our2competitor": 1
    },
    "potential_gain": {
        "our2potential": 1,
        "competitor2potential": 1,
        "potential2our": 1,
        "potential2competitor": 1
    },
    "competitor_gain": {
        "potential2competitor": 1,
        "our2competitor": 1,
        "competitor2potential": 1,
        "competitor2our": 1
    },

    "potential2our": {
        "our_customers": 1,
        "p11": 1,
        "sociability": 1,
        "potential_customers_concentration": 1,
        "efficiency_word_of_mouth": 1,
        "marketing_demand": 1
    },
    "potential2competitor": {
        "competitor_customers": 1,
        "p21": 1,
        "sociability": 1,
        "potential_customers_concentration": 1,
        "efficiency_word_of_mouth": 1,
        "marketing_demand": 1

    },
    "our2potential": {
        "our_customers": 1,
        "p13": 1,
        "k": 1
    },
    "competitor2potential": {
        "competitor_customers": 1,
        "p23": 1,
        "k": 1
    },
    "our2competitor": {
        "tr": 1,
        "efficiency_word_of_mouth": 1,
        "sociability": 1,
        "competitor_customers": 1,
        "p21": 1,
        "our_customers": 1,
        "p11": 1,
        "k": 1,
        "p13": 1,
        "total_market": 1
    },
    "competitor2our": {
        "tr": 1,
        "efficiency_word_of_mouth": 1,
        "sociability": 1,
        "our_customers": 1,
        "p11": 1,
        "competitor_customers": 1,
        "p21": 1,
        "k": 1,
        "p23": 1,
        "total_market": 1
    },
    "marketing_demand": {
        "efficiency_marketing": 1,
        "potential_customers": 1
    },
    "potential_customers_concentration": {
        "potential_customers": 1,
        "total_market": 1
    },
    "total_market": {
        "our_customers": 1,
        "potential_customers": 1,
        "competitor_customers": 1
    },

    "p11": {},
    "p13": {},
    "p21": {},
    "p23": {},
    "efficiency_word_of_mouth": {},
    "efficiency_marketing": {},
    "sociability": {},
    "k": {
        "efficiency_marketing": 1,
        "efficiency_word_of_mouth": 1
    },
    "tr": {
        "efficiency_word_of_mouth": 1,
        "efficiency_marketing": 1
    },
}

##########################################################################
#                            CONTROL VARIABLES                           #
##########################################################################

_control_vars = {
    "initial_time": lambda: 0,
    "final_time": lambda: final_time(),
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
    """
    Real Name: Our Customers
    Original Eqn: INTEG(-our gain, 0)
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_our_customers()


def potential_customers():
    """
    Real Name: Potential Customers
    Original Eqn: INTEG(-potential gain, 10e05)
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_potential_customers()


def competitor_customers():
    """
    Real Name: Competitor Customers
    Original Eqn: INTEG(-competitor gain, 0)
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_competitor_customers()


_integ_our_customers = Integ(lambda: our_gain(), lambda: 0, "_integ_customers")


_integ_potential_customers = Integ(lambda: potential_gain(), lambda: 1e05, "_integ_potential_customers")


_integ_competitor_customers = Integ(lambda: competitor_gain(), lambda: 0, "_integ_customers")


def our_gain():
    """
    Real Name: New Customers
    Original Eqn: potential2our + competitor2our + our2potential + our2competitor 
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return potential2our() + competitor2our() - our2potential() - our2competitor() 


def potential_gain():
    """
    Real Name: New Potential Customers
    Original Eqn: our2potential + competitor2potential + potential2our + potential2competitor 
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return our2potential() + competitor2potential() - potential2our() - potential2competitor()


def competitor_gain():
    """
    Real Name: New Competitor Customers
    Original Eqn: potential2competitor + our2competitor + competitor2potential + competitor2our 
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return potential2competitor() + our2competitor() - competitor2potential() - competitor2our()


def potential2our():
    """
    Real Name: Potential Customers -> Our Customers
    Original Eqn: marketing_demand + (efficiency_wom * rate * potential_customers * our_customers * p11) / total_market
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    satisfied_customers = our_customers() * p11()
    contacts_with_customers = satisfied_customers * sociability()
    contacts_of_noncustomers_with_customers = contacts_with_customers * potential_customers_concentration()
    word_of_mouth_demand = efficiency_word_of_mouth() * contacts_of_noncustomers_with_customers
    return marketing_demand() + word_of_mouth_demand


def potential2competitor():
    """
    Real Name: Potential Customers -> Competitor Customers
    Original Eqn: marketing_demand + (efficiency_wom * rate * potential_customers * competitor_customers * p21) / total_market
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    satisfied_customers = competitor_customers() * p21()
    contacts_with_customers = satisfied_customers * sociability()
    contacts_of_noncustomers_with_customers = contacts_with_customers * potential_customers_concentration()
    word_of_mouth_demand = efficiency_word_of_mouth() * contacts_of_noncustomers_with_customers
    return marketing_demand() + word_of_mouth_demand


def our2potential():
    """
    Real Name: Our Customers -> Potential Customers
    Original Eqn: our_customers * p13 * share_dissatisfied
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return our_customers() * p13() * k()


def competitor2potential():
    """
    Real Name: Competitor Customers -> Potential Customers
    Original Eqn: competitor_customers * p23 * share_dissatisfied
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return competitor_customers() * p23() * k()


def our2competitor():
    """
    Real Name: Our Customers -> Competitor Customers
    Original Eqn: luring_threshold * efficiency_word_of_mouth * rate * competitor_customers * p21 * our_customers * (1 - p11 - share_dissatisfied * p13) / total_market
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return tr() * efficiency_word_of_mouth() * sociability() * competitor_customers() * p21() * our_customers() * (1 - p11() - k() * p13()) / total_market()


def competitor2our():
    """
    Real Name: Competitor Customers -> Our Customers
    Original Eqn: luring_threshold * efficiency_word_of_mouth * rate * competitor_customers * p11 * our_customers * (1 - p21 - share_dissatisfied * p23) / total_market
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return tr() * efficiency_word_of_mouth() * sociability() * our_customers() * p11() * competitor_customers() * (1 - p21() - k() * p23()) / total_market()


def marketing_demand():
    """
    Real Name: Demand from Marketing
    Original Eqn: Efficiency Marketing / Potential Customers
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return efficiency_marketing() * potential_customers()


def potential_customers_concentration():
    """
    Real Name: Concentration of Potential Customers
    Original Eqn: Potential Customers / Total Market
    Units: float
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return potential_customers() / total_market()


def total_market():
    """
    Real Name: Total population (actual)
    Original Eqn: Our Customers + Potential Customers + Competitor Customers
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return our_customers() + potential_customers() + competitor_customers()


def p11():
    """
    Real Name: P11
    Original Eqn: 0.5
    Units: float
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.5


def p13():
    """
    Real Name: P13
    Original Eqn: 0.5
    Units: float
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.5


def p21():
    """
    Real Name: P21
    Original Eqn: 0.5
    Units: float
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.5


def p23():
    """
    Real Name: P23
    Original Eqn: 0.5
    Units: float
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.5


def efficiency_word_of_mouth():
    """
    Real Name: Word of Mouth impact
    Original Eqn: 0.011
    Units: person / contact
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.015


def efficiency_marketing():
    """
    Real Name: Marketing impact
    Original Eqn: 0.015
    Units: person / contact
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.011


def final_time():
    """
    Real Name: FINAL TIME
    Original Eqn: 100
    Units: int
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 100


def sociability():
    """
    Real Name: Rate
    Original Eqn: 100
    Units: contact / person / Month
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 100


def k():
    """
    Real Name: Share of Dissatisfied
    Original Eqn: Market_impact / (WoM_impact + Market_impact)
    Units: float
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return efficiency_marketing() / (efficiency_marketing() + efficiency_word_of_mouth())


def tr():
    """
    Real Name: Share of Dissatisfied
    Original Eqn: WoM_impact / (WoM_impact + Market_impact)
    Units: float
    Limits: (None, None)
    Type: constant
    Subs: None
    """
    return efficiency_word_of_mouth() / (efficiency_marketing() + efficiency_word_of_mouth())
