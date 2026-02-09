# Bug Report

### Describe the bug

The `useDocumentTitle` hook is not updating the document title when the title prop changes. After the initial mount, changing the title value has no effect on the actual document title.

### Reproduction

```jsx
function MyComponent() {
  const [title, setTitle] = useState('Initial Title');
  
  useDocumentTitle(title);
  
  // Clicking this button doesn't update the document title
  return (
    <button onClick={() => setTitle('Updated Title')}>
      Change Title
    </button>
  );
}
```

### Expected behavior

When the `title` parameter passed to `useDocumentTitle` changes, the document title should update accordingly. The hook should be reactive to changes in the title prop.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
