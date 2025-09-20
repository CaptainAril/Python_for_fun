#!/bin/python3

"""
Script to fetch and pool Local Government Areas (LGAs) for Nigerian states from an API 
and save to a JSON file."""

import sys

import requests

LGA_API_URL = "https://nga-states-lga.onrender.com/"
STATES = []
LGA_COUNT = 0
STATES_lGA = {}

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m" 

log_success = lambda msg: sys.stdout.write(f"{GREEN}[SUCCESS]{RESET} {msg}\n")
log_error = lambda msg: sys.stdout.write(f"{RED}[ERROR]{RESET} {msg}\n")
log_info = lambda msg: sys.stdout.write(f"{BLUE}[INFO]{RESET} {msg}\n")


def main():
    log_success("Starting pool data fetch...")
    fetch_states()
    for state in STATES:
        fetch_lgas_for_state(state)
    save_to_file()
    log_success(f"Completed fetching LGAs. Total LGAs fetched: {LGA_COUNT} for {len(STATES)} states.")


def fetch_states():
    log_info("Fetching states...")
    global STATES
    try:
        response = requests.get(f'{LGA_API_URL}/fetch')
        response.raise_for_status()
        data = response.json()
        STATES = data
    except requests.RequestException as e:
        log_error(f"Error fetching states: {e}")
        # print(f"Error fetching states: {e}")


def fetch_lgas_for_state(state):
    global STATES_lGA
    try:
        log_info(f"Fetching LGAs for state {state}...")
        response = requests.get(f'{LGA_API_URL}/?state={state}')
        response.raise_for_status()
        data = response.json()
        STATES_lGA[state] = data
        global LGA_COUNT
        LGA_COUNT += len(data)
        log_success(f"Fetched {len(data)} LGAs for state {state}.")
    except requests.RequestException as e:
        log_error(f"Error fetching LGAs for state {state}: {e}")
        # print(f"Error fetching LGAs for state {state}: {e}")


def save_to_file(filename='states_lga.json'):
    import json
    with open(filename, 'w') as f:
        json.dump(STATES_lGA, f)
    log_success(f"Saved states and LGAs to {filename}.")



if __name__ == "__main__":
    main()