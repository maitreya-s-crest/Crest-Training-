from person import Person
from tree_utils import print_tree

# =========================
# CENTER OF THE UNIVERSE
# =========================
markie = Person("Markie", 2003)
aditi = Person("Aditi", 2003)

# =========================
# PARENTS
# =========================
markie_father = Person("Markie's Father", 1975)
markie_mother = Person("Markie's Mother", 1978)

aditi_father = Person("Aditi's Father", 1974)
aditi_mother = Person("Aditi's Mother", 1977)

# =========================
# GRANDPARENTS
# =========================
markie_grandfather = Person("Markie's Grandfather", 1950)
markie_grandmother = Person("Markie's Grandmother", 1952)

aditi_grandfather = Person("Aditi's Grandfather", 1948)
aditi_grandmother = Person("Aditi's Grandmother", 1951)

# =========================
# SIBLINGS
# =========================
aditi_brother = Person("Aditi's Brother", 2000)
brother_wife = Person("Brother's Wife", 2001)

# =========================
# RELATIONSHIPS
# =========================
markie_father.add_child(markie)
markie_mother.add_child(markie)

aditi_father.add_child(aditi)
aditi_mother.add_child(aditi)

aditi_father.add_child(aditi_brother)
aditi_brother.add_child(brother_wife)

markie_grandfather.add_child(markie_father)
markie_grandmother.add_child(markie_father)

aditi_grandfather.add_child(aditi_father)
aditi_grandmother.add_child(aditi_father)

# =========================
# OUTPUT
# =========================
print("\n🌳 MARKIE FAMILY TREE")
print("--------------------")
print_tree(markie_grandfather)

print("\n🌳 ADITI FAMILY TREE")
print("-------------------")
print_tree(aditi_grandfather)
