# Bug Report

### Describe the bug

The table of contents (TOC) tree structure is not updating when the `toc` prop changes. After navigating between pages or when the TOC items change, the component continues to display the old TOC structure instead of reflecting the new content.

### Reproduction

```jsx
function MyComponent() {
  const [toc, setToc] = useState([
    { id: 'heading-1', value: 'First Heading', level: 2 }
  ]);
  
  const treeifiedTOC = useTreeifiedTOC(toc);
  
  // Later, update the TOC
  setToc([
    { id: 'heading-2', value: 'Second Heading', level: 2 }
  ]);
  
  // treeifiedTOC still shows the old structure with 'First Heading'
  // instead of updating to 'Second Heading'
}
```

Steps to reproduce:
1. Render a component using `useTreeifiedTOC` hook
2. Change the `toc` array passed to the hook
3. Observe that the returned tree structure doesn't update

### Expected behavior

The `useTreeifiedTOC` hook should return an updated tree structure whenever the `toc` input changes. The memoization should properly track the `toc` dependency so that changes trigger a recalculation.

### System Info
- Docusaurus version: latest
- React version: 18.x

---
Repository: /testbed
