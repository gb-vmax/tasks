# Bug Report

### Describe the bug

I'm experiencing an issue where JSX elements are not being properly transformed in MDX files. The transformation seems to stop midway through processing, resulting in incomplete or malformed output.

### Reproduction

When processing MDX content with JSX elements, the transformation appears to be incomplete. This affects any MDX file that contains JSX syntax, including fragments and nested elements.

```mdx
<div>
  <Fragment>
    <p>Some text</p>
  </Fragment>
</div>
```

The above MDX content doesn't get properly transformed to the expected runtime JSX calls.

### Expected behavior

JSX elements and fragments in MDX files should be fully transformed to their runtime equivalents (jsx, jsxs, jsxDEV, Fragment imports) based on the configuration. The entire AST should be processed correctly without truncation.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have broken recently - the JSX transformation logic appears to be cutting off prematurely during the leave phase of the tree traversal.

---
Repository: /testbed
