import struct

class UserData:
    def __init__(self, id, username):
        
        self.id = id
        
        self.username = username
        

    def serialize(self):
        # Przykład binarnej serializacji (format: i = int, 20s = string)
        return struct.pack('i20s', self.id, self.username.encode())

    @staticmethod
    def deserialize(data):
        unpacked = struct.unpack('i20s', data)
        return UserData(unpacked[0], unpacked[1].decode().strip('\x00'))