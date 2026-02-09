# Bug Report

### Describe the bug

I'm experiencing an issue with template tag attribute selection in the UI. After a recent update, certain attributes that should be visible in the dropdown are not showing up anymore. Specifically, when trying to select attributes like `parameter`, `header`, or `cookie`, they don't appear as options even though they should be available.

### Reproduction

Steps to reproduce:
1. Open a request that uses template tags
2. Try to access the attribute dropdown for a response tag
3. Notice that `parameter`, `header`, and `cookie` options are missing from the list
4. These attributes were previously visible and selectable

### Expected behavior

The dropdown should show all available attributes including `parameter`, `header`, and `cookie` when they are valid options for the selected context. These attributes should not be hidden from the user.

### Additional context

This seems to have started happening recently. The basic attributes like `url`, `oauth2`, etc. are correctly hidden as expected, but the filtering logic appears to be too aggressive and is hiding attributes that should be visible.

---
Repository: /testbed
