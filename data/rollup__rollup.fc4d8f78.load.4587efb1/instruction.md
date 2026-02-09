# Bug Report

### Describe the bug

After a recent update, I'm noticing that region comments in help.md files are not being properly removed from the CLI help output. The comments like `// #region` and `// #endregion` are appearing in the final help text when they should be stripped out.

### Reproduction

1. Create a help.md file with region comments:
```md
Some help text
// #region example
Hidden content
// #endregion
More help text
```

2. Build the project and check the CLI help output
3. The region comment lines are still present in the output

### Expected behavior

All lines containing `// #region` and `// #endregion` comments should be completely removed from the help text, including the newline characters. The final output should only show:
```
Some help text
Hidden content
More help text
```

### Additional context

This seems to have broken recently. The help output now includes these internal comment markers which makes the CLI help look messy and confusing to end users.

---
Repository: /testbed
