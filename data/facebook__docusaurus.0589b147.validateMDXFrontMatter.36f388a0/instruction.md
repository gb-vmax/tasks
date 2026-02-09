# Bug Report

### Describe the bug

After a recent update, MDX front matter validation is now accepting unknown/undocumented fields without throwing any errors. Previously, the loader would reject front matter with unrecognized properties, which helped catch typos and configuration mistakes.

### Reproduction

Create an MDX file with invalid/unknown front matter fields:

```mdx
---
title: "My Page"
invalidField: "this should not be allowed"
anotherTypo: true
---

# Content here
```

Previously this would fail validation, but now it silently accepts these unknown fields.

### Expected behavior

The MDX loader should reject front matter with unknown properties and provide a clear error message indicating which fields are not recognized. This helps developers catch configuration errors early.

### Additional context

This is particularly problematic because:
1. Typos in front matter field names go unnoticed
2. Deprecated fields are not flagged
3. No feedback when accidentally using incorrect property names

The validation should be strict by default to maintain configuration integrity.

---
Repository: /testbed
