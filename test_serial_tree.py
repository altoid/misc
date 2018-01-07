import unittest
import serial_tree as st

class TestSerialTree(unittest.TestCase):

    def test_1(self):
        a = st.Node(data='A')
        b = st.Node(data='B')
        c = st.Node(data='C')
        d = st.Node(data='D')
        e = st.Node(data='E')
        f = st.Node(data='F')
        g = st.Node(data='G')

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        e.left = g
        c.right = f

        a.preorder()

        print a.serialize()