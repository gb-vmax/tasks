# Bug Report

### Describe the bug

When processing HTML nodes in markdown with `allowDangerousHtml` set to `false`, the handler is returning the original mdast node instead of `undefined`. This causes the HTML content to leak through in an unexpected format rather than being properly filtered out.

### Reproduction

```js
const state = {
  options: { allowDangerousHtml: false },
  patch: () => {},
  applyData: () => {}
}

const node = {
  type: 'html',
  value: '<script>alert("test")</script>'
}

const result = html(state, node)
// result is now the original node object instead of undefined
// Expected: result should be undefined when allowDangerousHtml is false
```

### Expected behavior

When `allowDangerousHtml` is disabled, HTML nodes should be completely filtered out (return `undefined`), not passed through as the original node object. The current behavior could lead to raw HTML markdown nodes appearing in the transformed output where they shouldn't.

### Additional context

This seems to affect any markdown content with inline HTML when dangerous HTML is not allowed. The HTML should be stripped/ignored entirely rather than being returned in its original form.

---
Repository: /testbed
