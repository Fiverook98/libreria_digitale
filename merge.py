#ordinamento della libreria con merge sort
def merge_sort(books):
    if len(books) > 1:
        mid = len(books) // 2
        left_half = books[:mid]
        right_half = books[mid:]

        merge_sort(left_half)
        merge_sort(right_half)


        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i]["title"].lower() < right_half[j]['title'].lower():
                books[k] = left_half[i]
                i += 1
            else:
                books[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            books[k] = left_half[i]
            i+=1
            k+=1

        while j < len(right_half):
            books[k] = right_half[j]
            j+=1
            k+=1
