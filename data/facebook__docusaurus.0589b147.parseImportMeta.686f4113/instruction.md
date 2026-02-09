# Bug Report

### Describe the bug
After a recent update, `import.meta` statements in MDX files are causing parsing errors. The parser seems to fail when encountering `import.meta` syntax, which was working fine in previous versions.

### Reproduction
```js
// In an MDX file
const metaUrl = import.meta.url;
console.log(import.meta.env);
```

When trying to parse MDX content that contains `import.meta` expressions, the parser throws an error or fails to recognize the syntax properly.

### Expected behavior
The parser should correctly handle `import.meta` expressions in MDX files, as this is valid ES module syntax. Both `import.meta.url` and other `import.meta` properties should be parsed without errors.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest LTS

This seems like a regression as it was working before. Any help would be appreciated!

---
Repository: /testbed
