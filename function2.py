import os ,json
returned = os.popen("git diff --staged --name-only").read().split()
new_list= []
for one_change in returned:
    if one_change.endswith('.py'):
        new_list.append(one_change[:-3])
# print(new_list)
with open('test.txt', 'w') as f:
    f.write(json.dumps(new_list))
os.system("more test.txt")
text_sls_deploy = os.popen("more test.txt").read()
print(f"sls deploy list {text_sls_deploy}")