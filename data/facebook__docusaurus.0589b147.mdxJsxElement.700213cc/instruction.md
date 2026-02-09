# Bug Report

### Describe the bug

I'm experiencing an issue with JSX elements when using nested SVG tags in MDX. It seems like the schema state is not being restored correctly after processing SVG elements, which causes problems when SVG tags are nested or when other elements follow SVG elements.

### Reproduction

```jsx
<div>
  <svg>
    <circle cx="50" cy="50" r="40" />
  </svg>
  <p>Some text after SVG</p>
</div>
```

Or with nested SVG:

```jsx
<svg>
  <svg>
    <rect width="100" height="100" />
  </svg>
</svg>
```

### Expected behavior

The schema should be properly managed when entering and exiting SVG contexts. Elements that come after SVG elements should be processed with the correct (HTML) schema, and nested SVG elements should handle schema switching correctly.

Currently, it appears that the schema state gets stuck in SVG mode or doesn't switch back to the parent schema at the right time, causing subsequent elements to be processed incorrectly.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
