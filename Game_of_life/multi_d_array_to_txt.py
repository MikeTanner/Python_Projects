import random
import csv


def array_to_txt(arr, meta):
    file_name = str(random.randint(0, 100000)) + "game_of_life_save"
    file_write = open(
        f"/home/mike/repos/Python/Projects/Game_of_life/{file_name}.txt", "w"
    )
    write = csv.writer(file_write)
    write.writerow(meta)
    for rnd in range(len(arr)):
        write.writerows(arr[rnd])
    print("Saved!")


def txt_to_array(file_name):
    file_read = open(file_name, "r")
    n, width, height = map(lambda x: int(x), file_read.readline().split(","))
    game_arr = []
    for rnd in range(n):
        game_arr.append([])
        for y in range(height):
            line = file_read.readline().split(",")
            game_arr[rnd].append(clean_array(line))
    return game_arr
    file_read.close()


def clean_array(arr):
    step_one = list(map(lambda x: x.strip(), arr))
    # print(step_one)
    step_two = list(map(lambda x: int(x), step_one))
    return step_two


"""n = 2
width = 4
height = 3
arr = [
    [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 0]],
    [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1]],
]
# array_to_txt(arr, (n, width, height))
txt_to_array("/home/mike/repos/Python/Projects/Game_of_life/22981game_of_life_save.txt")
"""
