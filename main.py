def arithmetic_arranger(nums, res=False):
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    opperands = ['+', '-']
    splitted_nums = [i.split() for i in nums]
    nums_opperands = [i.pop(1) for i in splitted_nums]
    formated_first_line = ''
    formated_second_line = ''
    formated_lines = ''
    formated_results = ''

    if len(splitted_nums) > 5:
        return 'Error: Too many problems.'
    for i in nums_opperands:
        if i not in opperands:
            return 'Error: Operator must be \'+\' or \'-\'.'
    for num, i in enumerate(splitted_nums):
        max_num = len(max(i, key=len))
        for x in i:
            if len(x) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            for z in x:
                if z not in numbers:
                    return 'Error: Numbers must only contain digits.'
        first_line = i[0].rjust(max_num + 2) + '    '
        second_line = nums_opperands[num] + i[1].rjust(max_num + 1) + '    '
        lines = '-' * (int(max_num) + 2) + '    '

        formated_first_line += first_line
        formated_second_line += second_line
        formated_lines += lines
        
       
        if nums_opperands[num] == '+':
            result = str(int(i[0]) + int(i[1])).rjust(max_num + 2) + '    '
        else:
            result = str(int(i[0]) - int(i[1])).rjust(max_num + 2) + '    '
        formated_results += result

        
    if res:
        return formated_first_line[0:-4] + '\n' + formated_second_line[0:-4] + '\n' + formated_lines[0:-4] + '\n' + formated_results[0:-4]
   
    return formated_first_line[0:-4] + '\n' + formated_second_line[0:-4] + '\n' + formated_lines[0:-4]

    

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))