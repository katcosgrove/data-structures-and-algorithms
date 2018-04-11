def towers_of_hanoi(n):
    """Validate tower argument and trigger recursion."""
    if type(n) is not int:
        raise TypeError('Please enter an integer!')
    moves = move_tower(n, 'A', 'C', 'B')
    return moves


def move_tower(discs, origin, target, helper):
    """Handle recursive shuffle of discs."""
    temp = []
    if discs > 0:
        move_tower(discs - 1, origin, helper, target)
        temp.append(f'move disk from {origin} to {target}')
        move_tower(discs - 1, helper, target, origin)
    return temp
