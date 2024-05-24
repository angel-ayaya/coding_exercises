def two_sum(nums, target):
    dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in dict:
            return[dict[complement], i]
        dict[num] = i
    
    
    # #Not best solution
    # for i in range(len(nums)-1):
    #     for j in range(len(nums)):
    #         if i == j:
    #             pass
    #         elif nums[i] + nums[j] == target:
    #             return [i,j]
                
       

            
        
        
        

# Casos de prueba
test_cases = [
    {'input': {'nums': [2, 7, 11, 15], 'target': 9}, 'expected': [0, 1]},
    {'input': {'nums': [3, 2, 4], 'target': 6}, 'expected': [1, 2]},
    {'input': {'nums': [3, 3], 'target': 6}, 'expected': [0, 1]},
]

def run_tests():
    for i, test in enumerate(test_cases):
        result = two_sum(test['input']['nums'], test['input']['target'])
        assert result == test['expected'], f"Test case {i + 1} failed: expected {test['expected']}, got {result}"
    print("Todos los casos de prueba pasaron!")

# Ejecuta los tests
# nums = [3,2,4]
# target = 6
# print(two_sum(nums, target))
run_tests()
