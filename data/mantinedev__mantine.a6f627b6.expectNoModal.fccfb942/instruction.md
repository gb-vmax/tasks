# Bug Report

### Describe the bug

The `expectNoModal` helper function is not working as expected. When checking that a modal is not present, the function is actually checking for the presence of a modal root element instead of verifying its absence.

### Reproduction

```js
import { expectNoModal } from '@mantine-tests/dates';

// After closing a modal or when no modal should be visible
const container = document.body;
expectNoModal(container);

// The check passes even when a modal is actually present
```

### Expected behavior

The `expectNoModal` helper should verify that no modal is displayed on the page. Currently, it appears to be checking for the presence of a modal root element rather than confirming the modal is absent, which is the opposite of what the function name suggests.

### System Info
- @mantine/dates version: latest
- Testing environment: jsdom

---
Repository: /testbed
