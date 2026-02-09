# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing where whitespace handling seems to be broken. The parser is not correctly processing directives when there are spaces before them.

### Reproduction

```js
const input = `
:::note
Some content
:::
`;

// Parser fails to recognize the directive correctly
// The whitespace before the directive causes unexpected behavior
```

When I have a directive with leading whitespace, the parser doesn't handle it properly. It seems like the space consumption logic got flipped somehow - spaces that should be consumed are being returned early, and vice versa.

### Expected behavior

Directives should be parsed correctly regardless of leading whitespace. The parser should consume the appropriate whitespace characters before processing the directive content.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This is blocking my project as many of my markdown files have indented directives. Any help would be appreciated!

---
Repository: /testbed
