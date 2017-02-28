file_name = 'Access.txt'
auth_type = 'r+'

record_list =list([])
with open (file_name,auth_type) as f:
    for eachline in f:
        record_list.append(eachline)
print(record_list)

# if [record_list[1]] == ['USER','ACCESS','NTNAME']:
#     print(record_list[1])
#     print('It works')
# else:
#     print('No Idea')


