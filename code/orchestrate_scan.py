import subprocess
import time
import sys
import os

# Import your LTS script (same folder)
from lts_script import run_lts_scan


UUT = "acq1001_694"


def start_acquisition(runtime, root="Encoder_"):
    """
    Launch OCTO-BEE acquisition as a subprocess
    """
    print("\n--- Starting OCTO-BEE Acquisition ---")

    cmd = [
        sys.executable,
        "acq400_stream.py",
        "--verbose=1",
        "--filesize=1011712",
        f"--runtime={runtime}",
        "--root", root,
        UUT
    ]

    return subprocess.Popen(cmd)


def main():
    # USER PARAMETERS (Version 1 hardcoded simple test)
    x_target = 50
    velocity = 10
    acceleration = 5
    runtime = 20
    home = True

    print("\n==============================")
    print(" OCTO-BEE + LTS ORCHESTRATOR ")
    print("==============================\n")

    # 1. Start acquisition FIRST
    acq_proc = start_acquisition(runtime)

    # small delay so stream socket is ready
    time.sleep(2)

    # 2. Run LTS scan (blocking)
    run_lts_scan(
        x_pos=x_target,
        velocity=velocity,
        acceleration=acceleration,
        home=home
    )

    # 3. Wait for acquisition to finish
    print("\n--- Waiting for acquisition to finish ---")
    acq_proc.wait()

    print("\n--- ALL SYSTEMS COMPLETE ---")
    print("Data should now exist in OCTO-BEE output directory")


if __name__ == "__main__":
    main()