# Bug Report

### Describe the bug

Directive names are being displayed incorrectly in error messages. When an unused directive is encountered, the error message shows the wrong directive syntax.

### Reproduction

When using a directive like `:::note` in an MDX file that isn't properly configured, the error message displays the directive with incorrect formatting. For example:

```mdx
:::note
This is a note
:::
```

The error message might show something like `::note` or `:note:` instead of the correct `:::note` syntax that was actually used in the file.

### Expected behavior

The error message should display the exact directive syntax that appears in the source file, making it easier to identify and fix the issue. If I write `:::note`, the error should reference `:::note`, not a different prefix/name combination.

### System Info
- Docusaurus version: latest
- MDX loader: @docusaurus/mdx-loader

---
Repository: /testbed
