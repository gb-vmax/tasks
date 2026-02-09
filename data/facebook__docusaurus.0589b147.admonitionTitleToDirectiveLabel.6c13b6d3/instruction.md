# Bug Report

### Describe the bug

I'm experiencing an issue with admonition directive parsing in markdown content. When using admonitions with two colons (like `::note` or `::warning`), they are now being incorrectly processed and converted, which breaks the expected markdown rendering.

### Reproduction

```markdown
::note My Title
This is a note with two colons
::

:::warning Important
This is a warning with three colons
:::
```

After processing, the two-colon syntax gets transformed when it shouldn't be. This affects markdown files that use the two-colon syntax for other purposes or plugins.

### Expected behavior

Only admonition directives with three or more colons (like `:::note`, `:::warning`, etc.) should be processed and have their titles converted to directive labels. Two-colon syntax should be left untouched as it's not a valid Docusaurus admonition syntax.

### Additional context

This seems to have started happening recently. The regex pattern appears to be matching directives with 2+ colons instead of the standard 3+ colons that Docusaurus uses for admonitions.

---
Repository: /testbed
