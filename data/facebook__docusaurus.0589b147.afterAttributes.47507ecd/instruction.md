# Bug Report

### Describe the bug

I'm experiencing an infinite loop issue when parsing directive containers in markdown. The parser seems to hang indefinitely and never completes processing.

### Reproduction

```js
const text = `
:::note{#id .class}
Some content here
:::
`;

// Parser hangs here and never returns
const result = parse(text);
```

### Expected behavior

The parser should complete successfully and return the parsed AST for the directive container with attributes.

### Additional context

This seems to happen specifically when directive containers have attributes (the `{#id .class}` part). Without attributes, parsing works fine. The process just hangs and consumes CPU until I have to kill it.

---
Repository: /testbed
