from typing import Dict

# The rest of the codebase uses pups everywhere. Only uses these units
# for user facing interfaces
units: Dict[str, int] = {
    "aloe": 10 ** 12,  # 1 aloe (ALOE) is 1,000,000,000,000 pups (1 Trillion)
    "pups:": 1,
    "colouredcoin": 10 ** 3,  # 1 coloured coin is 1000 colouredcoin pups
}
