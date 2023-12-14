def findTriplets(lst, k):
    triplet_count = 0
    final_temp_list = []

    for i in range(0, len(lst) - 1):

        s = set()
        temp_list = []

        # Adding first element
        temp_list.append(lst[i])

        curr_k = k - lst[i]

        for j in range(i + 1, len(lst)):

            if (curr_k - lst[j]) in s:
                triplet_count += 1

                # Adding second element
                temp_list.append(lst[j])

                # Adding third element
                temp_list.append(curr_k - lst[j])

                # Appending tuple to the final list
                final_temp_list.append(tuple(temp_list))
                temp_list.pop(2)
                temp_list.pop(1)
            s.add(lst[j])

    return final_temp_list
# Driver code
lst = [10, 20, 30, 9]
k = 59

print(findTriplets(lst, k))
