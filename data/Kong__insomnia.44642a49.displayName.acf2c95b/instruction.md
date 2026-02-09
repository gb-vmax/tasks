# Bug Report

### Describe the bug

After a recent update, the template tag attribute name display is broken. When trying to use request variables in the templating system, the UI shows malformed text instead of the proper attribute names.

### Reproduction

1. Open a request in Insomnia
2. Try to add a template tag for request attributes (cookie, parameter, or header)
3. Look at the displayed name for the attribute field

The display name appears to be incorrectly formatted or showing unexpected text like "Cookie Name (case-insensitive)" when it should just show "Cookie Name".

### Expected behavior

The attribute name fields should display clean, readable names:
- "Cookie Name" for cookies
- "Query Parameter Name" for parameters  
- "Header Name" for headers
- "Name" for other types

The hint text like "(case-insensitive)" or "(parent name)" shouldn't be appended to the display name.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
