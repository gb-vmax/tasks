# Bug Report

### Describe the bug

After a recent update, I'm experiencing crashes when loading response data. The application hangs or crashes when trying to access historical responses, particularly those that were saved with body data.

### Reproduction

This seems to happen when:
1. Opening a request that has a saved response with a body
2. The response body was previously stored to disk
3. The application tries to load/display the response

The crash occurs during the response loading phase. It appears to be related to file system operations when reading response bodies.

### Expected behavior

The application should gracefully handle response data loading without crashing, even if the stored response body files have issues or are missing.

### System Info
- Insomnia version: latest
- OS: Various (reproduced on multiple systems)

### Additional context

This appears to affect existing responses that were saved prior to the update. New responses seem to work fine, but historical data causes problems. The issue might be related to how response body compression is being detected or validated.

---
Repository: /testbed
