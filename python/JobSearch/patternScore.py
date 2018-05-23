
#TODO variable names, class names, and class attribute names are all pretty bad
#Assert types

"""This script is just meant to be used as an importable set of classes"""
import re
from ast import literal_eval
class Scored_Pattern():
    """A pattern with a score attatched to it"""
    def __init__(self, pattern, score=3, flags=0):
        self.score = score
        self.pattern = pattern
        self.re_obj = re.compile(pattern, flags)

class Score_Legend(set):
    """List of Scored_Pattern objects"""
    def __init__(self):
        super(Score_Legend, self).__init__()
    
    def find_patterns_by_score(self, score):
        """Returns a list of all of the Scored_Pattern objects
        that have a score attribute that matches the provided number"""
        return_list = list()
        for i in self:
            if i.score == score:
                return_list.append(i)
        return return_list

    def pattern_exists(self, pattern):
        """Check if there is a pattern in this instance that matches the
        provided string"""
        for i in self:
            if i.pattern == pattern:
                return True
        return False

    def add(self, Scored_Pattern):
        """Works just like add for the 'set' class, but doesn't allow multiple
        of the same pattern"""
        if not self.pattern_exists(Scored_Pattern.pattern):
            super(Score_Legend, self).add(Scored_Pattern)
    
    def create_from_file(self, filepath):
        """Adds every expression in a file, one expression per line"""
        
        with open(filepath) as f:
            file_contents = f.readlines()
        empty_re = re.compile(r'^\s*$')
        for line in file_contents:
            if re.match(empty_re, line):
                continue
            self.add(Scored_Pattern(**literal_eval(line)))
    
class Document():
    """This class just contains some text, a Score_Legend to score it by,
    and and optional title and author"""
    def __init__(self, legend, text, author=None, title=None):
        self.text = text
        self.author = author
        self.title = title
        self.legend = legend
        self.score_total = 0.0
        self._score()

    def _score(self):
        """Scores the provided document based on the number of matches with the
        patterns in the legend's regex"""
        total = 0
        match_total = 0
        for scored_pattern in self.legend:
            matches = re.findall(scored_pattern.re_obj, self.text)
            for match in matches:
                total = total + float(scored_pattern.score)
                match_total = match_total + 1
        if not (total == 0 or match_total == 0):
            self.score_total = total /match_total

    def rescore(self):
        """A public call to _score"""
        self._score()
