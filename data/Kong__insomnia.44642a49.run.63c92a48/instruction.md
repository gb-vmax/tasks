# Bug Report

### Describe the bug

The file template tag is broken after a recent change. When trying to use the file template tag to read file contents, I'm getting a syntax error and the template doesn't work at all.

### Reproduction

1. Create a request with a file template tag
2. Try to reference a file using the template syntax
3. The template fails to execute

Example usage:
```
{% file '/path/to/my/file.txt' %}
```

The template tag should read and return the file contents, but instead it's throwing an error about the function definition.

### Expected behavior

The file template tag should successfully read the file contents and return them as a string, just like it did before.

### Additional context

This seems to have broken recently - the file template was working fine in previous versions. The syntax error appears to be related to how the `run` function is defined in the template tag object.

---
Repository: /testbed
