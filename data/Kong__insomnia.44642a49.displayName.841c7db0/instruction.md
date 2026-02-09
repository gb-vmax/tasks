# Bug Report

### Describe the bug

After a recent update, the template tag display names for request attributes are showing incorrect labels. When using the request attribute template tag, the display name now includes "(case-insensitive)" appended to labels that shouldn't have this hint, or the labels themselves are different from what they used to be.

### Reproduction

When configuring a template tag for request attributes, the display names shown in the UI are now incorrect:

1. Select "Request" template tag
2. Choose attribute type (e.g., 'oauth2', 'url', 'name', 'folder')
3. Observe the display name shown for the attribute field

Expected display names should be simple labels like "Name" for most attribute types, but now they're showing enhanced labels with additional context hints that weren't there before.

### Expected behavior

The display names should match the original behavior:
- For 'cookie': "Cookie Name"
- For 'parameter': "Query Parameter Name"  
- For 'header': "Header Name"
- For all other types (oauth2, url, name, folder, etc.): "Name"

The labels should NOT include any additional hints or contextual information appended to them.

### System Info
- Insomnia version: latest
- OS: N/A (UI issue)

---
Repository: /testbed
