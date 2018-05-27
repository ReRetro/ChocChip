from struct import *
import sys
import os
# CPU Implementation

class Chip8:
    def __init__(self):
        """
        opcode        = pack('H', 0)
        memory        = pack('B', 0)
        V             = pack('B', 0)
        I             = pack('H', 0)
        pc            = pack('H', 0)
        zeroList      = [0] * (64 * 32)
        gfx           = pack('B', *zeroList)
        delayTimer    = pack('B', 0)
        soundTimer    = pack('B', 0)
        """

        self.opcode     = bytearray(2)
        self.memory     = bytearray(4096)
        self.V          = bytearray(16)
        self.I          = bytearray(2)
        self.pc         = bytearray(2)
        self.gfx        = bytearray(64 * 32)
        self.delayTimer = bytearray(1)
        self.soundTimer = bytearray(1)
        self.stack      = bytearray(16)
        self.sp         = bytearray(2)
        self.key        = bytearray(16)

        self.drawFlag   = False

        self.fontset = (
            0xF0, 0x90, 0x90, 0x90, 0xF0,  # 0
            0x20, 0x60, 0x20, 0x20, 0x70,  # 1
            0xF0, 0x10, 0xF0, 0x80, 0xF0,  # 2
            0xF0, 0x10, 0xF0, 0x10, 0xF0,  # 3
            0x90, 0x90, 0xF0, 0x10, 0x10,  # 4
            0xF0, 0x80, 0xF0, 0x10, 0xF0,  # 5
            0xF0, 0x80, 0xF0, 0x90, 0xF0,  # 6
            0xF0, 0x10, 0x20, 0x40, 0x40,  # 7
            0xF0, 0x90, 0xF0, 0x90, 0xF0,  # 8
            0xF0, 0x90, 0xF0, 0x10, 0xF0,  # 9
            0xF0, 0x90, 0xF0, 0x90, 0x90,  # A
            0xE0, 0x90, 0xE0, 0x90, 0xE0,  # B
            0xF0, 0x80, 0x80, 0x80, 0xF0,  # C
            0xE0, 0x90, 0x90, 0x90, 0xE0,  # D
            0xF0, 0x80, 0xF0, 0x80, 0xF0,  # E
            0xF0, 0x80, 0xF0, 0x80, 0x80   # F
        )

        pc     = 0x200
        opcode = 0
        I      = 0
        sp     = 0

        for i in range(0, 80 + 1):
            self.memory[i-1] = self.fontset[i-1]

    def loadGame(self, game):
        with open(game, "rb") as binaryFile:
            buffer = binaryFile.read()
            bufferSize = os.path.getsize(game)
        for i in range(0, bufferSize + 1):
            try:
                self.memory[i + 512] = buffer[i]
            except:
                pass

    def emulateCycle(self):
        # Fetch Opcode
        self.opcode = self.memory[self.pc[0]] << 8 | self.memory[self.pc[0] + 1] << 8
        # self.opcode[1] = self.memory[self.pc[0] + 1] << 8

        # Decode Opcode
        if self.opcode & 0xF000:
            if self.opcode & 0xA000:
                self.I = self.opcode & 0x0FFF

        else:
            print("Unknown opcode: " + str(self.opcode))

        # print(self.opcode)
        for i in range(0, sys.getsizeof(self.memory) - 4):
            print(self.pc[0])
            self.pc[0] += 2

    def setKeys(self):
        pass

if __name__ == "__main__":
    main()
