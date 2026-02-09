# Bug Report

### Describe the bug

The screen reset functionality in the CLI is not displaying the heading on the first run. When the CLI starts up, the initial heading message is missing, but subsequent headings are displayed correctly.

### Reproduction

```js
const resetScreen = getResetScreen(configs, allowClearScreen, stderr);

// First call - heading is not displayed
resetScreen('Starting build...');

// Second call - heading IS displayed (but shouldn't be on first run)
resetScreen('Rebuilding...');
```

### Expected behavior

The heading should be displayed on the first run, and subsequent calls should not display the heading (assuming that's the intended behavior for screen reset).

### Additional context

This appears to affect the initial user feedback when starting the CLI tool. Users don't see the first status message which can be confusing about whether the tool has started properly.

---
Repository: /testbed
