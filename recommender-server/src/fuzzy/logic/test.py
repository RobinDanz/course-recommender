import fuzzy_controller as fc
import simpful as sf

FS = fc.create_fuzzy()

sets = FS.get_fuzzy_sets('University')

print(sets[0].get_term())
#FS._detected_type()
#FS.set_variable()

print(FS._lvs.values())
# Take the linguistic variables out of the system
for key, value in FS._lvs.items():
    # Take just one lvs 
    if key == 'University':
        print(key, value)
        # obtain the membership values to each term of the lvs for one value
        lvs = value.get_values(1)
        print(lvs)
        # Take only the maximum value and store the term associated with it
        term = max(lvs, key = lambda i: lvs[i])
        print(term)
