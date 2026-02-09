# Bug Report

### Describe the bug

When using Spotlight with grouped actions, the actions are not being displayed correctly. It seems like the filtering/flattening logic is broken and actions are missing from the results.

### Reproduction

```js
const actions = [
  {
    group: 'Navigation',
    actions: [
      { id: 'home', label: 'Home' },
      { id: 'settings', label: 'Settings' }
    ]
  },
  {
    id: 'logout',
    label: 'Logout'
  }
];

// When spotlight processes these actions, 
// the grouped actions don't appear in the final list
```

### Expected behavior

All actions should be flattened and available in the spotlight search, including both grouped actions and standalone actions. The current behavior seems to be dropping actions or not processing them correctly.

### System Info
- @mantine/spotlight version: latest
- React version: 18.x

---
Repository: /testbed
