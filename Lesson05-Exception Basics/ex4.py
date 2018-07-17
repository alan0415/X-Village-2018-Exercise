'''
TODO: define a exception class
'''
class RelationException(Exception):
    def __init__(self, err_msg1,err_msg2):
        self.msg1 = err_msg1
        self.msg2 = err_msg2
    def __str__(self):
        return "Are you sure that "+ self.msg1 + " and " + self.msg2 +" are in love with each other?"
relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}
def check(pa, pb):
    try:
        if relation[pa] != pb:
            raise RelationException(relation[pa], pb)
    except KeyError:
        print("Relation not found")
        raise RelationException(pa, pb)
try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1, p2)
    print("{} and {} are in love with each other!".format(p1, p2))
    
except RelationException as e:
    print(e)