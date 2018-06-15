"""
Martin Kersner, m.kersner@gmail.com
seoulai.com
2018
"""
import seoulai_gym as gym
from seoulai_gym.envs.checkers.agents import RandomAgentLight
from seoulai_gym.envs.checkers.agents import RandomAgentDark


def main():
    env = gym.make("Mighty")

    a1 = RandomAgent("Agent 1")
    a2 = RandomAgent("Agent 2")
    a3 = RandomAgent("Agent 3")
    a4 = RandomAgent("Agent 4")
    a5 = RandomAgent("Agent 5")

    obs = env.reset()

    current_agent = a1
   
    '''
    rew = 0
    done = False

    while True:
        from_row, from_col, to_row, to_col = current_agent.act(obs, rew, done)
        try:
            obs, rew, done, info = env.step(current_agent, from_row, from_col, to_row, to_col)
        except ValueError:
            print(f"Invalid move by {current_agent} agent.")
            break

        # switch agents
        temporary_agent = current_agent
        current_agent = next_agent
        next_agent = temporary_agent

        env.render()

        if done:
            print(f"Game over! {current_agent} agent wins.")
            obs = env.reset()
    '''
    env.close()


if __name__ == "__main__":
    main()
