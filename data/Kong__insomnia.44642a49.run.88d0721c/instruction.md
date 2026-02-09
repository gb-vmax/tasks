# Bug Report

### Describe the bug

The timestamp template tag is broken after a recent update. When trying to use it in requests, I get an error about the template tag not being properly defined. The timestamp functionality that was working before is now completely non-functional.

### Reproduction

1. Create a new request
2. Try to use the timestamp template tag with any format (e.g., `{% timestamp %}`, `{% timestamp 'iso-8601' %}`, or `{% timestamp 'unix' %}`)
3. The template tag fails to render and breaks the request

### Expected behavior

The timestamp template tag should work as before:
- `{% timestamp %}` or `{% timestamp 'iso-8601' %}` should return an ISO-8601 formatted date
- `{% timestamp 'unix' %}` should return Unix timestamp in seconds
- `{% timestamp 'millis' %}` should return timestamp in milliseconds
- `{% timestamp 'custom', 'yyyy-MM-dd' %}` should return a custom formatted date

All of these were working in the previous version but now fail to execute.

### Additional context

This appears to have started happening after some changes to the template tag system. The timestamp tag is essential for our API testing workflow where we need to include current timestamps in request headers and bodies.

---
Repository: /testbed
