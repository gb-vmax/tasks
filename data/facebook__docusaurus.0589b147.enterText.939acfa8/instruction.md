# Bug Report

### Describe the bug

I'm encountering an issue with text directives in remark-directive where the parser seems to be passing incorrect arguments to the `enter` function. When processing text directives, the code appears to be wrapping the token in an object structure that doesn't match what the `enter` function expects.

### Reproduction

```js
// When parsing markdown with text directives like:
// :directive[text content]

// The enterText function is called and tries to enter a textDirective node
// but the context and token are being passed incorrectly
```

When processing text directives in markdown content, the parser crashes or produces unexpected results because the function call signature doesn't match what's expected downstream.

### Expected behavior

Text directives should be parsed correctly with the proper context and token structure, similar to how leaf directives are handled. The `enter` function should receive the correct `this` context and token parameter without additional wrapping.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
