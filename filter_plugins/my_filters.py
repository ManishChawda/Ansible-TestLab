# file: filter_plugins/reverse_filter.py
def reverse_string(value):
    """Reverses a string"""
    return value[::-1]

class FilterModule(object):
    def filters(self):
        return {
            'reverse': reverse_string
        }