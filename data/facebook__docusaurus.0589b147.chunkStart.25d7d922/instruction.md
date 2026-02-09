# Bug Report

### Describe the bug

I'm experiencing an issue with directive containers where the linked list structure for document chunks appears to be broken. When processing nested directives or multiple directive containers, the `previous` and `next` references between chunks are not being set up correctly.

### Reproduction

```js
// Parse markdown with nested directive containers
const markdown = `
:::outer
Content in outer

:::inner
Content in inner
:::

More content in outer
:::
`;

// The document chunks are not properly linked
// previous2.next should reference the newly created token
// but the assignment happens before previous2 is updated
```

### Expected behavior

The document chunks should form a proper doubly-linked list where:
1. Each new chunk's `previous` property points to the previous chunk
2. The previous chunk's `next` property points to the new chunk
3. The chain should be maintained correctly throughout parsing

Currently, the chain appears to be breaking because the token assignment and linking logic is in the wrong order.

### System Info
- remark-directive version: 3.0.0
- Parser: micromark

---
Repository: /testbed
