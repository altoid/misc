# serializing a binary tree.

class Node(object):
    def __init__(self, **kwargs):
        self.data = kwargs.get('data')
        self.left = kwargs.get('left', '.')
        self.right = kwargs.get('right', '.')

    def preorder(self, level = 0):
        print "%s%s" % ('    ' * level, self.data)
        if self.left:
            if self.left == '.':
                print "%s." % ('    ' * (level + 1))
            else:
                self.left.preorder(level + 1)
        if self.right:
            if self.right == '.':
                print "%s." % ('    ' * (level + 1))
            else:
                self.right.preorder(level + 1)

    def serialize(self):
        # do a preorder walk
        result = str(self.data)
        if self.left:
            if self.left == '.':
                result += '.'
            else:
                result += self.left.serialize()
        else:
            result += '.'

        if self.right:
            if self.right == '.':
                result += '.'
            else:
                result += self.right.serialize()
        else:
            result += '.'

        return result

