# Bug Report

### Describe the bug

When using MDX code blocks with admonitions, the content is not being processed correctly. It seems like the admonition titles are being converted to directive labels even when `mdx1Compat.admonitions` is enabled, which shouldn't happen.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  markdown: {
    mdx1Compat: {
      admonitions: true
    }
  },
  // ... other config
}
```

Then create an MDX file with an admonition:

```mdx
:::note My Custom Title
This is the content
:::
```

The admonition title gets transformed unexpectedly even though `mdx1Compat.admonitions` is set to `true`.

### Expected behavior

When `mdx1Compat.admonitions` is enabled, admonition titles should NOT be converted to directive labels. The transformation should only happen when the compatibility mode is disabled (set to `false`).

### Additional context

Also noticed that code blocks might not be getting unwrapped properly in some cases when `headingIds` compat is disabled. The unwrapping seems to only happen conditionally now.

---
Repository: /testbed
