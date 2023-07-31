#!/usr/bin/env python3

USE_TIMEIT_RESOURCE = True
if USE_TIMEIT_RESOURCE:
  import sys
  sys.path = [p for p in sys.path if not p.endswith('site-packages/timeit_resource')]
  sys.path.insert(0, "/Users/arunsundaram/apps/timeit-resource/src")
  print(sys.path)

from timeit_resource import TimeIt


if __name__ == "__main__":
  with TimeIt():
    for _ in range(1, 1000):
      print("hello world")
