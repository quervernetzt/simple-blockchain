import hashlib
from datetime import datetime


class Block(object):
    def __init__(self: object, timestamp: str, data: str, previous_hash: str) -> None:
        """
        Constructor.

        Parameters
        ----------
        timestamp: str, required
            The timestamp when the block is being created.
            Format has to be %Y-%m-%dT%H:%M:%S.%fZ.

        data: str, required
            The input data stored in the block.

        previous_hash: str, required
            The previous hash value. The first block has None as previous_hash.
        """
        self.timestamp: str = timestamp
        self.data: str = data
        self.previous_hash: str = previous_hash
        self.hash: str = self.calc_hash()

    def calc_hash(self: object) -> str:
        """
        Create hash of block. The hash is based on the timestamp and data.

        Returns
        ----------
        str
            Returns the hash in hexidecimal format.
        """
        sha: hashlib._Hash = hashlib.sha256()

        hash_str: str = f"{self.timestamp}\n{self.data}".encode("utf-8")

        sha.update(hash_str)

        return sha.hexdigest()
