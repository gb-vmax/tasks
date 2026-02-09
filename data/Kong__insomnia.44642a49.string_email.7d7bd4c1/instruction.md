# Bug Report

### Describe the bug

When importing Swagger 2.0 specifications, email parameter examples are being generated with the current browser's hostname instead of using a standard domain like 'example.com'. This causes issues when the application is accessed from different domains or when running in environments without a proper hostname.

### Reproduction

1. Open Insomnia in a browser environment where `document.host` is undefined or empty
2. Import a Swagger 2.0 spec that contains an email parameter (e.g., `userEmail`)
3. Check the generated example value for the email parameter

Expected: `user@example.com` or similar standard example email
Actual: `user@undefined` or similar malformed email address

### Additional context

This appears to be related to how email examples are generated during the import process. The issue is particularly noticeable when:
- Running in Node.js environments where `document` is not available
- Testing with automated tools
- Using the application in non-browser contexts

The generated email addresses should use a consistent, standard domain rather than relying on the runtime environment's hostname.

---
Repository: /testbed
