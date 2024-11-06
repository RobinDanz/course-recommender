import fuzzy_controller as fc
import simpful as sf

FS = fc.create_fuzzy()

sets = FS.get_fuzzy_sets('University')

print(sets[0].get_term())
#FS._detected_type()
#FS.set_variable()

print(FS._lvs.values())
for key, value in FS._lvs.items():
    if key == 'University':
        print(key, value)
        x = value.get_values(1)
        print(x)
        print(max(x, key = lambda i: x[i]))
