# Bug Report

### Describe the bug

When checking for the absence of modals using the test helper, it's incorrectly reporting that modals are present when they should not be. The `expectNoModal` function seems to be broken and always expects to find a modal instead of verifying that no modal exists.

### Reproduction

```js
import { expectNoModal } from '@mantine-tests/dates';

// After closing a modal or when no modal should be visible
const container = document.body;
expectNoModal(container);

// This fails even though no modal is actually visible
// The test expects 1 modal to be present instead of 0
```

### Expected behavior

The `expectNoModal` helper should verify that there are no modals present in the container. When no modals exist, the assertion should pass. Currently it's doing the opposite - it expects to find 1 modal when it should expect 0.

### Additional context

This affects all tests that verify modal dismissal or initial states where no modal should be open. The logic appears to be inverted - filtering elements without a className and then expecting length of 1 doesn't make sense for checking modal absence.

---
Repository: /testbed
