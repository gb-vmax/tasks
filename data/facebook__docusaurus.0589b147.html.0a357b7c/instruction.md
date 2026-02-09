# Bug Report

### Describe the bug

When processing HTML nodes in markdown with `allowDangerousHtml` disabled, the function is returning an empty object `{}` instead of `undefined`. This causes unexpected behavior in the rendering pipeline where nodes that should be ignored are instead being treated as valid nodes.

### Reproduction

```js
const state = {
  options: {
    allowDangerousHtml: false
  }
};

const node = {
  type: 'html',
  value: '<div>test</div>'
};

// Current behavior: returns {}
// Expected behavior: returns undefined
const result = html(state, node);
console.log(result); // {} instead of undefined
```

### Expected behavior

When `allowDangerousHtml` is disabled, the `html()` function should return `undefined` to indicate that the HTML node should not be processed. Returning an empty object causes the node to be treated as a valid element in the tree, which is incorrect.

### System Info
- remark-rehype version: 11.0.0

---
Repository: /testbed
