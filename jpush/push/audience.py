import re

DEVICE_TOKEN_FORMAT = re.compile(r'^[0-9a-fA-F]{64}$')
PIN_FORMAT = re.compile(r'^[0-9a-fA-F]{8}$')
UUID_FORMAT = re.compile(
    r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}'
    r'-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')


# Value selectors; device IDs, aliases, tags, etc.

def tag(tag):
    """Select a single tag."""
    return {"tag": tag}

def tag_and(tag_and):
    """Select a single tag_and."""
    return {"tag_and": tag_and}

def alias(alias):
    """Select a single alias."""
    return {"alias": alias}

def registration_id(registration_id):
    """Select a (list of) registration_id(s)."""
    return {"registration_id": registration_id}

def audience(*children):
    """Select audience that match all of the given selectors.

    >>> audience(tag('sports'), tag_and('business'))
    {'audience': {'tag': 'sports'}, {'tag_and': 'business'}}

    """
    return {"audience": {child for child in children}}
