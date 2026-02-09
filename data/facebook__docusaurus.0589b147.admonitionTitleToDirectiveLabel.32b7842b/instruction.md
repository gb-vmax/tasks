# Bug Report

### Describe the bug

I'm experiencing an issue with the `admonitionTitleToDirectiveLabel` function where it's not correctly processing multi-line markdown content with admonition directives. When I have multiple admonitions in the same document, only the first one gets converted properly, and the rest are ignored.

### Reproduction

```js
const content = `
:::note Title 1
Content 1
:::

:::tip Title 2
Content 2
:::

:::warning Title 3
Content 3
:::
`;

const result = admonitionTitleToDirectiveLabel(content, admonitionContainerDirectives);
// Only the first admonition directive gets processed
// The subsequent :::tip and :::warning directives are left unchanged
```

### Expected behavior

All admonition directives in the content should be processed and converted, not just the first occurrence. Each `:::note`, `:::tip`, `:::warning`, etc. should be handled regardless of how many appear in the document.

### Additional context

This seems to have started happening recently. I have markdown files with multiple admonitions and they're not all being transformed as expected. The function appears to stop after processing the first match instead of continuing through the entire content.

---
Repository: /testbed
