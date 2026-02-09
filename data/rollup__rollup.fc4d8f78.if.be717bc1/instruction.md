# Bug Report

### Describe the bug

The screen reset functionality in watch mode is not displaying the initial heading on the first run. The heading only appears on subsequent runs, which makes the initial output incomplete and confusing.

### Reproduction

```js
import { getResetScreen } from './cli/run/resetScreen';

const resetScreen = getResetScreen(/* config */, false);

// Call on first run
resetScreen('Building bundle...');
// Expected: Should print 'Building bundle...'
// Actual: Nothing is printed

// Call on second run  
resetScreen('Rebuilding...');
// Now it prints 'Rebuilding...'
```

### Expected behavior

The heading should be displayed on the first run. Currently it's being skipped and only shows up starting from the second call onwards.

### System Info

- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
