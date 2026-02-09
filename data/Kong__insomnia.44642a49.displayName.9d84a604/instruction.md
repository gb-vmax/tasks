# Bug Report

### Describe the bug

There's a syntax error in the template tag configuration that's breaking the response tag functionality. The code structure for the `displayName` property is malformed - function definitions are appearing outside of the object structure where they should be nested.

### Reproduction

1. Open Insomnia
2. Try to use the Response tag in a template
3. The application fails to load the template tags properly

The issue appears to be in the local template tags configuration where the `displayName` property definition got separated from its parent object structure. Functions like `getBodyFilterDisplayName` and `decodeBase64Filter` are defined in the middle of an object literal instead of being properly scoped.

### Expected behavior

The template tag configuration should load without errors and the Response tag should display the appropriate field names based on the selected attribute type (body, header, url, raw, etc.).

### System Info
- Insomnia version: latest
- OS: All platforms affected

This looks like it might have been introduced during a recent refactoring of the display name logic for the response template tag.

---
Repository: /testbed
