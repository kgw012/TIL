def switchToggle(switch):
    return (0 if switch else 1)

def switchBoy(switches, switch):
    idx = switch - 1
    while True:
        if idx >= len(switches):
            break
        switches[idx] = switchToggle(switches[idx])
        idx += switch
        
    return

def switchGirl(switches, switch):
    idx = switch - 1
    switches[idx] = switchToggle(switches[idx])
    offset = 1
    
    while True:
        if idx - offset < 0 or idx + offset >= len(switches):
            break
        if switches[idx - offset] != switches[idx + offset]:
            break
        switches[idx - offset] = switchToggle(switches[idx - offset])
        switches[idx + offset] = switchToggle(switches[idx + offset])
        offset += 1
    
    return

switch_len = int(input())
switches = list(map(int, input().split()))
student_len = int(input())
for i in range(student_len):
    sex, switch = map(int, input().split())
    if sex == 1:
        switchBoy(switches, switch)
    else:
        switchGirl(switches, switch)

for i in range(0, switch_len, 20):
    print(*switches[i : i+20])