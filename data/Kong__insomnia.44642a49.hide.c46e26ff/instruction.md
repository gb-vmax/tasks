# Bug Report

### Describe the bug

I'm experiencing an issue with template tag argument visibility in the UI. When selecting certain template tag types, the second argument field that should be visible is being hidden incorrectly. 

Specifically, when I select 'url' as the first argument value, the second argument field disappears from the UI even though it should remain visible for this option.

### Reproduction

1. Open a request in Insomnia
2. Add a template tag that uses the local template plugins
3. Set the first argument to 'url'
4. Notice that the second argument field is hidden when it should be shown

Expected: The second argument field should only be hidden for values like 'oauth2', 'oauth2-identity', 'oauth2-refresh', 'name', and 'folder'

Actual: The 'url' option also hides the second argument field incorrectly

### System Info
- Insomnia version: latest
- OS: macOS

This seems to affect the visibility logic for template tag arguments. The 'url' option should allow users to input a second argument, but currently the field is being hidden.

---
Repository: /testbed
