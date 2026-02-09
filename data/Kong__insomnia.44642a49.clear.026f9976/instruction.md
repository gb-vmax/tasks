# Bug Report

### Describe the bug

The plugin API's clipboard `clear()` method is now storing backup data internally, which is causing unexpected behavior when multiple plugins try to clear the clipboard. The method is attempting to read the current clipboard content before clearing it, but this fails silently in certain contexts (like when clipboard permissions aren't granted or in headless environments).

### Reproduction

```js
// In a plugin context
const { app } = context;

// This now tries to read clipboard before clearing
app.clipboard.clear();

// Expected: clipboard is cleared
// Actual: clipboard might not be cleared if readText() throws an error
```

The issue occurs because:
1. The `clear()` method now calls `window.clipboard.readText()` before clearing
2. If `readText()` fails (permissions, context, etc.), the error is caught but the clear operation still proceeds
3. The backup data is stored in internal properties that persist across calls

### Expected behavior

The `clear()` method should simply clear the clipboard without side effects or attempting to read its contents first. Plugin clipboard operations should be straightforward and not depend on read permissions when only clearing is needed.

### Additional context

This seems to have been introduced recently. The method is also adding internal state (`_lastClearedContent`, `_lastClearedTimestamp`) and a restore function that weren't part of the original API surface. This makes the clipboard API stateful when it should be stateless.

---
Repository: /testbed
