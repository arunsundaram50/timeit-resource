# timeit_resource
`timeit_resource`: Python Resource to easily capture and report time consumed by code snippets.

### Here is the GitHub repo:
- <https://github.com/arunsundaram50/timeit-resource>

### Here is the pip command to install it:
```bash
pip install timeit_resource
```


### Here’s a simple example of how you might use timeit_resource:
```python
  # Write time elapsed information to stdout, with default title (prefix)
  with TimeIt() as timer:
    # Your time-consuming code here
    for _ in range(1000000):
      pass

```


### Here are examples that further explore using timeit_resource:

```python
  TimeIt.prefix = '  '
  
  # Write to stdout, nested
  with TimeIt("Total time taken"):
    from time import sleep
    for _ in range(10):
      with TimeIt("Time taken - outer"):
        for _ in range(10):
          with TimeIt("Time taken - inner"):
            sleep(0.01)


  # Append to output.txt
  with TimeIt(title="Time taken", output="output.txt") as t:
    # Your time-consuming code here
    for _ in range(1000000):
      pass

  # Write to stderr
  with TimeIt(output=sys.stderr) as t:
    # Your time-consuming code here
    for _ in range(1000000):
      pass

  # Write to an output stream that the client owns!
  with open("output.txt", 'w') as f:
    with TimeIt(output=f) as t:
      # Your time-consuming code here
      for _ in range(1000000):
        pass
```