# Bug Report

### Describe the bug

When adding custom front matter fields to MDX files, the loader is rejecting them even though they should be allowed. This is breaking our documentation build where we use additional metadata fields beyond the standard ones.

### Reproduction

Create an MDX file with custom front matter:

```mdx
---
title: My Page
description: Page description
customField: some value
anotherCustomField: another value
---

# My Content
```

The build fails because the custom fields (`customField`, `anotherCustomField`) are not recognized, even though custom front matter should be supported.

### Expected behavior

Custom front matter fields should be allowed and passed through without validation errors. Only the standard MDX front matter fields (like `title`, `description`) should be validated, while additional custom fields should be permitted for user-specific needs.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
