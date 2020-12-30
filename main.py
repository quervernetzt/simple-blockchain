from datetime import datetime
from solution.linked_list import LinkedList
from solution.block import Block

if __name__ == "__main__":
    ###################################
    # Demo
    ###################################
    block_chain: LinkedList = LinkedList()

    first_block: Block = Block(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"), "first", None)
    block_chain.prepend(first_block)

    second_block: Block = Block(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"), "second", first_block.hash)
    block_chain.prepend(second_block)

    third_block: Block = Block(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"), "third", second_block.hash)
    block_chain.prepend(third_block)

    print(block_chain.size()) # 3
    print("-----------")
    for block in block_chain.to_list():
        print(block.timestamp) # UTC time when the corresponding block has been created e.g. 2020-12-29T09:17:43.732627Z
        print(block.data) # first, second or third
        print("-----------")
        