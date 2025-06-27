from typing import List, Optional
import json

class BrainfInterpreter:
    def __init__(self, memory_size: int = 30000):
        self.memory_size = memory_size
        self.reset()
    
    def reset(self):
        """Reset the interpreter state"""
        self.memory: List[int] = [0] * self.memory_size
        self.pointer: int = 0
        self.instruction_pointer: int = 0
        self.output: str = ""
        self.input_buffer: str = ""
        self.input_index: int = 0
        self.debug_mode: bool = False
        
    def set_input(self, input_string: str):
        """Set input for the program"""
        self.input_buffer = input_string
        self.input_index = 0
    
    def enable_debug(self, enabled: bool = True):
        """Enable or disable debug mode"""
        self.debug_mode = enabled
    
    def _find_matching_bracket(self, code: str, start: int, direction: int) -> Optional[int]:
        """Find matching bracket for loop constructs"""
        bracket_count = 0
        pos = start
        open_bracket = '[' if direction > 0 else ']'
        close_bracket = ']' if direction > 0 else '['
        
        while 0 <= pos < len(code):
            if code[pos] == open_bracket:
                bracket_count += 1
            elif code[pos] == close_bracket:
                bracket_count -= 1
                if bracket_count == 0:
                    return pos
            pos += direction
        
        return None
    
    def _debug_print(self, code: str, instruction: str):
        """Print debug information"""
        if not self.debug_mode:
            return
            
        # Show current state
        mem_view = self.memory[max(0, self.pointer-5):self.pointer+6]
        mem_str = " ".join(f"{x:3d}" for x in mem_view)
        pointer_pos = min(5, self.pointer) * 4
        
        print(f"IP: {self.instruction_pointer:4d} | Cmd: {instruction} | "
              f"Ptr: {self.pointer:4d} | Memory: [{mem_str}]")
        print(f"{' ' * (pointer_pos + 35)}{'^^^'}")
    
    def execute(self, code: str, input_data: str = "") -> str:
        """Execute Brainf**k code and return output"""
        self.reset()
        self.set_input(input_data)
        
        # Remove non-Brainf**k characters
        valid_chars = set("><+-.,[]")
        code = "".join(c for c in code if c in valid_chars)
        
        if not code:
            return ""
        
        # Pre-compute bracket matches for efficiency
        bracket_map = {}
        bracket_stack = []
        
        for i, char in enumerate(code):
            if char == '[':
                bracket_stack.append(i)
            elif char == ']':
                if not bracket_stack:
                    raise SyntaxError(f"Unmatched ']' at position {i}")
                start = bracket_stack.pop()
                bracket_map[start] = i
                bracket_map[i] = start
        
        if bracket_stack:
            raise SyntaxError(f"Unmatched '[' at position {bracket_stack[0]}")
        
        # Execute the program
        while self.instruction_pointer < len(code):
            instruction = code[self.instruction_pointer]
            
            if self.debug_mode:
                self._debug_print(code, instruction)
            
            if instruction == '>':
                self.pointer += 1
                if self.pointer >= self.memory_size:
                    raise RuntimeError(f"Memory pointer overflow at position {self.instruction_pointer}")
            
            elif instruction == '<':
                self.pointer -= 1
                if self.pointer < 0:
                    raise RuntimeError(f"Memory pointer underflow at position {self.instruction_pointer}")
            
            elif instruction == '+':
                self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256
            
            elif instruction == '-':
                self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 256
            
            elif instruction == '.':
                char = chr(self.memory[self.pointer])
                self.output += char
                if not self.debug_mode:
                    print(char, end='', flush=True)
            
            elif instruction == ',':
                if self.input_index < len(self.input_buffer):
                    self.memory[self.pointer] = ord(self.input_buffer[self.input_index])
                    self.input_index += 1
                else:
                    # No more input available, set to 0 or wait for input
                    try:
                        char = input("Input: ")
                        if char:
                            self.memory[self.pointer] = ord(char[0])
                        else:
                            self.memory[self.pointer] = 0
                    except (EOFError, KeyboardInterrupt):
                        self.memory[self.pointer] = 0
            
            elif instruction == '[':
                if self.memory[self.pointer] == 0:
                    self.instruction_pointer = bracket_map[self.instruction_pointer]
            
            elif instruction == ']':
                if self.memory[self.pointer] != 0:
                    self.instruction_pointer = bracket_map[self.instruction_pointer]
            
            self.instruction_pointer += 1
        
        return self.output
    
    def get_dump(self) -> str:
        """Get a formatted dump of memory contents"""
        dump = {}
        dump2 = []
        
        dump["memory-size"]        = self.memory_size
        dump["instruction-ptr"]    = self.instruction_pointer
        dump["memory-cursor"]      = self.pointer
        dump["last-input-buffer"]  = self.input_buffer
        dump["last-output-buffer"] = self.output
        dump["debug-mode?"]        = "true" if self.debug_mode else "false"
        o = 0
        for I in self.memory:
            dump2.append({"address": int(o), "value": int(I)})
            o += 1
        dump["memory-dump"] = dump2
        with open("salahbf-dump.json", "w") as f:
            f.write(json.dumps(dump, indent=4))

