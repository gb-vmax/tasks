# Bug Report

### Describe the bug

After a recent update, page front matter validation is broken. When trying to build a site with pages that have front matter, the build process fails with an error about invalid arguments being passed to the validation function.

### Reproduction

Create a page with front matter:

```md
---
title: My Page
description: A test page
---

# Content here
```

Try to build the site - the validation fails and throws an error because the arguments passed to `validateFrontMatter` don't match what the function expects.

### Expected behavior

The front matter should be validated successfully and the page should build without errors, just like it did before the change.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
