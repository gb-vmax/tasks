# Bug Report

### Describe the bug

After a recent update, the "Clear" action in the prompt template tag is not working as expected. When I try to clear stored prompt values, the action seems to complete but the values remain in storage and continue to appear as defaults when I open the prompt again.

### Reproduction

1. Create a request with a prompt template tag
2. Enter a value in the prompt and save it
3. Click the "Clear" action button
4. Close and reopen the prompt

**Expected:** The prompt should be empty or show the default value
**Actual:** The previously saved value still appears

### Additional context

This was working fine before - the Clear button would remove all stored prompt values. Now it seems like the clear operation isn't actually removing the items from storage, even though the console shows the action is being triggered.

I'm using the prompt tag with `saveLastValue` enabled, if that matters. The issue happens consistently across different requests and workspaces.

---
Repository: /testbed
