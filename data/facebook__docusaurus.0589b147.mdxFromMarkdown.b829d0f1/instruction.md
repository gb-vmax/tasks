# Bug Report

### Describe the bug

After a recent update, JSX elements in MDX files are no longer being parsed correctly. The JSX syntax is being treated as plain text instead of being converted to proper JSX components.

### Reproduction

Create an MDX file with JSX components:

```mdx
# Hello World

<CustomComponent prop="value">
  Content here
</CustomComponent>

<div className="wrapper">
  <p>Some text</p>
</div>
```

When processing this MDX file, the JSX elements are not being recognized and remain as raw text in the output instead of being transformed into proper component calls.

### Expected behavior

JSX elements should be properly parsed and transformed. The `<CustomComponent>` and `<div>` tags should be converted to their JSX equivalents in the compiled output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
