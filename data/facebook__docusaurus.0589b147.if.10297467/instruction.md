# Bug Report

### Describe the bug

I'm experiencing an issue with admonitions not rendering correctly after updating to the latest version. It seems like the default admonition types (note, tip, warning, etc.) are not being recognized anymore.

### Reproduction

When using standard admonition syntax in MDX files:

```md
:::note
This is a note
:::

:::tip
This is a tip
:::
```

The admonitions don't render with the expected styling and behavior. It appears the default admonition configuration is not being applied properly.

### Expected behavior

Admonitions should work out of the box with the default types (note, tip, warning, danger, info, caution) without requiring explicit configuration. The default options should be merged with any user-provided options.

### Additional context

This seems to happen when admonitions are enabled in the MDX loader configuration. The default admonition types that should be available by default are not working as expected.

---
Repository: /testbed
