class Jump:
    """
    This just represents a 'jump' from one hole over another hole
    to a 'destination' hole.  We implement simple __eq__ and __hash__ so we
    can use jumps in sets and stuff.
    """

    def __init__(self, start, jump, end):
        self.origin = start
        self.over = jump
        self.dest = end

    def __eq__(self, other):
        return self.origin == other.origin and self.over == other.over and self.dest == other.dest

    def __hash__(self):
        return hash((self.origin, self.dest, self.over))

    def __str__(self):
        """ Called by print() """
        return "Jump from {} to {} over {}".format(self.origin, self.dest, self.over)

    def __repr__(self):
        """ Called when printing a collection containing jump objects """
        return "Jump({}, {}, {})".format(self.origin, self.over, self.dest)

