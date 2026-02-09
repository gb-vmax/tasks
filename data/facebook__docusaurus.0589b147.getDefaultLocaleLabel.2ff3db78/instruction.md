# Bug Report

### Describe the bug

The default locale label generation is broken - it's not capitalizing the first letter correctly and is returning the wrong substring of the language name.

### Reproduction

When I set up a site with a non-English default locale, the language name displayed in the UI is incorrect. For example:

```js
// Expected: "Français"
// Actual: "français" (entire original string instead of capitalized version)
```

The issue appears to be in how the default locale label is being generated from the language name. It seems like the first character isn't being properly capitalized and the rest of the string is being handled incorrectly.

### Expected behavior

The default locale label should:
1. Capitalize the first character of the language name
2. Keep the rest of the original language name intact
3. Return a properly formatted string like "English", "Français", "Español", etc.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
