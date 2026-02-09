# Bug Report

### Describe the bug

I'm experiencing an infinite loop when parsing directive containers with attributes in markdown. The parser seems to hang indefinitely and never completes when processing certain directive syntax.

### Reproduction

```js
const markdown = `
:::directive{attr="value"}
content
:::
`;

// Parser hangs here and never returns
const result = parse(markdown);
```

### Expected behavior

The parser should successfully process directive containers with attributes and return the parsed result without hanging.

### Additional context

This seems to happen specifically when directives have attributes enclosed in curly braces. Directives without attributes parse fine. The issue appeared recently and causes the entire parsing process to freeze.

---
Repository: /testbed
