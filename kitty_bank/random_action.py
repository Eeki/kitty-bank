import numpy as np
import robosuite as suite
from robosuite.models.robots.robot_model import register_robot
from kitty_bank_robot import KittyBank
from robosuite.robots import ROBOT_CLASS_MAPPING, SingleArm

ROBOT_CLASS_MAPPING["KittyBank"] = SingleArm
register_robot(KittyBank)


if __name__ == "__main__":
    options = {
        "env_name": "Lift",
        "robots": "KittyBank",
        "controller_configs": {
            "type": "JOINT_VELOCITY",
            "input_max": 1,
            "input_min": -1,
            "output_max": 0.5,
            "output_min": -0.5,
            "kp": 3.0,
            "velocity_limits": [-1, 1],
            "interpolation": None,
            "ramp_ratio": 0.2,
        },
    }

    # initialize the task
    env = suite.make(
        **options,
        has_renderer=True,
        has_offscreen_renderer=False,
        ignore_done=True,
        use_camera_obs=False,
        control_freq=20,
    )
    env.reset()
    env.viewer.set_camera(camera_id=0)

    # Get action limits
    low, high = env.action_spec

    # do visualization
    for i in range(10000):
        action = np.random.uniform(low, high)
        obs, reward, done, _ = env.step(action)
        env.render()
