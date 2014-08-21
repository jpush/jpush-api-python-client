#!/usr/bin/env python
#-*- coding:utf8 -*-

def add(*types):
    """Select a (list of) to be added objects(s)

    >>> add("registrationid1", "registrationid2")
    {'add': ['registrationid1', 'registrationid2']}
    >>> add("tag1", "tag2")                         
    {'add': ['tag1', 'tag2']}
    >>> add("alias1", "alias2")   
    {'add': ['alias1', 'alias2']}
    """
    vadd = [v for v in types]
    return {"add": vadd}

def remove(*types):
    """Select a (list of) to be removed objects(s)

    >>> remove("registrationid1", "registrationid2")   
    {'remove': ['registrationid1', 'registrationid2']}
    >>> remove("tag1", "tag2")                              
    {'remove': ['tag1', 'tag2']}
    >>> remove("alias1", "alias2")                        
    {'remove': ['alias1', 'alias2']}
    """
    vremove = [v for v in types]
    return {"remove": vremove}

def tag(*types):
    """Get a tag object

    >>> tag("")
    {'tag': ''}
    >>> tag("tag1")
    {'tag': 'tag1'}
    >>> tag(add("tag1", "tag2"), remove("tag3", "tag4"))
    {'tag': {'add': ['tag1', 'tag2'], 'remove': ['tag3', 'tag4']}}
    """
    tag = {}
    if 1 == len(types) and isinstance(types[0], (str, unicode)):
        tag["tag"] = types[0]
        return tag
    tag["tag"] = {}
    for t in types:
        for key in t:
            if key not in ('add', 'remove'):
                raise ValueError("Invalid tag '%s'" % t)
            tag["tag"][key] = t[key]
    return tag

def alias(*types):
    """Get an alias object

    >>> alias("")
    {'alias': ''}
    >>> alias("alias1")
    {'alias': 'alias1'}
    >>> alias(add("alias1", "alias2"), remove("alias3", "alias4"))
    {'alias': {'add': ['alias1', 'alias2'], 'remove': ['alias3', 'alias4']}}
    """
    alias = {}
    if 1 == len(types) and isinstance(types[0], (str, unicode)):
        alias["alias"] = types[0]
        return alias 
    alias["alias"] = {}
    for t in types:
        for key in t:
            if key not in ('add', 'remove'):
                raise ValueError("Invalid alias '%s'" % t)
            alias["alias"][key] = t[key]
    return alias

def registration_id(*types):
    """Get a registration_id object

    >>> registration_id("")
    {'registration_id': ''}
    >>> registration_id("registration_id1")
    {'registration_id': 'registration_id1'}
    >>> registration_id(add("registration_id1", "registration_id2"), remove("registration_id3", "registration_id4"))
    {'registration_id': {'add': ['registration_id1', 'registration_id2'], 'remove': ['registration_id3', 'registration_id4']}}
    """
    registration_id = {}
    if 1 == len(types) and isinstance(types[0], (str, unicode)):
        registration_id["registration_id"] = types[0]
        return registration_id
    registration_id["registration_id"] = {}
    for t in types:
        for key in t:
            if key not in ('add', 'remove'):
                raise ValueError("Invalid registration_id '%s'" % t)
            registration_id["registration_id"][key] = t[key]
    return registration_id

if "__main__" == __name__:
    print add("1", "2")
    print tag(add("a", "b"), remove('1', '2'))
