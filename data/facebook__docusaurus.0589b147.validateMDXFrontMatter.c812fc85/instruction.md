# Bug Report

### Describe the bug

When processing MDX files with front matter, the validation is not working correctly. It seems like the front matter schema is not being applied, which means invalid front matter fields are not being caught and validated properly.

### Reproduction

Create an MDX file with front matter:

```mdx
---
title: My Page
some_invalid_field: value
another_random_field: 123
---

# Content here
```

Expected: The loader should validate the front matter against the defined schema and reject unknown fields (or at least validate the known ones correctly).

Actual: The front matter passes through without proper validation, and the schema constraints are not enforced.

### Expected behavior

The MDX loader should validate front matter fields against the `MDXFrontMatterSchema` and properly handle unknown fields according to the schema definition. Valid fields should be validated for their types and constraints, while invalid fields should be handled appropriately.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
