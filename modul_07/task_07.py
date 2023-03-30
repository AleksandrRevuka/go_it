def data_preparation(list_data):
    element_all = []
    for list_ in list_data:
        if len(list_) <= 2:
            element_all += list_
        else:
            list_.sort()
            element_all += list_[1:-1]

    return sorted(element_all, reverse=True)
        
    
    
print(data_preparation([[1,2,3],[3,4], [5,6]]))