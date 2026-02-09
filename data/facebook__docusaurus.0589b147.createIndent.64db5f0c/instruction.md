# Bug Report

### Describe the bug

I'm experiencing incorrect indentation behavior when working with MDX content. The indentation level appears to be off by one, causing nested elements to not align properly with their expected depth.

### Reproduction

When processing MDX with nested structures, the indentation doesn't match the nesting level:

```js
// With depth = 2, expecting 2 levels of indentation
// But getting only 1 level of indentation instead

// Example MDX structure:
<div>
  <Component>
    <NestedComponent />
  </Component>
</div>

// The nested components are rendering with incorrect indentation
```

### Expected behavior

The indentation should match the actual nesting depth. If an element is at depth 2, it should have 2 levels of indentation, not 1.

### Additional context

This seems to affect the rendering/formatting of MDX content when elements are nested. The visual structure doesn't match the logical nesting level, making the output harder to read.

---
Repository: /testbed
