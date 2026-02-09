# Bug Report

### Describe the bug

The `expectNoModal` helper function is checking for the wrong condition. When verifying that no modal is present, it's currently checking if there is exactly 1 modal overlay element, but it should be checking that there are 0 modal elements.

### Reproduction

```tsx
import { expectNoModal } from '@mantine-tests/dates';

// Scenario: After closing a modal, verify it's no longer present
const container = document.createElement('div');
// Modal is closed, no modal elements should exist

expectNoModal(container);
// This will fail because it expects 1 overlay element instead of 0
```

### Expected behavior

When no modal is displayed, `expectNoModal` should verify that modal elements are not present in the DOM (count should be 0), not that exactly 1 overlay exists.

The function should pass when:
- The modal is closed
- No modal elements exist in the container

Currently it's doing the opposite check which doesn't make sense for a function named `expectNoModal`.

### System Info
- Package: @mantine-tests/dates
- Related helper: date-input-test-helpers.ts

---
Repository: /testbed
