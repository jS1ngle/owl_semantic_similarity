from owlready2 import *

onto = get_ontology("file://pizza.owl").load()
pizza = get_namespace("http://www.co-ode.org/ontologies/pizza/pizza.owl#")


def get_lowest_common_ancestor(class_a, class_b):
    r"""
    Get lowest common ancestor (common ancestor with greatest depth)
    Parameters
    ----------
    class_a : owl class
    class_b : owl class
    Returns
    -------
    lca : owl class
    Notes
    First, the more simple cases are handled;
    in case they do not apply the Tarjan LCA algorithm is used
    -----
    """
    if class_a == owl.Thing or class_b == owl.Thing:
        return owl.Thing
    elif issubclass(class_b, class_a):
        return class_a
    elif issubclass(class_a, class_b):
        return class_b
    else:
        return tarjan_lca_algorithm(class_a, class_b)


def get_vertex_height(class_a):
    r"""
    Get height of vertex of class_a (depth in taxonomy)
    Parameters
    ----------
    class_a : owl class
    Returns
    -------
    height : int
    Notes
    -----
    """
    ancestors = class_a.ancestors(include_self=False)
    height = len(ancestors)
    return height


def tarjan_lca_algorithm(class_a, class_b):
    r"""
    Get lowest common ancestor
    Parameters
    ----------
    class_a : owl class
    class_b : owl class
    Returns
    -------
    lca : owl class
    Notes
    -----
    Principle behind algorithm described in:
    https://en.wikipedia.org/wiki/Tarjan%27s_off-line_lowest_common_ancestors_algorithm
    The idea behind the recursive algorithm was adapted from
    https://codeforces.com/blog/entry/16221#lca

    """
    if class_a == class_b:  # Trivial case
        return class_a
    if get_vertex_height(class_a) < get_vertex_height(class_b):
        class_a, class_b = class_b, class_a  # Swap classes

    return tarjan_lca_algorithm(get_parent(class_a), class_b)


def get_parent(class_a):
    r"""
    Get parent class
    Parameters
    ----------
    class_a : owl class
    Returns
    -------
    parent : owl class
    Notes
    -----
    """
    parent = class_a.is_a[0]
    return parent


if __name__ == '__main__':
    # Syn reasoner to infer super classes based on defined axioms/restrictions
    sync_reasoner()

    # Example class a and b
    a = pizza.RealItalianPizza
    b = pizza.InterestingPizza

    # determine lca
    lca = get_lowest_common_ancestor(a, b)

    properties_of_a = a.get_class_properties()
