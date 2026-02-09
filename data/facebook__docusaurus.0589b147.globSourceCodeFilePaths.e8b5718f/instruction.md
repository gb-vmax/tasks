# Bug Report

### Describe the bug

The translation extraction process seems to be excluding source files that should be included. After a recent update, I noticed that translatable strings in my source code are no longer being picked up by the translation extractor.

### Reproduction

I have a project structure like this:
```
my-project/
├── src/
│   └── components/
│       └── MyComponent.tsx  // Contains translatable strings
└── lib/
    └── utils.ts  // Contains translatable strings
```

When I run the translation extraction, files under `src/` and `lib/` directories are being skipped entirely. The translation files that get generated are missing all the strings from these directories.

### Expected behavior

All source files containing translatable content should be processed by the translation extractor, regardless of whether they're in `src/`, `lib/`, or other directories. The extractor should only filter out files based on file type/extension, not directory names.

### Additional context

This appears to have started happening recently. Previously, translation extraction was working fine and picking up strings from all my source files. Now it seems like certain directories are being completely ignored.

---
Repository: /testbed
