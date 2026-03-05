import sys

def page_command(command_type, pid):
    assert command_type in ['read', 'write', 'remove']
    # FOR MY MACBOOK, I USED THIS TO CHECK IN TERMINAL
    # sys.stdout.write(command_type + " " + str(pid) + "\r\n") 
    print(command_type, pid) 


def LRU(n, t, pin):
    best_rid = -1

    best_time = 10**9
    for i in range(n):
        if pin[i] == 0:
            if t[i] < best_time:
                best_time = t[i]
                best_rid = i
    return best_rid


if __name__ == '__main__':
    n, m, q = list(map(int, input().strip('\ufeff').split()))

    # define buffer pool as 4 lists
    page = [0] * n
    pin = [0] * n
    dirty = [False] * n
    t = [0] * n
    num = 0 # the number of pages in the buffer pool

    pid_map = dict() # a dict maps pid to row_id in buffer pool

    cur_time = 0

    for tnow in range(q):
        op, pid = input().split()
        pid = int(pid)
        assert op in ['request', 'release', 'release*']
        if op == 'request':
            cur_time += 1
            if pid in pid_map:
                
                row = pid_map[pid]
                pin[row] += 1
                t[row] = cur_time

            elif num < n:
                
                row = num
                page[row] = pid
                pin[row] = 1
                dirty[row] = False
                t[row] = cur_time
                pid_map[pid] = row
                num += 1
                page_command('read', pid)

            else:
                # buffer replacement
                row = LRU(n, t, pin)
                old_pid = page[row]
                if dirty[row]:
                    page_command('write', old_pid)
                page_command('remove', old_pid)
                del pid_map[old_pid]

                page[row] = pid
                
                pin[row] = 1
                dirty[row] = False
                t[row] = cur_time
                pid_map[pid] = row
                page_command('read', pid)

        else: # release or release*
            if pid not in pid_map:
                continue
            row = pid_map[pid]
            if pin[row] > 0:
                pin[row] -= 1
            if op == 'release':
                dirty[row] = True
