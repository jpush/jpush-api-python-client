import re

# Value selectors; aliases, tags, etc.

def tag(*tags):
    """Select a single tag."""
    vtag = [t for t in tags]
    return {"tag": vtag}

def tag_and(*tag_ands):
    """Select a single tag_and."""
    vtag_and = [t for t in tag_ands]
    return {"tag_and": vtag_and}

def alias(*alias):
    """Select a single alias."""
    valias = [t for t in alias]
    return {"alias": valias}

def registration_id(*reg_ids):
    """Select a (list of) registration_id(s)."""
    vregistration_id = [t for t in reg_ids]
    return {"registration_id": vregistration_id}
