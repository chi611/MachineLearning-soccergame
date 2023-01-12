# q_learning.py
# -*- coding: UTF-8 -*-
"""
Q Learning Algorithm
"""

import numpy as np
import pandas as pd
import os

class QLearning:
    model_name = "model_data_testV15.csv"
    def __init__(self, actions, learning_rate=0.01, discount_factor=0.9, e_greedy=0.1):
        self.actions = actions  # action 列表
        self.lr = learning_rate  # 學習速率
        self.gamma = discount_factor  # 折扣因子
        self.epsilon = e_greedy  # 貪婪
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float32)  # Q 表

    def check_state_exist(self, state):
        if state not in self.q_table.index:
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )
            flag = 0
            return flag
        else:
            flag = 1
            return flag


    # 根據 state 來決定 action
    def choose_action(self, state):
        self.check_state_exist(state)  # 檢查當前 state 是否在 q_table 中存在
        # 用 Epsilon Greedy 來選擇行為
        if np.random.uniform() < self.epsilon:
            # 隨機選 action
            action = np.random.choice(self.actions)
        else:  # 選擇 Q 直最高的 action
            state_action = self.q_table.loc[state, :]

            state_action = state_action.reindex(np.random.permutation(state_action.index))
            action = state_action.idxmax()
        return action

    # 更新 Q 表中的值
    def learn(self, s, a, r, s_):
        flag = self.check_state_exist(s_)  # q_table 中是否存在 s_
        # print('flag2')
        # print(flag)

        q_predict = self.q_table.loc[s, a]  # 根據 Q 表得到的 （predict）值
        if s_ != 'terminal':  # state 不是 终止
            q_target = r + self.gamma * self.q_table.loc[s_, :].max()
        else:
            q_target = r  # state 是 终止

        # 更新 Q 表中 state_action 的數值
        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)

    def save(self):
        self.q_table.to_csv(self.model_name, index=True)
        print('save data')
        print(self.q_table)

    def read(self):
        if os.path.isfile(self.model_name):
            self.q_table = pd.read_csv(self.model_name)
            self.q_table.index
            self.q_table.set_index("Unnamed: 0", inplace=True)
        print(self.q_table)
        print('read data')
