"""
State configuration for this IndianaDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "IN"
STATE_NAME = "Indiana"
APP_NAME = "IndianaDischargeWatch"
APP_TAGLINE = "Indiana Discharge Monitoring"
DOMAIN = "indianadischargewatch.org"
DATA_FILE = "in_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@indianadischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "EST"
EPA_REGION = 5
