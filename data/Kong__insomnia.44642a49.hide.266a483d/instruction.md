# Bug Report

### Describe the bug

The SelectModal component appears to have duplicate code and malformed structure. When trying to use the modal, it's not behaving as expected - the hide/show methods seem to be defined multiple times and there's interface/hook declarations appearing in the wrong place within the component.

### Reproduction

```tsx
// Try to use SelectModal in a component
const modalRef = useRef<SelectModalHandle>(null);

// Call show method
modalRef.current?.show({
  title: 'Select Option',
  message: 'Please choose',
  options: [
    { name: 'Option 1', value: '1' },
    { name: 'Option 2', value: '2' }
  ],
  value: null,
  onDone: (value) => console.log('Selected:', value),
  onCancel: () => console.log('Cancelled')
});

// Modal doesn't render properly or throws errors
```

### Expected behavior

The SelectModal should render correctly and the show/hide methods should work as intended. The component structure should be valid TypeScript/React code without duplicate method definitions or misplaced interface declarations.

### System Info
- Insomnia version: latest
- Platform: All

The code structure looks corrupted - there's interface definitions, useImperativeHandle hooks, and JSX button elements appearing in the middle of the useImperativeHandle callback, followed by duplicate hide/show method definitions. This breaks the component entirely.

---
Repository: /testbed
