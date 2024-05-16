import pytest

from Lösungen.circle import Circle

class TestCircle:
    def test_collides_with(self):
        circle1 = Circle((0, 0), 10, (255, 0, 0))
        circle2 = Circle((10, 10), 10, (0, 0, 255))
        assert circle1.collides_with(circle2) == True

        circle1 = Circle((0, 0), 5, (255, 0, 0))
        circle2 = Circle((10, 10), 5, (0, 0, 255))
        assert circle1.collides_with(circle2) == False
    
    def test_collides_with_other_circles(self):
        circle1 = Circle((0, 0), 10, (255, 0, 0))
        circle2 = Circle((10, 10), 10, (0, 0, 255))
        circle3 = Circle((20, 20), 4, (0, 255, 0))
        assert circle1.collides_with_other_circles() == True
        assert circle2.collides_with_other_circles() == True
        assert circle3.collides_with_other_circles() == False
    
    def test_move(self):
        circle1 = Circle((0, 0), 10, (255, 0, 0))
        circle2 = Circle((10, 10), 10, (0, 0, 255))
        circle3 = Circle((20, 20), 4, (0, 255, 0))
        
        circle1.move((5, 5))
        assert circle1.pos == (0, 0)
        
        circle2.move((-5, -5))
        assert circle2.pos == (10, 10)
        
        circle3.move((5, 5))
        assert circle3.pos == (25, 25)

if __name__ == '__main__':
    pytest.main()
