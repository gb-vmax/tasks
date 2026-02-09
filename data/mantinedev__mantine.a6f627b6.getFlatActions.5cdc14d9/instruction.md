# Bug Report

### Describe the bug

When using spotlight with grouped actions, only the first action from each group is being displayed/processed. All other actions in the group are missing from the results.

### Reproduction

```js
const actions = [
  {
    group: 'Navigation',
    actions: [
      { id: 'home', label: 'Home' },
      { id: 'about', label: 'About' },
      { id: 'contact', label: 'Contact' }
    ]
  }
];

// Only 'Home' action appears, 'About' and 'Contact' are missing
```

### Expected behavior

All actions within a group should be flattened and available in the spotlight, not just the first one. In the example above, all three actions (Home, About, Contact) should be accessible.

### System Info
- @mantine/spotlight version: latest
- React version: 18.x

---
Repository: /testbed
