import unittest
from model.cursor import Cursor
from infrastructure.position import Position
from infrastructure.cursor_hit_the_edge_exception import CursorHitTheEdgeException


class CursorTests(unittest.TestCase):
    data = [
        'Когда благому просвещенью',
        'Отдвинем более границ',
        'Со временем (по расчисленью'
        'Философических таблиц,',
        'Лет чрез пятьсот) дороги, верно',
        'У нас изменятся безмерно']

    def test_init(self):
        cursor = Cursor(self.data)
        self.assertEqual(cursor.position, Position(0, 0))
        self.assertEqual(str(cursor), '(0, 0)')

    def test_right(self):
        cursor = Cursor(self.data)
        cursor.right()
        self.assertEqual(cursor.position, Position(0, 1))

    def test_right_edge(self):
        cursor = Cursor(self.data)
        cursor.x = 25
        cursor.right()
        self.assertEqual(cursor.position, Position(1, 0))

    def test_left(self):
        cursor = Cursor(self.data)
        cursor.x = 1
        cursor.left()
        self.assertEqual(cursor.position, Position(0, 0))

    def test_left_edge(self):
        cursor = Cursor(self.data)
        cursor.y = 1
        cursor.left()
        self.assertEqual(cursor.position, Position(0, 25))

    def test_up(self):
        cursor = Cursor(self.data)
        cursor.y = 1
        cursor.up()
        self.assertEqual(cursor.position, Position(0, 0))

    def test_up_edge(self):
        cursor = Cursor(self.data)
        self.assertRaises(CursorHitTheEdgeException, cursor.up)

    def test_down(self):
        cursor = Cursor(self.data)
        cursor.down()
        self.assertEqual(cursor.position, Position(1, 0))

    def test_down_edge(self):
        cursor = Cursor(self.data)
        cursor.y = 4
        self.assertRaises(CursorHitTheEdgeException, cursor.down)
