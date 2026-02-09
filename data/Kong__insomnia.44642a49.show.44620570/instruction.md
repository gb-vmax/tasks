# Bug Report

### Describe the bug

The `WrapperModal` component's `show` method seems to have a syntax/formatting issue that's breaking the modal functionality. When trying to open a modal using the `show` method, the modal fails to display properly.

### Reproduction

```tsx
const modalRef = useRef<WrapperModalHandle>(null);

// Try to show the modal
modalRef.current?.show({
  title: 'Test Modal',
  body: <div>Modal content</div>
});
```

The modal doesn't appear when calling the `show` method. Looking at the code, there appears to be an indentation/structure problem in the `WrapperModal` component where the `mergeWithDefaults` function is defined in an invalid location within the `useImperativeHandle` hook.

### Expected behavior

The modal should display normally when the `show` method is called with valid options.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
