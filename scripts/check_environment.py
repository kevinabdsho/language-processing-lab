#!/usr/bin/env python3
"""Small preflight check for Session 01. Uses only the Python standard library."""

from __future__ import annotations

import locale
import platform
import sys
import unicodedata


def status(label: str, ok: bool, detail: str = "") -> bool:
    mark = "OK" if ok else "FAIL"
    suffix = f" — {detail}" if detail else ""
    print(f"[{mark:4}] {label}{suffix}")
    return ok


def main() -> int:
    print("Language Processing Laboratory — environment check\n")

    py_ok = sys.version_info >= (3, 10)
    checks = [
        status("Python >= 3.10", py_ok, platform.python_version()),
        status("Persian string round trip",
               "پردازش".encode("utf-8").decode("utf-8") == "پردازش"),
        status("Persian YEH code point",
               ord("ی") == 0x06CC, f"U+{ord('ی'):04X}"),
        status("Arabic YEH differs from Persian YEH",
               "ي" != "ی"),
        status("ZWNJ code point",
               ord("\u200c") == 0x200C, f"U+{ord(chr(0x200C)):04X}"),
        status("NFC available",
               unicodedata.normalize("NFC", "ا\u0653") == "آ"),
    ]

    print("\nRuntime information")
    print("-------------------")
    print("Platform:", platform.platform())
    print("Default encoding:", sys.getdefaultencoding())
    print("Preferred locale encoding:", locale.getpreferredencoding(False))
    print("stdout encoding:", sys.stdout.encoding)

    if all(checks):
        print("\nEnvironment looks ready for Session 01.")
        return 0

    print("\nOne or more checks failed. See docs/TROUBLESHOOTING_FA.md.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
