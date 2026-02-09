# Bug Report

### Describe the bug

I'm experiencing an issue with markdown strong/bold text formatting. When using custom strong markers in the markdown options, the output is incorrect. Instead of using the configured marker, it seems to be evaluating to something unexpected.

### Reproduction

```js
const options = {
  strong: '**'
}

// Generate markdown with strong text
const result = toMarkdown(ast, options)

// Expected: uses '**' as the strong marker
// Actual: the marker appears to be wrong or missing
```

When I configure the `strong` option to use a specific marker (like `'**'`), the generated markdown doesn't respect this setting properly. The peek function for strong formatting seems to be returning an incorrect value.

### Expected behavior

The markdown generator should use the configured strong marker from `state.options.strong` when provided, and fall back to `"*"` as the default when no option is set.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
