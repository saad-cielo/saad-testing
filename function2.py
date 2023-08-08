import os ,json
returned = os.popen("git diff --staged").read().split()
new_list= []
open('saad.sh', 'w').close()

for one_change in returned:
    if "common" in one_change:
        new_list = []
        stringed = "serverless deploy"
        new_list.append(stringed)
        break
    elif one_change.endswith('.py') and "common" not in  one_change:
        stringed = f"serverless deploy function --function {one_change[:-3].split('/')[-1]}"
        new_list.append(stringed)


new_commands = set(new_list)
with open('saad.sh', 'a') as f:  
    for one_value in new_commands:
        f.write(stringed)
        f.write("\n")