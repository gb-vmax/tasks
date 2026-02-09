# Bug Report

### Describe the bug

After a recent update, the PromptModal component is completely broken and won't render at all. The modal doesn't appear when trying to use it, and it seems like the component structure was corrupted somehow.

### Reproduction

Try to use the PromptModal component in any scenario where it's supposed to show up:

```js
// Attempting to show a prompt modal
const modalRef = useRef();

// Later in code...
modalRef.current?.show({
  title: 'Enter value',
  defaultValue: '',
  submitName: 'Submit',
  onComplete: (value) => console.log(value)
});
```

The modal simply doesn't appear and there are no errors in the console.

### Expected behavior

The PromptModal should display with the configured options and allow user input.

### Additional context

Looking at the component file, it appears that the interface definition for `PromptModalHandle` got corrupted or merged with the actual component implementation. The `show` and `hide` method signatures seem to have been replaced with what looks like component code in the wrong place.

This is blocking any workflow that requires user input prompts in the application.

---
Repository: /testbed
