# Bug Report

### Describe the bug

When generating HAR files from requests with file attachments, I'm getting duplicate function definitions and the code is not executing properly. It looks like the `getRequestPostData` function is being defined twice in the same file, which causes a syntax error.

### Reproduction

1. Create a request with a file body (using `renderedRequest.body.fileName`)
2. Try to export/generate HAR format from this request
3. The code fails to execute due to duplicate function declarations

The issue appears to be in the `har.ts` file where `getRequestPostData` is defined multiple times. The second definition starts around line 405 but the original function body from line 383 onwards is still present, causing conflicts.

### Expected behavior

The HAR generation should work correctly with file bodies. There should only be one `getRequestPostData` function definition that handles both file-based and regular request bodies properly.

### System Info
- Insomnia version: Latest
- OS: Not specified

This seems to have been introduced in a recent change to add file caching functionality. The refactoring left duplicate code in place.

---
Repository: /testbed
