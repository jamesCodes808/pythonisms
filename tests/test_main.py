import pytest
from main import LinkedList, Node

def test_ll_exists():
    assert LinkedList

def test_empty_head():
    test = LinkedList()
    assert test.head is None

def test_iteration_works_single():
    test = LinkedList()
    test.add_node(1)
    expected = [1]
    actual = [value for value in test]
    assert expected == actual

def test_iteration_works_multiple():
    test = LinkedList()
    for i in range(1, 5+1):
        test.add_node(i)
    expected = [1,2,3,4,5]
    actual = [value for value in test]
    assert expected == actual