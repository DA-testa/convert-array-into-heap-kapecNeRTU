# python3


def build_heap(data):
    swaps = []

    def sift_down(i):
        min_index = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < len(data) and data[left_child] < data[min_index]:
            min_index = left_child

        if right_child < len(data) and data[right_child] < data[min_index]:
            min_index = right_child

        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            sift_down(min_index)

    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(i)

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    inputChoice = input()
    if  inputChoice.lower()[0] == "i":
        n = int(input("input:"))
        data = list(map(int, input().split()))

    elif inputChoice[0] == "F":
        #faila nosaukumam tiek pievienots relatīvais path, citādāk neizpildās testi
        file = open("tests/" + input(), mode="r", encoding="utf-8")
        n = int(next(file))
        data = list(map(int, file.readline().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
