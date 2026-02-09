# Bug Report

### Describe the bug

The `expectOpenedModal` helper function is not correctly checking if a modal is open. It seems to be checking for the wrong element or using an incorrect assertion, which causes tests to pass when they shouldn't or fail when the modal is actually open.

### Reproduction

```js
import { expectOpenedModal } from '@mantine-tests/dates';

// Open a modal in your test
openModal();

// This check doesn't work as expected
expectOpenedModal(container);
```

When I call `expectOpenedModal` after opening a modal, the assertion doesn't behave correctly. The modal is clearly visible on screen but the helper function doesn't properly verify its presence.

### Expected behavior

The `expectOpenedModal` function should correctly verify that a modal is open and visible in the DOM. It should check for the appropriate modal elements and use the right assertions.

### System Info
- @mantine/dates version: latest
- Testing library: @testing-library/react

---
Repository: /testbed
