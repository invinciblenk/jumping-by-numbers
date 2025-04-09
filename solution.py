def jump(nums):
    num_element = len(nums)
    i = 0
    visited = set()  #отслеживаем посещенные индексы чтобы в будущем бороться с зацикливанием вроде [3 -1 2 -2 6]
    while i < num_element:
        if nums[i] == 0: #с нулем мы далеко не уйдём...
            return False
        else:
            i = i + nums[i]
        if i in visited:  # Проверка на зацикливание
            return False
        visited.add(i)
        if i < 0: #учитываем вылет в отрицательные i :)
            return False
    return True


user_input = input('Введите элементы массива, раделенные пробелами: ')

array = user_input.split()

array = [int(x) for x in array]

print(jump(array))
#invincible_nk :)
