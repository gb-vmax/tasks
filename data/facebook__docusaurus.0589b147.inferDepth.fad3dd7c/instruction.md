# Bug Report

### Describe the bug

I'm encountering an issue with JSX element depth calculation in MDX files. It appears that nested JSX elements are not being properly counted, which leads to incorrect indentation or depth tracking when rendering MDX content.

### Reproduction

```jsx
<div>
  <section>
    <article>
      <p>Content here</p>
    </article>
  </section>
</div>
```

When processing the above MDX structure, the depth calculation seems off. The nesting level doesn't match what I'd expect - it's like the depth counter is working in reverse or starting from the wrong initial value.

### Expected behavior

The depth should correctly reflect the nesting level of JSX elements, with the outermost element at depth 0 (or 1) and each nested child incrementing the depth accordingly. Currently, it seems like non-JSX elements are being counted instead of JSX elements, or the traversal order is reversed.

### System Info
- MDX version: 3.0.0
- Using remark-mdx parser

This is affecting how my MDX content is being serialized/processed. Any help would be appreciated!

---
Repository: /testbed
