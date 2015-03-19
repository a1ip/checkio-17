__author__ = 'taras-sereda'

def checkio(teleports_string):
    connections = teleports_string.split(',')
    nodes = set(sum(zip(*connections) , ()))
    start = connections[0][0]
    stack = [(start, [])]

    seen = []
    used_fringe = []
    result = [1]
    while stack:
    # while nodes - set(result) and result[-1]!=start:
        current_node, path = stack.pop()

        # nodes.remove(current_node)

        seen.append(current_node)
        used_fringe.append(path[-2:])
        print used_fringe
        print connections
        fringe = [i for i in connections if i[0] == current_node and i not in used_fringe]
        seen_fringe = [i for i in fringe if i[0] in seen or i[1] in seen]
        newfringe = []
        for i in fringe:
            if i not in seen_fringe:
                newfringe.append(i)
        newfringe+=seen_fringe
        if fringe:
            currently_passed = path[:-1]
            if not currently_passed:
                new_path = fringe[0]
            else:
                new_path = currently_passed + fringe[0]
            connections.remove(fringe[0])
            stack.append((fringe[0][1], new_path))
            result = new_path
        # print fringe
        # print stack
        # print result

    # print result
    return result


if __name__ == "__main__":
   # print checkio("12,23,34,45,56,67,78,81")
   print checkio("12,28,87,71,13,14,34,35,45,46,63,65")
   # print checkio("12,15,16,23,24,28,83,85,86,87,71,74,56")
