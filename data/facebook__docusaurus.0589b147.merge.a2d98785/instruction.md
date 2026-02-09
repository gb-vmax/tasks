# Bug Report

### Describe the bug

I'm experiencing an issue where HTML attribute names are being incorrectly mapped when processing MDX content. It seems like property names and their normalized versions are getting swapped, causing attributes to be set with the wrong values or not recognized properly.

### Reproduction

When using MDX with HTML attributes that have special naming conventions (like `className` vs `class`, or `htmlFor` vs `for`), the attributes are not being processed correctly. For example:

```jsx
// In MDX file
<div className="test" aria-label="example">
  <label htmlFor="input-id">Label</label>
</div>
```

The resulting output has the property mappings reversed - normalized names appear where property names should be, and vice versa. This causes the attributes to either not work or be applied incorrectly in the rendered output.

### Expected behavior

HTML attributes should be correctly mapped between their property names (e.g., `className`, `htmlFor`) and their normalized/standard names (e.g., `class`, `for`). The schema should maintain the proper relationship between these two naming conventions.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
