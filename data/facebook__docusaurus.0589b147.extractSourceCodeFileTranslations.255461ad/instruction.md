# Bug Report

### Describe the bug

I'm experiencing an issue with translation extraction from source code files. When the extraction process encounters an error (like a syntax error in a file), the error message is completely unhelpful - it just shows a generic error without any context about what went wrong or which file caused the problem.

### Reproduction

Try to extract translations from a file that has a syntax error or parsing issue. The error thrown doesn't include the original error details, making it impossible to debug what went wrong.

For example:
1. Have a source file with invalid syntax or a parsing issue
2. Run the translation extraction process
3. Get a generic error with no stack trace or details about the actual problem

### Expected behavior

When translation extraction fails, the error should include:
- The original error message and stack trace
- Information about what caused the parsing to fail
- Context that helps identify and fix the issue

Currently it's really hard to debug translation extraction failures because all the useful error information is being lost.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
