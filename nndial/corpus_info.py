from nndial import persistence

coll_dialogues = persistence.get_collection(persistence.Collection.dialogues)

all_dialogue_act_types = set()


#
#
# Get all unique user dialogue act types
print("UNIQUE USER SA")
c = 0
for user_sa in coll_dialogues.distinct("userSA"):
    print(user_sa)
    all_dialogue_act_types.add(user_sa)
    c += 1
print("Count: {0}".format(c))
print("\n")

#
#
# Get all unique user dialogue act types
print("UNIQUE SYSTEM SA")
c = 0
for sys_sa in coll_dialogues.distinct("sysSA"):
    print(sys_sa)
    all_dialogue_act_types.add(sys_sa)
    c += 1

print("Count: {0}".format(c))
print("\n")

#
#
# Set of DA types which are in system or user turns
print('ALL DA TYPES (USER AND SYSTEM')
print(all_dialogue_act_types)
print('Count: {0}'.format(len(all_dialogue_act_types)))
print('\n')

#
#
# Get all unique values for userFields
print("UNIQUE USER FIELD VALUES")
unique_user_values = set()
for user_fields_values in coll_dialogues.distinct("userFields"):
    values = user_fields_values.strip().split(' ')
    unique_user_values.update(values)

print(unique_user_values)
print("Count: {0}".format(len(unique_user_values)))
print('\n')


#
#
# Get all unique values for userFields
print("UNIQUE SYSTEM REPLY VALUES")
unique_system_values = set()
for system_fields_values in coll_dialogues.distinct("sysRep_field"):
    values = system_fields_values.strip().split(' ')
    unique_system_values.update(values)

print(unique_system_values)
print("Count: {0}".format(len(unique_system_values)))
print('\n')

#
#
# Get all unique values for user and system fields
print("UNIQUE USER FILED and SYSTEM REPLY VALUES")
all_fields = set()
all_fields.update(unique_user_values)  # add all user field values
all_fields.update(unique_system_values)  # add all system field values
print(all_fields)
print('Count: {0}'.format(len(all_fields)))
