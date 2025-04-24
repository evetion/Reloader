# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]


## [0.2.1] - 2025-04-24
### Added

- Watching group layers is now supported
- Added tests
- Added pixi tasks for a better development experience

## [0.2.0] - 2025-02-19

### Added
- Support added for file names that are URL-encoded (including those with options appended)
- Support added for all file path encoding used by QGIS on all platforms

### Changed
- All valid selected layers will be watched even if selection includes unwatchable ones

### Fixed

- Watching multiple files/layers is now working properly
- Files changed with non-in-place updates (write to temporary file + move) are now persistently watched 

## [0.1.0] - 2015-10-06

### Added

- Initial release

[unreleased]: https://github.com/evetion/reloader/compare/v0.2.1...HEAD
[0.2.1]: https://github.com/evetion/reloader/compare/v0.2.1...v0.2.0
[0.2.0]: https://github.com/evetion/reloader/compare/v0.2.0...v0.1.0
[0.1.0]: https://github.com/evetion/reloader/releases/tag/v0.1.0
