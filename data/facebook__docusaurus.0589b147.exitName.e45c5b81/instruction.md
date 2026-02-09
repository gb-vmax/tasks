# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing in remark. When using directives (container, leaf, or text directives), the directive name is not being set correctly on the node. It appears that the name property remains empty even when explicitly provided in the markdown.

### Reproduction

```js
// Example markdown with directives
const markdown = `
:::note
This is a note directive
:::

::warning
This is a leaf directive
::

:info[inline directive]
`;

// After parsing, the directive nodes have empty name properties
// Expected: node.name === 'note', 'warning', 'info'
// Actual: node.name === ''
```

### Expected behavior

When parsing markdown with directives, the `name` property of directive nodes should be populated with the directive name (e.g., 'note', 'warning', 'info'). Currently, all directive nodes end up with an empty string as their name.

### Additional context

This seems to have broken recently. The directive syntax is being recognized and parsed into the correct node types (containerDirective, leafDirective, textDirective), but the names aren't being extracted from the tokens properly.

---
Repository: /testbed
