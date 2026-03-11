Hey, I need some quick help with version tracking for my ML experiment pipeline. I have a model artifact registry that uses semantic versioning, and I just fixed a bug in the preprocessing step that was causing NaN values to slip through during feature normalization.

Here's the situation: my current project lives at `/home/user/mlops/artifact_registry`. Inside it there's a file called `VERSION` that contains the current version string, and a `CHANGELOG.md` that tracks the history of changes.

I need you to do two things:

1. **Bump the patch version** in `/home/user/mlops/artifact_registry/VERSION`. Read the current version from that file, increment the patch number by 1 (the third number in the `MAJOR.MINOR.PATCH` format), and overwrite the file with the new version string. The file should contain exactly the new version string followed by a newline, and nothing else.

2. **Prepend a new changelog entry** to `/home/user/mlops/artifact_registry/CHANGELOG.md`. The new entry must be added at the very top of the file (before all existing content) and must follow this exact format:

```
## [<new_version>] - 2024-11-15

### Fixed
- Preprocessing pipeline: reject NaN values during feature normalization step

```

Where `<new_version>` is the bumped version string you wrote to the VERSION file (e.g., if the new version is `1.4.8`, then the header reads `## [1.4.8] - 2024-11-15`). Note there must be a blank line after the bullet point before the existing changelog content begins.

The final CHANGELOG.md should have the new entry at the top, followed immediately by whatever was already in the file.
