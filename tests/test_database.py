import pytest

from database import Database


class TestDatabase:
    @pytest.mark.parametrize("bun_name", ["black bun", "white bun", "red bun"])
    def test_available_buns(self, bun_name):
        database = Database()
        available_buns = [bun.get_name() for bun in database.available_buns()]
        assert bun_name in available_buns

    @pytest.mark.parametrize("ingredient_name", ['hot sauce', 'sour cream', 'chili sauce', 'cutlet', 'dinosaur', 'sausage'])
    def test_available_ingredients(self, ingredient_name):
        database = Database()
        available_ingredients = [ingredient.get_name() for ingredient in database.available_ingredients()]
        assert ingredient_name in available_ingredients
       