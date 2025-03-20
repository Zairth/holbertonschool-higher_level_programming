#!/usr/bin/python3
"""
create a Python function that generates personalized invitation
files from a template with placeholders and a list of objects
"""


def generate_invitations(template, attendees):
    """
    Generate invitation from a template with attendees attributes
    """

    if not isinstance(template, str):
        raise TypeError(f"Invalid input: template \
            must be a string, but got {type(template).__name__}.")

    if len(template) == 0:
        raise ValueError("Template is empty, no output files generated.")

    if not isinstance(attendees, list):
        raise TypeError(f"Invalid input: attendees must be a list, \
            but got {type(attendees)}.")

    if not attendees:
        raise ValueError("No data provided, no output files generated.")

    for a in attendees:
        if not isinstance(a, dict):
            raise TypeError(f"Invalid input: \
                each attendee must be a dictionary, \
                but got {type(a).__name__}.")

    for i, attendee in enumerate(attendees, start=1):
        personalized_invitation = template.format(
            name=attendee.get('name', 'N/A'),
            event_title=attendee.get('event_title', 'N/A'),
            event_date=attendee.get('event_date', 'N/A'),
            event_location=attendee.get('event_location', 'N/A')
        )

        with open(f"output_{i}.txt", "w") as invitation:
            invitation.write(personalized_invitation)
