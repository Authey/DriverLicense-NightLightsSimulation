import random
import time


class LightControl:

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print('这是一个科三灯光练习工具，每道题的答案输入有5秒钟的时间限制')
        print('回答 1 - 远近光灯交替\n回答 2 - 近光灯\n回答 3 - 远光灯\n回答 4 - 危险报警灯+示廓灯')
        return instance

    def __init__(self):
        self.scenarios = {1: '夜间通过急弯', 2: '夜间通过坡道',
                          3: '夜间通过拱桥', 4: '夜间通过人行横道',
                          5: '夜间超越前方车辆', 6: '夜间通过没有信号灯控制的路口',
                          7: '夜间通过有信号灯控制的路口', 8: '夜间同方向近距离跟车',
                          9: '夜间与机动车会车', 10: '夜间在照明良好的道路行驶',
                          11: '夜间在照明不良条件下行驶', 12: '路边临时停车'}
        self.responses = {'远近光灯交替': [1, 2, 3, 4, 5, 6],
                          '近光灯': [7, 8, 9, 10],
                          '远光灯': [11], '危险报警灯+示廓灯': [12]}

        self.scenario_index = 0

    def select_scenario(self):
        idx = random.randint(1, 12)
        self.scenario_index = idx
        return self.scenarios[idx]

    @staticmethod
    def answer_to_response(answer):
        return '远近光灯交替' if answer == 1 else ('近光灯' if answer == 2 else ('远光灯' if answer == 3 else '危险报警灯+示廓灯'))

    def response_verification(self, response):
        return True if self.scenario_index in self.responses[response] else False


if __name__ == '__main__':
    light_control = LightControl()
    count = 0
    for i in range(1, 21):
        scenario = light_control.select_scenario()
        time_start = time.time()
        ans = input('第{}题: {} '.format(i, scenario))
        time_end = time.time()
        if ans in ['1', '2', '3', '4']:
            res = light_control.answer_to_response(int(ans))
        else:
            print('请输入数字1-4回答每道题')
            continue
        time_diff = time_end - time_start
        if time_diff > 5:
            print('回答超时')
            continue
        if light_control.response_verification(res):
            print('回答正确，用时{}'.format(time_diff))
            count += 1
        else:
            print('回答错误，用时{}'.format(time_diff))
    print('答题结束，有{}道题回答正确，正确率{}%'.format(count, count / 0.2))

