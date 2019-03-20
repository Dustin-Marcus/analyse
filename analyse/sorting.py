def bubble_sort(items):
    for x, number in enumerate(items):
        try:
            if items[x+1] < number:
                items[x] = items[x+1]
                items[x+1] = number
                bubble_sort(items)
        except IndexError:
            pass
    return items



def merge_sort(items):
    if len(items)>1:
        mid = len(items)//2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                items[k]=lefthalf[i]
                i=i+1
            else:
                items[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            items[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            items[k]=righthalf[j]
            j=j+1
            k=k+1

    return items



def quick_sort(items):
    if items == []:
        return []
    else:
        return quick_sort([x for x in items[1:] if x < items[0]]) + items[0:1] + \
    quick_sort([x for x in items[1:] if x >= items[0]])