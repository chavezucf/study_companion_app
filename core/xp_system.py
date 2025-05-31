# For now, basic level thresholds.
# Later could add XP bonuses, streaks, badges, etc.

LEVEL_THRESHOLDS = [100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500]

def get_level_for_xp(xp):
    new_level = 1
    for threshold in LEVEL_THRESHOLDS:
        if xp >= threshold:
            new_level += 1
        else:
            break
    return new_level
