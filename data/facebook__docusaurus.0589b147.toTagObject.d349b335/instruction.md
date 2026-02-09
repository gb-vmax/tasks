# Bug Report

### Describe the bug

Tags are not being generated correctly - the label and permalink values appear to be swapped or transformed incorrectly. When I define tags in frontmatter, the tag label is being converted to kebab-case and the permalink is being converted to camel-case, which seems backwards.

### Reproduction

When I add tags to my markdown files like this:

```yaml
---
title: My Post
tags: [Hello World, JavaScript Tips]
---
```

The generated tag objects have:
- label: `hello-world` (kebab-cased)
- permalink: `helloWorld` (camel-cased)

But I would expect:
- label: `Hello World` (original string)
- permalink: `hello-world` (kebab-cased for URL)

### Expected behavior

Tag labels should preserve the original string from frontmatter, and permalinks should be kebab-cased for proper URL formatting. Currently it seems like these are reversed or incorrectly transformed.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
