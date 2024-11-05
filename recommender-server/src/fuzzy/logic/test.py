import fuzzy_controller as fc

FS = fc.create_fuzzy()

sets = FS.get_fuzzy_sets('University')

sets.get_term()
FS._detected_type()