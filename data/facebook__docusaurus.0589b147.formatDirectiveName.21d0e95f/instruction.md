# Bug Report

### Describe the bug

I'm encountering an issue with MDX directive error messages. When an unsupported or unused directive is detected in my MDX files, the error message shows the directive type instead of the actual directive name that was used in the file.

### Reproduction

Create an MDX file with an unsupported directive, for example:

```mdx
:::unknownDirective
Some content here
:::
```

When this is processed, the error message will display something like:
```
Directive ':::containerDirective' is not supported
```

Instead of showing the actual directive name I used (`unknownDirective`), it's showing the generic directive type.

### Expected behavior

The error message should display the actual directive name that was used in the source file, making it easier to locate and fix the issue. For the example above, it should show:
```
Directive ':::unknownDirective' is not supported
```

This makes debugging much harder because I can't easily identify which specific directive in my MDX file is causing the problem.

### System Info
- Docusaurus version: latest
- MDX loader: @docusaurus/mdx-loader

---
Repository: /testbed
