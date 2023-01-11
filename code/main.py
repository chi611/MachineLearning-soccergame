# main.py
# -*- coding: UTF-8 -*-


from gym_unity.envs import UnityToGymWrapper
from mlagents_envs.environment import UnityEnvironment
from q_learning import QLearning
import keyboard

max_step = 1000
max_step_per_episode = 200
cnt = 0
if __name__ == '__main__':
    total_step = 0
    env_path = "C:\\Users\\ZI-WEI\\Desktop\\RL_shoot_game-master\\1-Q_learning2\\test6\\test20221214.exe"



    unity_env = UnityEnvironment(env_path,
                                 base_port=5000,
                                 seed=0,
                                 no_graphics=False,
                                 timeout_wait=60, )
    env = UnityToGymWrapper(unity_env, allow_multiple_obs=False)

    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.shape[0]


    RL = QLearning(actions=list(['u', 'd', 'l', 'r']))
    action = 'u'
    RL.read()
    while total_step < max_step:


        state_re = env.reset()
        current_ep_reward = 0
        # print(state_re[0])
        state = [(state_re[0]-state_re[3]), (state_re[2]-state_re[5])]
        state = [round(i, 1) for i in state]
        # print(state)
        for t in range(1, max_step_per_episode + 1):
            # print('choose')
            action = RL.choose_action(str(state))

            if keyboard.is_pressed("w"):
                action = 'u'
            elif keyboard.is_pressed("s"):
                action = 'd'
            elif keyboard.is_pressed("a"):
                action = 'l'
            elif keyboard.is_pressed("d"):
                action = 'r'


            # 動作由字串轉為數字輸入
            if action == 'u':
                action_d = [0, 1]
            elif action == 'd':
                action_d = [0, -1]
            elif action == 'l':
                action_d = [-1, 0]
            elif action == 'r':
                action_d = [1, 0]

            # unity回傳資訊
            state_re_, reward, done, _ = env.step(action_d)
            state_ = [(state_re_[0] - state_re_[3]), (state_re_[2] - state_re_[5])]
            state_ = [round(i, 1) for i in state_]
            # if done:
                # reward = -10
            # el
            if reward == 1:
                reward = 100
            elif(state_[0]**2+state_[1]**2) < (state[0]**2 + state[1]**2):
                reward = 10
            else:
                reward = -5
            # 更新Q表
            print('learn')
            RL.learn(str(state), action, reward, str(state_))


            if cnt < 100:
                cnt = cnt + 1
                # print(cnt)
            else:
                cnt = 1
                RL.save()
            #更新狀態
            state = state_
            # print(state_)
            # if reward != 0:
                # print(reward)
            if done:
                break

