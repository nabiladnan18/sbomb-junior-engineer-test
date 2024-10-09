import csv
from collections import Counter
from statistics import mean


def read_csv_file(file_path):
    """
    Read a CSV file and return its content as a list of dictionaries.
    """
    with open(file_path) as f:
        csv_data = csv.DictReader(f)
        data = [line for line in csv_data]

    return data


def get_unique_teams(data):
    """
    Return a set of unique team names from the provided data.
    """

    return set(map(lambda event: event["team_name"], data))


def get_most_common_event_type(data):
    """
    Return the most common event type name from the provided data.
    """
    event_type_names = [event["event_type_name"] for event in data]
    event_ranked_by_occurrence: list[tuple] = Counter(event_type_names).most_common()

    return event_ranked_by_occurrence[0][0]


def filter_by_team(data, team_name):
    """
    Filter the data by the provided team name and return the filtered data.
    """

    return [event for event in data if event["team_name"] == team_name]


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

    pass_lengths = [
        float(event["pass_length"])
        for event in filter_by_team(data, team_name)
        if event["event_type_name"] == "Pass"
    ]

    return round(mean(pass_lengths), 1)


def filter_players_by_position(data, position_name):
    """
    Return a list of player names who play at the provided position.
    """

    players = set()
    for event in data:
        if event["player_position_name"] == position_name:
            players.add(event["player_name"])

    return players


def count_successful_passes(data):
    """
    Count the number of successful passes (not considering pass outcome).
    """

    successful_pass_events = [
        event
        for event in data
        if event["event_type_name"] == "Pass" and event["outcome_name"] == ""
    ]

    return len(successful_pass_events)


def filter_by_period(data, period):
    """
    Return a list of events that occurred in the provided period (e.g., 1 or 2).
    """

    return [event for event in data if event["period"] == period]


def count_shots_by_player(data, player_name):
    """
    Count the number of shots taken by the provided player.
    """

    shot_events = set()
    for event in data:
        if event["event_type_name"] == "Shot" and event["player_name"] == player_name:
            timestamp = event["timestamp"]
            shot_events.add(timestamp)

    return len(shot_events)
