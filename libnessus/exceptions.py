class MissingAttribute(Exception):
    """Error when Nessus report items are missing essential properties"""
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, "Report object is missing essential attributes", *args, **kwargs)
