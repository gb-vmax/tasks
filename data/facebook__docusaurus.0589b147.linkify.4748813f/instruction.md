# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link processing in my docs. After updating, it seems like the content isn't being transformed correctly - the links in my markdown files are no longer being converted to their proper permalinks.

### Reproduction

1. Create a markdown file with internal doc links
2. Build the docs
3. The links remain as-is instead of being converted to permalinks

For example:
```md
Check out [this doc](./other-doc.md) for more info.
```

Expected: Link should be converted to the proper permalink
Actual: Link stays as `./other-doc.md` in the output

### Expected behavior

Markdown links should be processed and converted to their corresponding permalinks during the build process. The linkify function should transform the content and return the modified version.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
