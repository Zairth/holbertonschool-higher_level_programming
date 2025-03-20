#!/usr/bin/python3
import os
"""
create a Python function that generates personalized invitation
files from a template with placeholders and a list of objects
"""


def generate_invitations(template, attendees):
    """
    Generate invitation from a template with attendees attributes
    """

    if not isinstance(template, str):
        raise TypeError(f"Invalid input: template must\
        be a string, but got {type(template).__name__}.")

    if len(template) == 0:
        raise ValueError("Template is empty, no output files generated.")

    if not isinstance(attendees, list):
        raise TypeError(f"Invalid input: \
        attendees must be a list, but got {type(attendees)}.")

    if not attendees:
        raise ValueError("No data provided, no output files generated.")
    for a in attendees:
        if not isinstance(a, dict):
            raise TypeError(f"Invalid input: \
            each attendee must be a dictionary, but got {type(a).__name__}.")

    for key, value in a.items():
        if value is None or len(value.strip()) == 0:
            a[key] = "N/A"

    for i, attendee in enumerate(attendees, start=1):
        try:

            personalized_invitation = template\
                .replace("{name}", attendee["name"]) \
                .replace("{event_title}", attendee["event_title"]) \
                .replace("{event_date}", attendee["event_date"]) \
                .replace("{event_location}", attendee["event_location"])

            output_filename = f"output_{i}.txt"

            if os.path.exists(output_filename):
                raise FileExistsError(
                    f"File {output_filename} already exists.")

            with open(f"output_{i}.txt", "w") as invitation:
                invitation.write(personalized_invitation)

        except FileExistsError as e:
            return f"Error: {e}"

        except Exception as e:
            return f"An error occured: {e}"
