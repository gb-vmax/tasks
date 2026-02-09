# Bug Report

### Describe the bug
When showing a modal using `WrapperModal`, the component is throwing a syntax error and failing to render. The modal cannot be displayed at all.

### Reproduction
```jsx
const modalRef = useRef();

// Try to show the modal with options
modalRef.current?.show({
  title: 'Test Modal',
  body: <div>Modal content</div>,
  onShow: () => console.log('shown'),
  onHide: () => console.log('hidden')
});
```

The modal fails to show and the application crashes with a syntax error.

### Expected behavior
The modal should display properly with the provided title and body content, and the `onShow`/`onHide` callbacks should be invoked at the appropriate times.

### System Info
- Insomnia version: latest
- Platform: All platforms

This seems to have started happening recently. The modal was working fine before.

---
Repository: /testbed
