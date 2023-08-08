import os ,json
returned = os.popen("git diff --staged --name-only").read().split()
new_list= []
for one_change in returned:
    if one_change.endswith('.py'):
        new_list.append(one_change[:-3])

with open('test.txt', 'w') as f:
    f.write(json.dumps(new_list))

text_sls_deploy = os.popen("more test.txt").read()    
with open("saad.sh" ,"w") as f:
    dot_sh_file_script = f"sls deploy list {new_list}"
    f.write(dot_sh_file_script)