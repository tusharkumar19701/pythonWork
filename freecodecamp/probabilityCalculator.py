import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for atr, val in kwargs.items():
            for i in range(val):
                self.contents.append(atr)

    def draw(self,num):
        if num > len(self.contents):
            content_copy = self.contents.copy()
            self.contents.clear()
            return content_copy
        
        res = []
        while len(res) < num:
            ind = random.randint(0,len(self.contents)-1)
            ele = self.contents[ind]
            self.contents.remove(self.contents[ind])
            res.append(ele)
        return res
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    cnt = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)

        ans = 0
        for j in expected_balls.keys():
            if balls_drawn.count(j) >= expected_balls[j]:
                ans += 1
        
        if ans == len(expected_balls):
            cnt += 1
    
    prob = cnt / num_experiments
    return prob

hat = Hat(yellow=2,blue=3)
