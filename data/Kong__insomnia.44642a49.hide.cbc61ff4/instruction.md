# Bug Report

### Describe the bug

The SelectModal component is not properly structured - there's an issue with the code formatting where `getInitialState` function definition appears to be placed incorrectly within the `useImperativeHandle` hook. This causes the modal to fail to render or function properly.

### Reproduction

```tsx
import { SelectModal } from './select-modal';

// Try to use the SelectModal component
const modalRef = useRef<SelectModalHandle>(null);

// Attempting to show the modal results in errors
modalRef.current?.show({
  title: 'Select an option',
  options: [{ name: 'Option 1', value: '1' }],
  value: null,
  message: 'Please choose',
});
```

### Expected behavior

The SelectModal should render correctly and the `hide()` and `show()` methods should work as expected. The component structure should be valid TypeScript/JSX.

### System Info
- Insomnia version: latest
- OS: Any

---
Repository: /testbed
