def deadVolinteers(total, list_volunteers):
    lost_boards = ""
    for i in range(1, total + 1):
        if i not in list_volunteers:
            lost_boards += str(i) + " "
    return lost_boards


while True:
    try:
        num_volunteers = list(map(int, input().split()))  # N and R

        if num_volunteers[0] == num_volunteers[1]:
            trash = input()
            print("*")
        else:
            board_volunteers = list(map(int, input().split()))
            print(deadVolinteers(num_volunteers[0], board_volunteers))

    except EOFError:
        break
