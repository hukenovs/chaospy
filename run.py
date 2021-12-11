r"""Main function to run chaotic model

"""

from src.dynamic_system import DynamicSystem


if __name__ == '__main__':
    chaotic_system = DynamicSystem(input_args=None, show_log=True)
    chaotic_system.run()
