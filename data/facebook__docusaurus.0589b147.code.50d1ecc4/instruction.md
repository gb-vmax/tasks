# Bug Report

### Describe the bug

I'm experiencing an issue with code block rendering in MDX. When I have a code block without a meta attribute, the `data.meta` property is being set incorrectly on the node. Additionally, the `<pre>` element seems to be inheriting properties that should only belong to the inner `<code>` element.

### Reproduction

```mdx
# My Document

```js
const hello = 'world';
```
```

When rendering this code block (which has no meta string), the resulting AST node structure appears incorrect. The meta data is being attached when it shouldn't be, and properties are being duplicated between the `<pre>` and `<code>` elements.

### Expected behavior

- Code blocks without meta strings should not have a `data.meta` property set
- The `<pre>` wrapper element should have empty properties `{}`
- Only the inner `<code>` element should have the language class and other relevant properties

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is affecting how code blocks are styled and processed in my application. The incorrect property inheritance is causing CSS selectors to behave unexpectedly.

---
Repository: /testbed
