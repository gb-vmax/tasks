# Bug Report

### Describe the bug

The `useDocumentTitle` hook is causing unnecessary re-renders when the title string has leading or trailing whitespace. Even though the actual document title remains the same (trimmed version), the effect keeps re-running.

### Reproduction

```jsx
const [title, setTitle] = useState('My Title   ');

useDocumentTitle(title);

// Later in the code
setTitle('My Title  '); // Different whitespace, but same trimmed result

// The effect re-runs even though document.title would be set to the same value
```

Another example:
```jsx
// This will cause the effect to run on every render if title comes from props
// with varying whitespace
useDocumentTitle(props.pageTitle); // e.g., "Home  " vs "Home   "
```

### Expected behavior

The hook should only trigger re-renders when the *trimmed* title actually changes. If I pass `"My Title   "` and then later `"My Title  "`, the effect shouldn't re-run since both trim to `"My Title"`.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
