# Bug Report

### Describe the bug

The table of contents (TOC) tree is always empty regardless of the actual TOC items passed to `useTreeifiedTOC`. It seems like the hook is not processing the input TOC array correctly.

### Reproduction

```jsx
import { useTreeifiedTOC } from '@docusaurus/theme-common';

const tocItems = [
  { id: 'heading-1', value: 'Heading 1', level: 2 },
  { id: 'heading-2', value: 'Heading 2', level: 3 },
  { id: 'heading-3', value: 'Heading 3', level: 2 },
];

function MyComponent() {
  const tree = useTreeifiedTOC(tocItems);
  
  console.log(tree); // Expected: tree structure with 3 items
                     // Actual: empty array []
  
  return <div>{/* TOC rendering */}</div>;
}
```

### Expected behavior

The `useTreeifiedTOC` hook should return a treeified structure based on the provided TOC items. When passing an array of TOC items with different heading levels, it should build a hierarchical tree structure that can be used for rendering nested navigation.

### System Info

- Docusaurus version: latest
- Node version: 18.x

The TOC sidebar is completely empty in my documentation site even though the markdown files have proper headings. This makes navigation very difficult for users.

---
Repository: /testbed
