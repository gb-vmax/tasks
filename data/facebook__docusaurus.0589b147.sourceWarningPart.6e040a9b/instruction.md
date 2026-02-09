# Bug Report

### Describe the bug

When translation extraction warnings are generated for source code files, the reported line numbers are incorrect. The warning messages show the wrong line location for translation issues, making it difficult to locate and fix the actual problems in the source code.

### Reproduction

Create a source file with translation calls that trigger warnings (e.g., missing translation IDs or malformed translate calls). When the translation extraction runs and generates warnings, the line numbers in the warning output don't match the actual location of the problematic code in the file.

For example, if a translation issue exists on line 10 of a file, the warning message might report a different line number, pointing to the end of the code block instead of where the issue actually occurs.

### Expected behavior

The warning messages should accurately report the line number where the translation issue is located in the source file, pointing to the start of the problematic code block to make it easy to find and fix the issue.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
