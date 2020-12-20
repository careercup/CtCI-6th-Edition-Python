# Solution in chapter_01/p05_one_away.py are not identical.

The set based solution is incorrect because it passes for permutation of input strings, whereas the are_one_edit_different function correctly declares it as False.

Added following test 

        # permuatation with insert shouldn't match
        ("ale","elas",False), 


def are_one_edit_different_sets(a, b): returns True (which is incorrect)
def are_one_edit_different(s1, s2): returns False (which is correct)
