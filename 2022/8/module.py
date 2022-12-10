from dataclasses import dataclass

def __find_visible_threes__(trees):
    visible_tree_indices = set()

    total_trees = len(trees)
    for i in range(0, total_trees):
        if (i in visible_tree_indices):
            continue
        elif (i == 0):
            visible_tree_indices.add(i)
            visible_tree_indices.add(len(trees) - 1)
        elif(all(tree < trees[i] for tree in trees[0:i])):
            visible_tree_indices.add(i)
        elif(all(tree < trees[i] for tree in trees[i+1:])):
            visible_tree_indices.add(i)

    return list(visible_tree_indices)

@dataclass
class Row:
    trees: list

    def visible_trees(self):
        return __find_visible_threes__(self.trees)

@dataclass
class Column:
    trees: list

    def visible_trees(self):
        return __find_visible_threes__(self.trees)

@dataclass
class Grid:
    rows: list
    columns: list

    def number_of_visible_trees(self):
        visible_trees = set()

        for i, row in enumerate(self.rows):
            for visible_tree in row.visible_trees():
                visible_trees.add((i, visible_tree))

        for i, column in enumerate(self.columns):
            for visible_tree in column.visible_trees():
                visible_trees.add((visible_tree, i))            

        return len(visible_trees)

    @staticmethod
    def __number_of_tree_viewable__(tree, trees_in_distance):
        if len(trees_in_distance) == 0:
            return 0
        
        count = 1
        for tree_in_distance in trees_in_distance:
            if tree_in_distance >= tree:
                return count
            elif tree_in_distance < tree:
                count += 1
            
        return len(trees_in_distance)

    def highest_scenic_score(self):
        highest_scenic_score = 0
        for row_number, row in enumerate(self.rows):
            for column_number, tree in enumerate(row.trees):
                up_viewing_distance = Grid.__number_of_tree_viewable__(tree, list(reversed(self.columns[column_number].trees[0:row_number])))
                down_viewing_distance = Grid.__number_of_tree_viewable__(tree, self.columns[column_number].trees[row_number+1:])
                left_viewing_distance = Grid.__number_of_tree_viewable__(tree, list(reversed(self.rows[row_number].trees[0:column_number])))
                right_viewing_distance = Grid.__number_of_tree_viewable__(tree, self.rows[row_number].trees[column_number+1:])

                scenic_score = up_viewing_distance * down_viewing_distance * left_viewing_distance * right_viewing_distance
                if (scenic_score > highest_scenic_score):
                    print(f'tree {tree} at {row_number}:{column_number} with scenic score {scenic_score} (up:{up_viewing_distance},down:{down_viewing_distance},left:{left_viewing_distance},right:{right_viewing_distance})')

                    highest_scenic_score = scenic_score
                
        return highest_scenic_score