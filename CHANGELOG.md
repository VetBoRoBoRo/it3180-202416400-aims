# Changelog

All notable changes are documented here. Versions follow Semantic Versioning.

## [Unreleased]

## [1.1.0] - 2026-11-07
### Added
- Category search (case-insensitive exact category).
- Cart sorting by title and cost.

## [1.0.1] - 2026-11-07
### Fixed
- Title search now ignores letter case (#17).

## [1.0.0] - 2026-11-07
### Added
- DVD model, cart add/remove/total, print_cart and title search.
- Validated percentage discounts and use-case documentation.
- Regression tests, PR template and protected development branch.
### Fixed
- Reject the 21st DVD in cart (#6).
- Return the remaining total after discount; validate 0..100 percent.
