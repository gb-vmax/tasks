# Bug Report

### Describe the bug

The File template tag is broken after a recent update. When trying to read file contents using the template tag, I'm getting syntax errors and the tag doesn't work at all.

### Reproduction

1. Create a new request in Insomnia
2. Add a template tag and select "File"
3. Choose any text file
4. Try to send the request

The request fails to process and the file contents are not read.

### Expected behavior

The File template tag should read the file contents as UTF-8 text by default, just like it did before. The template should be processed without errors and the file contents should be inserted into the request.

### System Info
- Insomnia version: Latest
- OS: N/A

This was working fine in the previous version. Something must have changed with how the file template tag is being registered or processed.

---
Repository: /testbed
