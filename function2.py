import os ,json
def build_optimizer():
    returned = os.popen("git diff --staged").read().split()
    returned = [x for x in returned if (x.endswith(".py")) or (x.endswith(".yml"))]
    new_list= []
    open('saad.sh', 'w').close()
    print(returned)
    for one_change in returned:
        print(one_change)
        if "common" in one_change or one_change[:-3]==".yml":
            new_list = []
            stringed = "serverless deploy"
            new_list.append(stringed)
            break
        elif one_change.endswith('.py') and "common" not in one_change:
            stringed = f"serverless deploy function --function {one_change[:-3].split('/')[-1]}"
            new_list.append(stringed)


    new_commands = set(new_list)
    with open('saad.sh', 'a') as f:  
        for one_value in new_commands:
            f.write(stringed)
            f.write("\n")

if __name__=='__main__':
    build_optimizer()