import csv
import json
from collections import Counter


def read_csv_file(file_path):
    """
    Read a CSV file and return its content as a list of dictionaries.
    """
    with open(file_path) as f:
        csv_data = csv.DictReader(f)
        data = [line for line in csv_data]

    return json.dumps(data)


def get_unique_teams(data):
    """
    Return a set of unique team names from the provided data.
    """

    return set(map(lambda y: y["team_name"], json.loads(data)))


def get_most_common_event_type(data):
    """
    Return the most common event type name from the provided data.
    """
    event_type_names = [event["event_type_name"] for event in json.loads(data)]
    event_ranked_by_occurrence: list[tuple] = Counter(event_type_names).most_common()

    return event_ranked_by_occurrence[0][0]


def filter_by_team(data, team_name):
    """
    Filter the data by the provided team name and return the filtered data.
    """

    return [event for event in json.loads(data) if event["team_name"] == team_name]


def count_event_type_by_team(data, team_name, event_type_name):
    """
    Count the number of events of a specific type for a given team.
    """

    filtered_by_team = filter_by_team(data, team_name)
    event_type_names = [event["event_type_name"] for event in filtered_by_team]

    return event_type_names.count(event_type_name)


def average_pass_length_by_team(data, team_name):
    """
    Calculate the average pass length for the provided team to 1 decimal place
    """
    return

def filter_players_by_position(data, position_name):
    """
    Return a list of player names who play at the provided position.
    """
    return

def count_successful_passes(data):
    """
    Count the number of successful passes (not considering pass outcome).
    """
    return

def filter_by_period(data, period):
    """
    Return a list of events that occurred in the provided period (e.g., 1 or 2).
    """
    return

def count_shots_by_player(data, player_name):
    """
    Count the number of shots taken by the provided player.
    """
    return
