# Bug Report

### Describe the bug

When generating HAR (HTTP Archive) files from requests with file uploads, the code appears to have duplicate/malformed function definitions that cause syntax errors. The `getRequestPostData` function seems to be defined twice with overlapping logic, and there's an improperly nested helper function `_detectFileEncoding` that's defined inside the main function body.

### Reproduction

Try to generate code or export HAR for a request that includes a file upload:

1. Create a request with a file attached (e.g., multipart form data with a file field)
2. Attempt to generate code from the request or export to HAR format
3. The operation fails due to a syntax error in the har.ts module

### Expected behavior

The HAR generation should work correctly for requests with file uploads. The function should properly detect file encoding (text vs binary) and read the file contents accordingly without syntax errors.

### System Info
- Insomnia version: latest
- OS: Any

The issue appears to be in `packages/insomnia/src/common/har.ts` around the `getRequestPostData` function where there's malformed code structure.

---
Repository: /testbed
