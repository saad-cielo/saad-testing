import os ,json
os.system("git diff --staged --name-only")
print("d  dsscsvcpu")
returned = os.popen("git diff --staged --name-only").read().split()
new_list= []
for one_change in returned:
    if one_change.endswith('.py'):
        new_list.append(one_change)
print(new_list)
with open('test.txt', 'w') as f:
    f.write(json.dumps(new_list))