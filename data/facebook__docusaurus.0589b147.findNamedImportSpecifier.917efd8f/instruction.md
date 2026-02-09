# Bug Report

### Describe the bug

When importing a component with a default export in MDX files, the table of contents (TOC) generation fails to correctly identify the import. The code is trying to match against `ImportDefaultSpecifier` but then incorrectly accesses the `imported` property which doesn't exist on default imports.

### Reproduction

```mdx
import MyComponent from './MyComponent';

# Heading 1

<MyComponent />

## Heading 2
```

When the MDX loader processes this file, it fails to properly handle the default import statement. The issue occurs because default imports have a different AST structure than named imports - they use `ImportDefaultSpecifier` which only has a `local` property, not an `imported` property.

### Expected behavior

The TOC should be generated correctly regardless of whether components are imported using default or named imports. Both of these should work:

```js
// Default import
import MyComponent from './MyComponent';

// Named import  
import { MyComponent } from './MyComponent';
```

### Additional context

This appears to affect MDX files that use default imports for components. The import detection logic seems to be mixing up the handling of different import specifier types.

---
Repository: /testbed
