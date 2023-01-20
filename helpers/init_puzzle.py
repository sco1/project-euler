import argparse
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
SOLVE_DIR = BASE_DIR / "project_euler"

SOLVE_BASE = """\
\"\"\"

\"\"\"


if __name__ == "__main__":
    print(f"Solution: {...}")
"""


def init_problem(problem: int | None = None) -> None:  # noqa: D103
    if problem is None:
        # Find first missing digit
        solve_files = SOLVE_DIR.glob("pe_*.py")
        prob_ids = {int(file.stem.split("_")[-1]) for file in solve_files}

        for query in range(1, 102):
            if query not in prob_ids:
                puzzle_base = f"pe_{query:03}"
                break

        if query > 100:
            raise ValueError("Cannot publicly solve problems beyond the first 100")
    else:
        if problem > 100:
            raise ValueError("Cannot publicly solve problems beyond the first 100")

        puzzle_base = f"pe_{problem:03}"

    try:
        solve_path = SOLVE_DIR / f"{puzzle_base}.py"
        solve_path.touch(exist_ok=False)
        solve_path.write_text(SOLVE_BASE)
    except FileExistsError:
        print("Solution file already exists, skipping.")


def main() -> None:  # noqa: D103
    parser = argparse.ArgumentParser()
    parser.add_argument("problem", nargs="?", type=int)

    args = parser.parse_args()
    init_problem(args.problem)


if __name__ == "__main__":
    main()
