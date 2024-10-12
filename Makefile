build:
	# Replace --onefile with --standalone if desired.
	# Needs to be adapted for Windows.
	# See https://nuitka.net/user-documentation/ for details
	# uv run nuitka --onefile --static-libpython=yes app/hello.py
	uv run nuitka --onefile src/tui.py

tests:
	uv run pytest

.PHONY: build tests
