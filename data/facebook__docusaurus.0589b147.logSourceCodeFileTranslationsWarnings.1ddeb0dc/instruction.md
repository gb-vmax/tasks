# Bug Report

### Describe the bug

Translation extraction is logging warnings for files that don't have any translation warnings, instead of logging warnings only for files that actually have warnings.

### Reproduction

When running the translation extraction process, I'm seeing warning messages logged for source code files even when there are no actual warnings to report. The log output shows warnings for files that have `warnings.length === 0`, which shouldn't be happening.

Expected behavior: Only files with actual translation warnings should trigger log messages.

Actual behavior: Files without any warnings are generating log messages.

### Steps to reproduce

1. Run translation extraction on a project with some source files
2. Observe that warning messages are being logged for files without warnings
3. Files that actually have translation warnings are being silently ignored

The warning messages appear to be inverted - they're showing up when they shouldn't and not showing up when they should.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
