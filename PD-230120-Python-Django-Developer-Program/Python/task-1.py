a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]

def areSimilar(a,b):
    if len(set(a)) == len(set(b)):
        if sorted(a) == sorted(b):
            count = 0
            for idx, val in enumerate(a):
                if val == b[idx]:
                    continue
                else:
                    count = count + 1
                    if count == 3:
                        return False
            else:
                return True
        else:
            return False
    else:
        return False