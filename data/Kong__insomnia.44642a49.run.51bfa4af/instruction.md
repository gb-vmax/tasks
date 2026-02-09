# Bug Report

### Describe the bug

After a recent update, the file template tag is not working correctly. When I try to read a file using the template tag, it appears to be returning base64-encoded content for binary files instead of the raw file content like it used to.

### Reproduction

1. Create a template that reads a binary file (e.g., PNG, PDF, ZIP)
2. Use the file template tag to include the file content
3. The content is now base64-encoded instead of being returned as-is

Example:
```
{% file '/path/to/image.png' %}
```

Previously this would return the raw binary content, but now it's returning a base64 string.

### Expected behavior

The file template tag should return the raw file content as it did before, without automatically encoding binary files to base64. If encoding is needed, it should be an explicit option or a separate template tag.

This is breaking existing workflows where we were reading binary files directly.

### Additional context

This also seems to affect JSON files - they're being parsed and re-stringified which removes formatting and comments. Would be great if the original file content could be preserved as-is.

---
Repository: /testbed
