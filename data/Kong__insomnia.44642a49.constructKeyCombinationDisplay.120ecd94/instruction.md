# Bug Report

### Describe the bug

I'm encountering a syntax error in the hotkeys module after a recent update. The application fails to start and throws an error related to the `constructKeyCombinationDisplay` function.

### Reproduction

When trying to use any keyboard shortcut functionality, the app crashes immediately. Looking at the code, it seems like there's duplicate code in the `constructKeyCombinationDisplay` function - the logic for adding modifier keys and constructing the display appears twice, which causes a syntax error.

Steps to reproduce:
1. Start the application
2. Try to use any keyboard shortcut
3. Application fails to load/crashes

### Expected behavior

Keyboard shortcuts should work normally and the `constructKeyCombinationDisplay` function should properly format the key combination display without syntax errors.

### System Info
- Insomnia version: latest
- OS: macOS/Windows/Linux (affects all platforms)

The issue appears to be in `packages/insomnia/src/common/hotkeys.ts` where there's malformed code structure causing the entire module to fail parsing.

---
Repository: /testbed
