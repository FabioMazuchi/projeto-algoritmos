def merge_sort(array, inicio=0, fim=None):
    if fim is None:
        fim = len(array)
    if (fim - inicio) > 1:
        meio = (inicio + fim) // 2
        merge_sort(array, inicio, meio)
        merge_sort(array, meio, fim)
        merge(array, inicio, meio, fim)


def merge(list, inicio, meio, fim):
    left = list[inicio:meio]
    right = list[meio:fim]
    top_left, top_right = 0, 0

    for k in range(inicio, fim):
        if top_left >= len(left):
            list[k] = right[top_right]
            top_right += 1
        elif top_right >= len(right):
            list[k] = left[top_left]
            top_left += 1
        elif left[top_left] < right[top_right]:
            list[k] = left[top_left]
            top_left += 1
        else:
            list[k] = right[top_right]
            top_right += 1


def is_anagram(first_string, second_string):
    l1 = list(first_string.upper())
    l2 = list(second_string.upper())
    merge_sort(l1, 0, len(l1))
    merge_sort(l2, 0, len(l2))

    return l1 == l2
