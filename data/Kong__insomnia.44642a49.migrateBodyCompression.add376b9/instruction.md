# Bug Report

### Describe the bug

I'm experiencing an issue with response body compression detection. When loading responses that have compressed bodies, the `bodyCompression` field is being incorrectly set or modified, which causes problems when trying to read the response body later.

### Reproduction

Here's what's happening:

1. Save a response with a gzip-compressed body to disk
2. Load the response back
3. The `bodyCompression` field gets changed unexpectedly
4. When trying to read the body, it either fails to decompress or tries to decompress uncompressed data

I think this is related to how the migration logic handles the `bodyCompression` field. It seems like the code is checking the actual file contents and changing the compression setting based on that, which can cause issues if:
- The file doesn't exist yet
- The file is being read at the wrong time
- There are race conditions with file I/O

### Expected behavior

The `bodyCompression` field should remain stable and not be modified based on file system checks during normal operation. If a response has `bodyCompression` set to a specific value, it should stay that way unless explicitly changed by the user.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

This is causing data integrity issues in our workflow. Any help would be appreciated!

---
Repository: /testbed
