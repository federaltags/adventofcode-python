from dataclasses import dataclass


class CommandRunner:

    def run_for_directories(self, commands):
        directories = {}

        current_dir = ['/']

        for command in commands:
            if command == "$ cd ..":
                current_dir.pop()
            elif command.startswith('$ cd'):
                current_dir.append(command.split("$ cd ",1)[1])
            elif not (command.startswith('$') | command.startswith('dir')):
                for i in range(len(current_dir)):
                    path = '/'.join(current_dir[0:i+1])
                    directories[path] = directories.get(path, 0) + int(command.split(' ')[0])

        # 24933642
        # 30000000

        return Directories(directories)


@dataclass
class Directories:
    directories: dict

    def sum_of_big_directory_sizes(self):
        return sum(list(size for size in self.directories.values() if size <= 100000))

    def size_of_smallest_dir_to_delete(self):
        unused_space = 70_000_000 - self.directories['/']
        too_free_up = 30_000_000 - unused_space

        for size in sorted(self.directories.values(), reverse=False):
            if size >= too_free_up:
                return size