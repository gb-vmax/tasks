# Bug Report

### Describe the bug

I'm encountering an issue with `useMergedRef` where passing function refs to components causes them to not work properly. The ref callback doesn't get called when it should be.

### Reproduction

```jsx
const MyComponent = () => {
  const handleRef = (node) => {
    console.log('Ref callback called', node);
    // This doesn't get called anymore
  };

  return <div ref={handleRef}>Content</div>;
};
```

When using `useMergedRef` with a callback ref:

```jsx
const MyComponent = () => {
  const callbackRef = (node) => {
    console.log('This should be called', node);
  };
  
  const anotherRef = useRef(null);
  const mergedRef = useMergedRef(callbackRef, anotherRef);

  return <div ref={mergedRef}>Content</div>;
};
```

The callback function never gets invoked. This used to work in previous versions but seems to have broken recently.

### Expected behavior

Function refs (callback refs) should be called with the DOM node when the element is mounted/unmounted. The `useMergedRef` hook should properly detect and handle function refs.

### System Info

- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
