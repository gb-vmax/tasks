# Bug Report

### Describe the bug

The "Clear" action in the prompt template tag is completely broken. When trying to clear stored prompt values, nothing happens and the function appears to be malformed or incomplete.

### Reproduction

1. Use a prompt template tag in a request
2. Store some values by entering responses to prompts
3. Try to use the "Clear" action from the prompt actions menu
4. The clear operation fails to execute properly

### Expected behavior

The Clear action should:
- Show a confirmation dialog before clearing
- Successfully remove stored prompt values
- Complete the operation without errors

Currently it seems like the code is cut off or corrupted - the function definition doesn't look right and the implementation appears incomplete.

### System Info
- Insomnia version: latest
- OS: N/A

This is blocking our ability to clear old prompt values during testing. The previous version worked fine with a simple `context.store.clear()` call.

---
Repository: /testbed
