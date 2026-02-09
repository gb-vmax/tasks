# Bug Report

### Describe the bug

The page front matter validation is not working correctly. When I provide invalid front matter in my pages, the validation doesn't catch the errors and allows invalid data to pass through.

### Reproduction

Create a page with invalid front matter:

```md
---
title: 123
description: true
invalid_field: "this shouldn't be allowed"
---

# My Page

Content here
```

The page builds successfully even though the front matter contains invalid types and unknown fields that should be rejected by the schema validation.

### Expected behavior

The validation should throw an error when:
- Front matter fields have incorrect types
- Unknown fields are present (if schema is strict)
- Required fields are missing

The build should fail with a clear validation error message instead of silently accepting invalid front matter.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
