from .problem import Problem
from collections import namedtuple

Block = namedtuple('Block', ['id', 'size', 'free'])

class Day9(Problem):
    def PartA(self, input):
        # Parse disk map
        diskmap = [c for c in input]

        # Build block map
        id_incrementer = -1
        blockmap = []
        for i, size in enumerate(diskmap):
            if i % 2 == 0: # File
                blockmap.append(Block(id_incrementer := id_incrementer + 1, int(size), False))
            else: # Free space
                blockmap.extend([Block(None, int(1), True) for i in range(int(size))])
        
        # Reorganize block map, two pointers approach
        ordered_blockmap = []
        left_pointer, right_pointer = 0, len(blockmap) - 1
        while left_pointer <= right_pointer:
            if blockmap[left_pointer].free:
                while blockmap[right_pointer].free:
                    right_pointer -= 1
               
                ordered_blockmap.append(Block(blockmap[right_pointer].id, 1, False))
                blockmap[right_pointer] = Block(blockmap[right_pointer].id, blockmap[right_pointer].size - 1, False)
                
                if blockmap[right_pointer].size == 0:
                    right_pointer -= 1
            else:
                ordered_blockmap.append(blockmap[left_pointer])
            left_pointer += 1
        
        # Calculate and return checksum
        incrementer = -1
        return sum(
            sum((incrementer := incrementer + 1) * block.id
            for _ in range(block.size))
            for block in ordered_blockmap
        )

    def print_blockmap(self, blockmap):
        for item in blockmap:
            print(('.' if item.free else str(item.id)) * item.size, end = '')
        print()

    def PartB(self, input):
        # Parse disk map
        diskmap = [c for c in input]

        # Build block map
        id_incrementer = -1
        blockmap = []
        for i, size in enumerate(diskmap):
            blockmap.append(Block((id_incrementer := id_incrementer + 1) if i % 2 == 0 else None, int(size), i % 2 != 0))

        ordered_blockmap = []
        right_pointer = len(blockmap) - 1
        next_id = id_incrementer
        while right_pointer >= 0:
            next_block = blockmap[right_pointer]
            while next_block.free:
                right_pointer -= 1
                next_block = blockmap[right_pointer]

            left_pointer = 0
            while left_pointer < right_pointer:
                if blockmap[left_pointer].free:
                    if blockmap[left_pointer].size >= next_block.size:
                        delete_extra = False
                        if blockmap[left_pointer].size > next_block.size:
                            remainder_size = blockmap[left_pointer].size - next_block.size
                            if blockmap[left_pointer + 1].free:
                                original_size = blockmap[left_pointer + 1].size
                                blockmap[left_pointer + 1] = Block(None, original_size + remainder_size, True)
                            else:
                                blockmap.insert(left_pointer + 1, Block(None, remainder_size, True))
                                delete_extra = True
                        blockmap[left_pointer] = next_block
                        blockmap.insert(right_pointer + 1, Block(None, blockmap[left_pointer].size, True))
                        del blockmap[right_pointer + (2 if delete_extra else 0)]
                        break
                left_pointer += 1
            right_pointer -= 1

        solution = 0
        total_index = 0
        for i in range(len(blockmap)):
            next_block = blockmap[i]
            if blockmap[i].free:
                total_index += blockmap[i].size
            else:
                for j in range(blockmap[i].size):
                    solution += total_index * blockmap[i].id
                    total_index += 1
        return solution