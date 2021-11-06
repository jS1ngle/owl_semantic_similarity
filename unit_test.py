import unittest
import semantic_similarity as sesi
from owlready2 import *

onto = get_ontology("file://pizza.owl").load()
pizza = get_namespace("http://www.co-ode.org/ontologies/pizza/pizza.owl#")


class TestLowestCommonAncestor(unittest.TestCase):
    sync_reasoner()

    def test_1(self):
        class1 = owl.Thing
        class2 = owl.Thing
        lca = sesi.get_lowest_common_ancestor(class1, class2)
        self.assertEqual(lca, owl.Thing)

    def test_2(self):
        class1 = pizza.IceCream
        class2 = pizza.Pizza
        lca = sesi.get_lowest_common_ancestor(class1, class2)
        self.assertEqual(lca, pizza.Food)

    def test_3(self):
        class1 = pizza.NutTopping
        class2 = pizza.VegetarianTopping
        lca = sesi.get_lowest_common_ancestor(class1, class2)
        self.assertEqual(lca, pizza.VegetarianTopping)

    def test_4(self):
        class1 = pizza.Spiciness
        class2 = pizza.RealItalianPizza
        lca = sesi.get_lowest_common_ancestor(class1, class2)
        self.assertEqual(lca, owl.Thing)

    def test_5(self):
        class1 = pizza.UnclosedPizza
        class2 = pizza.NamedPizza
        lca = sesi.get_lowest_common_ancestor(class1, class2)
        self.assertEqual(lca, pizza.Pizza)

    def test_6(self):
        class1 = pizza.HerbSpiceTopping
        class2 = pizza.DeepPanBase
        lca = sesi.get_lowest_common_ancestor(class1, class2)
        self.assertEqual(lca, pizza.Food)

    def test_7(self):
        class1 = pizza.PolloAdAstra
        class2 = pizza.Giardiniera
        lca = sesi.get_lowest_common_ancestor(class1, class2)
        self.assertEqual(lca, pizza.NamedPizza)


if __name__ == '__main__':
    unittest.main()