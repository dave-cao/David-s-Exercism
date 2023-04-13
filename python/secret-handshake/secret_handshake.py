"""Exercism Python: Secret Handshake

Problem:
- Create a secret handshake based on binary numbers
- 00001 = wink
- 00010 = double blink
- 00100 = close your eyes
- 01000 = jump
- 10000 = Reverse the order of the operations in the secret handshake.
- Commands go from left to right, unless specified by the reverse command
"""


def commands(binary_str: str) -> list[str]:
    actions = ("Reverse Unneeded", "jump", "close your eyes", "double blink", "wink")

    # list actions in reverse
    output_commands = [actions[i] for i, number in enumerate(binary_str) if int(number)]

    # get rid of reverse uneeded command
    if output_commands and output_commands[0] == "Reverse Unneeded":
        output_commands = output_commands[1:]
    else:
        output_commands.reverse()

    return output_commands
