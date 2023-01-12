# main.py
# -*- coding: UTF-8 -*-

"""
q_learning和env
"""
from gym_unity.envs import UnityToGymWrapper
from mlagents_envs.environment import UnityEnvironment
from q_learning import QLearning
import keyboard

# 控制球員 藍1 紫1 藍2 紫2
# 0為手動操作 1為AI操作
player = [0, 1, 0, 1]

# 關閉AI特定動作,增加特定情況訓練樣本
up_sw = 1
down_sw = 1
left_sw = 1
right_sw = 1

# state數量 0 => 1 會增加100倍的樣本數
decimal = 0

# 最大訓練次數
max_step = 1000
# 單場最大步數
max_step_per_episode = 200

# 動作輸入鍵位 藍1 紫1 藍2
action_d = [['q', 'w', 'r', 'e'], ['x', 'z', 'c', 'v'], ['z', 'x', 'v', 'c']]

cnt = 0
if __name__ == '__main__':
    total_step = 0
    env_path = ".\\SoccerGame\\soccergame_final.exe "

    print('input_sus')
    unity_env = UnityEnvironment(env_path,
                                 base_port=5000,
                                 seed=0,
                                 no_graphics=False,
                                 timeout_wait=60, )
    env = UnityToGymWrapper(unity_env, allow_multiple_obs=True)

    time_cnt = 0
    Q = QLearning(actions=list(['u', 'd', 'l', 'r']))
    action = 'u'
    Q.q_table_read()
    times_cnt = 0
    while total_step < max_step:

        state_re = env.reset()
        current_ep_reward = 0
        state_x = {}
        state_y = {}
        state_z = {}
        # player1 藍1 x =-31 z =1.2
        state_x[0] = state_re[0][3]
        state_y[0] = state_re[0][4]
        state_z[0] = state_re[0][5]

        # player2 紫1 x =31 z =1.2
        state_x[1] = state_re[0][6]
        state_y[1] = state_re[0][7]
        state_z[1] = state_re[0][8]

        # player3 藍2 x =-31 z = -1.2
        state_x[2] = state_re[0][9]
        state_y[2] = state_re[0][10]
        state_z[2] = state_re[0][11]

        # player4 紫2 x =31 z = -1.2
        state_x[3] = state_re[0][12]
        state_y[3] = state_re[0][13]
        state_z[3] = state_re[0][14]

        # soccer
        state_x[4] = state_re[0][0]
        state_y[4] = state_re[0][1]
        state_z[4] = state_re[0][2]

        state_x_last = state_x.copy()
        state_z_last = state_z.copy()
        column, row = 4, 2
        state = [[0] * row for _ in range(column)]
        state_ = [[0] * row for _ in range(column)]
        state_d = {}
        state_d_ = {}
        print('重設')
        for a in range(4):
            # state = 自己位置減球的位置
            state[a] = [round((state_x[a] - state_x[4]), decimal), round((state_z[a] - state_z[4]), decimal)]
            state_d[a] = state_[a][0] ** 2 + state_[a][1] ** 2

        action = {}

        for t in range(1, max_step_per_episode + 1):
            # 選擇1~4號球員動作
            for i in range(4):
                action[i] = Q.choose_action(str(state[i]))
            # print('選動作')
            for i in range(4):
                # 動作由字串轉為數字輸入
                if i <= 2 and player[i] == 1:
                    if action[i] == 'u' and up_sw == 1:
                        keyboard.press(action_d[i][0])
                    elif action[i] == 'd' and down_sw == 1:
                        keyboard.press(action_d[i][1])
                    elif action[i] == 'l' and left_sw == 1:
                        keyboard.press(action_d[i][2])
                    elif action[i] == 'r' and right_sw == 1:
                        keyboard.press(action_d[i][3])
                elif player[i] == 1:
                    if action[i] == 'u' and up_sw == 1:
                        action_new = [[2], [0], [0]]
                    elif action[i] == 'd' and down_sw == 1:
                        action_new = [[1], [0], [0]]
                    elif action[i] == 'l' and left_sw == 1:
                        action_new = [[0], [1], [0]]
                    elif action[i] == 'r' and right_sw == 1:
                        action_new = [[0], [2], [0]]
                    else:
                        action_new = [[0], [0], [0]]
                else:
                    action_new = [[0], [0], [0]]

            # unity回傳資訊
            state_re_, reward, done, _ = env.step(action_new)

            # print('放開選動作')
            for i in range(4):
                # 動作由字串轉為數字輸入
                if i <= 2 and player[i] == 1:
                    if action[i] == 'u':
                        keyboard.release(action_d[i][0])
                    elif action[i] == 'd':
                        keyboard.release(action_d[i][1])
                    elif action[i] == 'l':
                        keyboard.release(action_d[i][2])
                    elif action[i] == 'r':
                        keyboard.release(action_d[i][3])
            # player1 藍1 x =-31 z =1.2
            state_x[0] = state_re_[0][3]
            state_y[0] = state_re_[0][4]
            state_z[0] = state_re_[0][5]

            # player2 紫1 x =31 z =1.2
            state_x[1] = state_re_[0][6]
            state_y[1] = state_re_[0][7]
            state_z[1] = state_re_[0][8]

            # player3 藍2 x =-31 z = -1.2
            state_x[2] = state_re_[0][9]
            state_y[2] = state_re_[0][10]
            state_z[2] = state_re_[0][11]

            # player4 紫2 x =31 z = -1.2
            state_x[3] = state_re_[0][12]
            state_y[3] = state_re_[0][13]
            state_z[3] = state_re_[0][14]

            # soccer
            state_x[4] = state_re_[0][0]
            state_y[4] = state_re_[0][1]
            state_z[4] = state_re_[0][2]

            reward_q = {}
            # print('----------------')
            for a in range(4):
                state_[a] = [round((state_x[a] - state_x[4]), decimal), round((state_z[a] - state_z[4]), decimal)]
                state_d_[a] = state_[a][0] ** 2 + state_[a][1] ** 2
                if done:
                    reward_q[a] = 0

                elif (state_d_[a] ** 0.5) <= 5:  # 球員靠很近時判斷射門方向
                    if state_x[4] > state_x[a]:
                        if state_d_[a] < state_d[a]:
                            reward_q[a] = 200
                        else:
                            reward_q[a] = -20
                    else:
                        if state_d_[a] >= state_d[a]:
                            reward_q[a] = 200
                        else:
                            reward_q[a] = -20
                elif state_x[4] - 3 > state_x[a]:
                    if abs(state_z[a] - state_z[4]) < 3:
                        if state_d_[a] >= state_d[a]:
                            reward_q[a] = 200
                        else:
                            reward_q[a] = -20
                    else:
                        if state_d_[a] < state_d[a]:
                            reward_q[a] = 200
                        else:
                            reward_q[a] = -20

                elif state_d_[a] >= state_d[a]:  # 移動後距離比移動前遠
                    reward_q[a] = -5
                    if state_d[a] - state_d_[a] < -6:
                        reward_q[a] = -50

                elif state_d_[a] < state_d[a]:  # 移動後距離比移動前近
                    reward_q[a] = 100
                    if state_d[a] - state_d_[a] > 6:
                        reward_q[a] = 200
                if reward_q[a] > 0:
                    print('好結果')
                if abs(state_z[a] - state_z[4]) < 3 and state_x[4] - 3 > state_x[a]:
                    if state_z_last[a] - state_z[a] > 0:
                        new_action = 'r'
                    else:
                        new_action = 'l'
                elif abs(state_z[a] - state_z[4]) > 1 and state_x[4] - 3 < state_x[a]:
                    if state_z_last[a] - state_z[a] > 0:
                        new_action = 'r'
                    else:
                        new_action = 'l'
                elif abs(state_x_last[a] - state_x[a]) > abs(state_z_last[a] - state_z[a]) and abs(
                        state_x_last[a] - state_x[4]) >= 0:
                    if state_x_last[a] - state_x[a] > 0:
                        new_action = 'd'
                    else:
                        new_action = 'u'
                else:
                    if state_z_last[a] - state_z[a] > 0:
                        new_action = 'r'
                    else:
                        new_action = 'l'

                # 更新Q表
                if player[a] == 1:
                    Q.learn(str(state[a]), new_action, reward_q[a], str(state_[a]))
            state_x_last = state_x.copy()
            state_z_last = state_z.copy()
            state_d = state_d_.copy()

            state = state_.copy()

            times_cnt = times_cnt + 1
            if times_cnt >= 100:
                Q.q_table_save()
                times_cnt = 0

            if done:
                break
