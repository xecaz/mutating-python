import random
import re

def func_8513():
    return random.randint(1, 10)

def func_3101():
    var_2912 = func_8513()
    print(f"Random var_2912: {var_2912}")

    with open(__file__, 'r') as file:
        code = file.read()

    new_names = {
        'func_8513': f"func_{random.randint(1000, 9999)}",
        'var_2912': f"var_{random.randint(1000, 9999)}",
        'func_3101': f"func_{random.randint(1000, 9999)}"
    }

    for old_name, new_name in new_names.items():
        code = re.sub(r'\b' + re.escape(old_name) + r'\b', new_name, code)

    with open(__file__, 'w') as file:
        file.write(code)

if __name__ == "__main__":
    func_3101()
