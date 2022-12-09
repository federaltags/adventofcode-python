from dataclasses import dataclass


class CommandRunner:

    def run_for_directories(self, commands):
        directories = {}

        current_dir = ['/']

        for command in commands:
            if command.startswith('$ cd'):
                current_dir.append(command.split("$ cd ",1)[1])
            if not (command.startswith('$') | command.startswith('dir')):
                directories[current_dir[-1]] = directories.get(current_dir[-1], 0) + int(command.split(' ')[0])


        return Directories(directories)


@dataclass
class Directories:
    directories: dict

    def sum_of_big_directory_sizes(self):
        return sum(list(size for size in self.directories.values() if size <= 100000))