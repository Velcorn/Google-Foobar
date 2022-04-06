def solution(h, q):
    """
    Slightly adapted solution from https://livecodestream.dev/challenge/ion-flux-relabeling/
    :param h: height of binary tree
    :param q: list of integers for flux converters
    :return:
    """
    # Initialize label array
    labels = []
    # Max number of nodes in tree of height h
    max_nodes = 2 ** h - 1
    # For each converter in q, traverse the tree to find its label
    for c in q:
        prev_node = -1
        curr_node = subtree = max_nodes
        # While current node is not the root, go to next level, get left and right node,
        # c label is prev_node if c is left or right node,
        # otherwise if c less than left, curr_node is left, else right; update prev_node
        while subtree > 1:
            subtree //= 2
            left = curr_node - subtree - 1
            right = curr_node - 1
            if c == left or c == right:
                labels.append(prev_node)
            if c < left:
                curr_node = left
            else:
                curr_node = right
            prev_node = curr_node
    return labels


if __name__ == '__main__':
    print(solution(3, [7, 3, 5, 1]))
    print(solution(5, [19, 14, 28]))
