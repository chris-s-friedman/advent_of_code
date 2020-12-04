import os
from pathlib import Path

year = "2020"

for n in range(1, 25):
    challenge_n = n.__str__().zfill(2)
    challenge_path = Path(year + "/" + challenge_n)
    challenge_path.mkdir()
    for part in ["a", "b"]:
        challenge_path.joinpath((challenge_n + part + ".py")).touch()
