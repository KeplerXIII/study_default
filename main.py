# with open(file1, encoding='utf-8') as file_1:
#     text1_list = file_1.readlines()
#     text1_len = str(len(text1_list))
#     text1_list.insert(0, text1_len + "\n")
#     text1_list.insert(0, file1 + '\n')
#
# with open(file2, encoding='utf-8') as file_2:
#     text2_list = file_2.readlines()
#     text2_len = str(len(text2_list))
#     text2_list.insert(0, text2_len + "\n")
#     text2_list.insert(0, file2 + '\n')
#
# with open(file3, encoding='utf-8') as file_3:
#     text3_list = file_3.readlines()
#     text3_len = str(len(text3_list))
#     text3_list.insert(0, text3_len + "\n")
#     text3_list.insert(0, file3 + '\n')
#
# sort_list = [text1_list, text2_list, text3_list]
# sort_list.sort(key=len)

# with open("4.txt", "w", encoding='utf-8') as file_4:
#     file_4.write(
#         "".join(sort_list[0]) + "\n" + "".join(sort_list[1]) + "\n" + "".join(sort_list[2]))