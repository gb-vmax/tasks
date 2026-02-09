# Bug Report

### Describe the bug

I'm experiencing an issue with parsing directives in markdown content. When a directive appears after a lazy continuation line (like in a list or blockquote), it's not being parsed correctly. The directive is either being ignored or treated as regular text instead of being processed as a directive.

### Reproduction

```js
const markdown = `
> This is a blockquote
> with a lazy continuation
::directive
Content
::
`

// The directive is not recognized and gets treated as plain text
```

Another example with lists:

```js
const markdown = `
- List item
  that continues on next line
:::container
This should be a directive
:::
`

// Directive parsing fails in this context
```

### Expected behavior

Directives should be properly recognized and parsed even when they appear after lazy continuation lines in block contexts like blockquotes or lists. The directive syntax (`::` or `:::`) should trigger the directive parser regardless of the preceding content structure.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
