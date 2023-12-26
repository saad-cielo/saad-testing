import os

os.system("git add .")

def build_optimizer():
    changed_data = os.popen("git diff --staged").read().split()

    changed_data = [x for x in changed_data if ((x.endswith(".py")) or (x.endswith(".yml") or x.endswith(".yaml"))) and ("build_optimizer" not in x)]
    new_filtered_list = []

    open('saad.sh', 'w').close()
    for one_change in changed_data:
        if "common" in one_change or one_change.endswith((".yml", ".yaml")):
            new_filtered_list = ["serverless deploy"]
            break
        elif one_change.endswith('.py') and "common" not in one_change:
            function_name = one_change[:-3].split('/')[-1]
            new_filtered_list.append(f"serverless deploy function --function {function_name}")

    new_commands = set(new_filtered_list)
    print(new_commands)
    with open('saad.sh', 'a') as f:
        for one_value in new_commands:
            f.write(one_value)
            f.write("\n")

if __name__ == '__main__':
    build_optimizer()
