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

    if not isinstance(template, str) or template is None:
        print(f"Invalid input: template must be a string, but got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or attendees is None:
        print(f"Invalid input: attendees must be a list, but got {type(attendees)}.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for a in attendees:
        if not isinstance(a, dict):
            print(f"Invalid input: each attendee must be a dictionary, but got {type(a).__name__}.")
            return

        for key, value in a.items():
            if value is None or len(value.strip()) == 0:
                a[key] = "N/A"

    for i, attendee in enumerate(attendees, start=1):
        try:
            attendee_name = attendee.get("name") or "N/A"
            attendee_title = attendee.get("event_title") or "N/A"
            attendee_date = attendee.get("event_date") or "N/A"
            attendee_location = attendee.get("event_location") or "N/A"

            personalized_invitation = template\
                .replace("{name}", attendee_name) \
                .replace("{event_title}", attendee_title) \
                .replace("{event_date}", attendee_date) \
                .replace("{event_location}", attendee_location)

            output_filename = f"output_{i}.txt"

            if os.path.exists(output_filename):
                print(f"File {output_filename} already exists.")
                continue

            with open(f"output_{i}.txt", "w", encoding="utf-8") as invitation:
                invitation.write(personalized_invitation)

        except Exception as e:
            print(f"An error occured: {str(e)}")
            return

# Read the template from a file
with open('template.txt', 'r') as file:
    template_content = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Call the function with the template and attendees list
generate_invitations(template_content, attendees)