def check_loadinf_prog(a):
    if a == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    return f"{a}% [{'%'* (a // 10)}{'.' * (10 -(a // 10))}]\nStill loading..."

bar_value = int(input())

print(check_loadinf_prog(bar_value))
