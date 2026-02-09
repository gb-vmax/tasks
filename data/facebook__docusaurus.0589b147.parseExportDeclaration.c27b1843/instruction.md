# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where export declarations seem to be parsed twice, causing unexpected behavior in the output. When I have a simple export statement in my MDX file, it appears to be duplicated or processed incorrectly.

### Reproduction

```mdx
export const foo = 'bar';

# My Content
```

When this MDX is parsed, the export declaration gets processed in a way that creates duplicate or malformed output. The parsed result doesn't match what I would expect from a single export statement.

### Expected behavior

The export statement should be parsed once and appear correctly in the output. A single `export const foo = 'bar'` should result in a single export declaration in the compiled output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. Not sure if it's related to a recent change in the parser logic, but wanted to report it in case others are seeing the same issue.

---
Repository: /testbed
