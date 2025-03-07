from ds_store import DSStore

with DSStore.open("C:\\Users\\kltz4\\Desktop\\IT\\MyITprojects\\python\\.DS_Store") as ds:
    for item in ds:
        print(item)