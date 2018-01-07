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


def deserialize(s):
    stack = []

    # put first node on the stack
    n = Node(data=s[0])
    n.left = None
    n.right = None
    stack.append(n)

    # process the rest of the string.
    for c in s[1:]:
        # pop stack until we get node with unset right child
        top = stack[-1]
        while top.right:
            stack.pop()
            top = stack[-1]

        if c == '.':
            if not top.left:
                top.left = '.'
            else:
                top.right = '.'
        else:
            n = Node(data=c)
            n.left = None
            n.right = None

            if not top.left:
                top.left = n
            else:
                # top.right should be unset
                top.right = n
            stack.append(n)

    return stack[0]