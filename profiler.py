import os
from pathlib import Path

import yappi
import contextlib
from pyinstrument import Profiler


@contextlib.contextmanager
def yappi_context(filename="callgrind.prof"):
    yappi.set_clock_type("WALL")
    directory = Path("profiling/")
    try:
        yappi.start()
        yield
    finally:
        yappi.stop()

        # yappi.get_func_stats().print_all()
        directory.mkdir(parents=True, exist_ok=True)
        yappi.get_func_stats().save(f"{directory}/{filename}", "pstat")

    print("saved!")
    print(f"Run command: $ snakeviz {directory}/{filename}")
    print(f"Run command: $ pyprof2calltree -k -i {directory}/{filename}")


@contextlib.contextmanager
def instrument(filename='results'):
    profiler = Profiler()
    directory = Path("profiling/")
    try:
        profiler.start()
        yield
    finally:
        profiler.stop()
        directory.mkdir(parents=True, exist_ok=True)
        path = os.path.join(directory, f'{filename}.html')
        with open(path, 'w') as fs:
            fs.write(profiler.output_html())

    print(f"Run command: $ xdg-open {path}")



# @router.post("/main")
# async def main(request: Request):
#     with yappi_context():
#         ... 
