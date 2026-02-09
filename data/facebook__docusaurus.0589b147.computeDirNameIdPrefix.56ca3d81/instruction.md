# Bug Report

### Describe the bug

I'm experiencing an issue with document ID generation in the docs plugin. When I have documents in subdirectories with number prefixes, the IDs are being generated incorrectly. It seems like the directory name is not being included in the ID prefix when it should be.

### Reproduction

```
docs/
  01-getting-started/
    intro.md
  02-guides/
    tutorial.md
```

With the above structure and `numberPrefixParser` enabled, the document IDs are not including the directory names as expected. All documents end up with just their base filename as the ID instead of including the directory path.

For example, `intro.md` should have an ID like `getting-started/intro` but it's just getting `intro`.

### Expected behavior

Documents in subdirectories should have their parent directory names included in the ID prefix (with number prefixes stripped when `numberPrefixParser` is enabled). The directory structure should be reflected in the document IDs.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
