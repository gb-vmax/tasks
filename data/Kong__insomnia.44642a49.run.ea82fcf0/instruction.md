# Bug Report

### Describe the bug

The File template tag is throwing errors when trying to read files. It looks like there's a syntax issue with the template tag definition that's preventing it from working properly.

### Reproduction

1. Create a new request in Insomnia
2. Add a template tag for reading a file (e.g., `{% file '/path/to/file.txt' %}`)
3. Try to send the request

The request fails with a syntax error instead of reading the file content.

### Expected behavior

The File template tag should successfully read the file content and include it in the request. Previously this was working fine for reading text files.

### Additional context

This seems to have broken recently. The template tag picker shows the File option but using it causes errors. I tried with both absolute and relative paths and different file types but none of them work.

---
Repository: /testbed
