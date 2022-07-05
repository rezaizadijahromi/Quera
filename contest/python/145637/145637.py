def new_folder(n):
    folders = []
    folders_dict = {}
    for i in range(n):
        name = input()
        if name not in folders or name not in folders_dict.keys():
            flag = False
            if name not in folders_dict.keys() and name in folders:
                flag = True
            if flag:
                number_name = folders.count(name)
                new_name = f"{name} ({str(number_name)})"
                folders.append(new_name)
                folders_dict[new_name] = 1

                new_folders = str(sorted(folders))
                new_folders = new_folders[1:-1]
                print(new_folders)
            else:
                folders_dict[name] = 1
                folders.append(name)
                new_folders = str(sorted(folders))
                new_folders = new_folders[1:-1]
                print(new_folders)
        elif name in folders and name in folders_dict.keys():
            number_name = folders_dict[name]
            folders_dict[name] += 1
            new_name = f"{name} ({str(number_name)})"
            folders.append(new_name)
            new_folders = str(sorted(folders))
            new_folders = new_folders[1:-1]
            print(new_folders)
    # for i in range(1, n+1):
    #     if i != n:
    #         new_folders = str(sorted(folders[:i]))
    #         new_folders = new_folders[1:-1]
    #         print(new_folders)
    #     else:
    #         folders.sort()
    #         print(str(folders[:i])[1:-1])


n = int(input())
new_folder(n)
