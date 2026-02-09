# Bug Report

### Describe the bug

I'm experiencing an issue with directive containers where the exit order seems incorrect. When parsing container directives, the content exit is happening after the container exit, which appears to be causing problems with the AST structure.

### Reproduction

```js
const directive = `
:::note
Some content here
:::
`;

// Parse the directive container
// The exits are happening in wrong order:
// 1. directiveContainer exits first
// 2. directiveContainerContent exits second
// This should be reversed
```

### Expected behavior

The `directiveContainerContent` should exit before `directiveContainer` exits, following the proper nesting order. Parent nodes should close after their children.

### Additional context

This seems to affect how the parser handles nested directive structures. The closing sequence should mirror the opening sequence in reverse order.

---
Repository: /testbed
