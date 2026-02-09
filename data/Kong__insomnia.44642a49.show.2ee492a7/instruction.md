# Bug Report

### Describe the bug

I'm getting a TypeScript compilation error when trying to use the `PromptModal` component. The error says that `show` and `hide` are not valid properties on the `PromptModalHandle` interface.

### Reproduction

```tsx
const promptModalRef = useRef<PromptModalHandle>(null);

// Later in the code:
promptModalRef.current?.show({
  title: 'Enter name',
  defaultValue: '',
  onComplete: (value) => console.log(value)
});

// This also fails:
promptModalRef.current?.hide();
```

### Expected behavior

The `show()` and `hide()` methods should be callable on the ref without TypeScript errors. These methods were working fine in previous versions.

### System Info
- TypeScript version: 4.x+
- Component: `PromptModal` in `ui/components/modals/prompt-modal.tsx`

The interface definition seems to have incorrect syntax - looks like function implementations instead of method signatures.

---
Repository: /testbed
