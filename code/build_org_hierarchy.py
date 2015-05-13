def build_hierarchy(input):
    employee_list = input.split()
    hierarchy_dict = {}
    hierarchy_info_dict = {}
    employee_chunk_list = []
    new_chunk = []
    for idx, employee in enumerate(employee_list):
        if idx % 3 == 0:
            if new_chunk:
                employee_chunk_list.append(new_chunk)
            new_chunk = []
        new_chunk.append(employee)

    EMPLOYEE_INDEX = 0
    BOSS_INDEX = 1
    INFO_INDEX = 2
    CEO = None
    for chunk in employee_chunk_list:
        if chunk[BOSS_INDEX] not in hierarchy_dict:
            hierarchy_dict[chunk[BOSS_INDEX]] = []
        if chunk[BOSS_INDEX] == chunk[EMPLOYEE_INDEX]:
            CEO = chunk[BOSS_INDEX]
        else:
            hierarchy_dict[chunk[BOSS_INDEX]].append(chunk[EMPLOYEE_INDEX])
        hierarchy_info_dict[chunk[EMPLOYEE_INDEX]] = chunk[INFO_INDEX]
    print_hierarchy(hierarchy_dict, hierarchy_info_dict, CEO, 0)


def print_hierarchy(hierarchy_dict, hierarchy_info_dict, employee, depth):
    dummy_spaces = '   ' * depth
    if employee not in hierarchy_dict:
        # This emplyee is the leaf node(not boss of anyone)
        print '%s %s %s' % (dummy_spaces, employee, hierarchy_info_dict[employee])
    else:
        # print yourself and then do recursive on your sub-ordinates
        print '%s %s %s' % (dummy_spaces, employee, hierarchy_info_dict[employee])
        for sub_ordinate in hierarchy_dict[employee]:
            print_hierarchy(hierarchy_dict, hierarchy_info_dict, sub_ordinate, depth + 1)

if __name__=='__main__':
   '''
   The aim of this program is to build the hierarchy of the organization
   The data provided is a big input string which is in this format 'employee boss employee_info....'
   Sample Output for the input below
   Mark CEO
     Aditya VP
       Ruchi SE
       Smith SE
     Boz VP
     Larry VP
   '''
   input_string = 'Aditya Mark VP Ruchi Aditya SE Mark Mark CEO Smith Aditya SE Boz Mark VP Larry Mark VP Page Larry SE'
   build_hierarchy(input_string)
