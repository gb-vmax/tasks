# Bug Report

### Describe the bug

I'm experiencing an issue with front matter validation where string values are being incorrectly converted to `[object Object]` instead of being preserved as-is. This appears to affect the YAML front matter parser when handling string fields.

### Reproduction

```yaml
---
title: "My Blog Post"
description: "A detailed description"
---
```

When parsing this front matter, the string values are not being handled correctly and end up being converted to object representations instead of staying as strings.

### Expected behavior

String values in front matter should remain as strings and not be converted to their object representation. The validation should pass through string values unchanged.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently and is breaking my documentation site's front matter processing. Any help would be appreciated!

---
Repository: /testbed
