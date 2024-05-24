def is_valid(s):
    stack = []
    char_correlation={')': '(', '}': '{', ']': '['}
    expected = ""
    for char in s:
        if char in char_correlation:
            top_element = stack.pop() if stack else "#"
            if char_correlation[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
            
        
    

# Casos de prueba
test_cases = [
    {'input': '()', 'expected': True},
    {'input': '()[]{}', 'expected': True},
    {'input': '(]', 'expected': False},
    {'input': '([)]', 'expected': False},
    {'input': '{[]}', 'expected': True},
]

def run_tests():
    for i, test in enumerate(test_cases):
        result = is_valid(test['input'])
        assert result == test['expected'], f"Test case {i + 1} failed: expected {test['expected']}, got {result}"
    print("Todos los casos de prueba pasaron!")

# Ejecuta los tests
run_tests()