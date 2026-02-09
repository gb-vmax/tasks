# Bug Report

### Describe the bug

After a recent update, the prompt modal is behaving strangely. The code seems to have a syntax error or structural issue that's preventing the modal from working at all. When trying to open a prompt, nothing happens and the application may crash or throw errors.

### Reproduction

Try to use the PromptModal component in any scenario:

```js
// Attempt to show a prompt modal
promptModalRef.current?.show({
  title: 'Enter value',
  defaultValue: 'test',
  hints: ['option1', 'option2']
});
```

The modal doesn't appear and there might be console errors related to the component structure.

### Expected behavior

The prompt modal should open normally and display the input field with hints as it did before.

### Additional context

This seems to have started happening very recently. The modal was working fine in previous versions. Looking at the component code, there appears to be something wrong with how the `show` method is defined in the `useImperativeHandle` hook - the structure looks malformed.

---
Repository: /testbed
