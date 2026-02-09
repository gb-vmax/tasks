# Bug Report

### Describe the bug

The timestamp template tag is not working anymore. When I try to use it in my requests, it throws an error about the `run` function not being defined. This seems to have broken after a recent update.

### Reproduction

1. Create a new request in Insomnia
2. Add a template tag for timestamp (e.g., `{% timestamp %}`)
3. Try to send the request

The request fails with an error indicating that the template tag cannot be executed properly.

### Expected behavior

The timestamp template tag should generate the current timestamp in the specified format (iso-8601, millis, unix, etc.) just like it did before. For example:
- `{% timestamp 'iso-8601' %}` should return something like `2024-01-15T10:30:00.000Z`
- `{% timestamp 'millis' %}` should return the current time in milliseconds
- `{% timestamp 'unix' %}` should return the current unix timestamp

### System Info
- Insomnia version: latest
- OS: N/A

This is blocking my workflow as I rely heavily on timestamp generation for API testing. Would appreciate a quick fix!

---
Repository: /testbed
