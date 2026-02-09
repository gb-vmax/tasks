# Bug Report

### Describe the bug

I'm encountering an issue with import statements in MDX files. When using default imports, they seem to be parsed incorrectly and treated as named imports instead. This is causing problems with component imports in my MDX documents.

### Reproduction

```jsx
// In an MDX file
import MyComponent from './MyComponent'

// MyComponent is not recognized correctly
<MyComponent />
```

The default import `MyComponent` doesn't work as expected. It appears the parser is treating it as a named import rather than a default import, which breaks the component resolution.

### Expected behavior

Default imports should be parsed as `ImportDefaultSpecifier` nodes and work correctly in MDX files. The component should be accessible and render properly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently. Has there been any changes to how import specifiers are handled?

---
Repository: /testbed
