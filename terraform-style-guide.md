# Terraform Style Guide

Our Terraform style is very modern, it uses YAML as the basis for configuration and by default should create zero material resources when adding it to your workspace. You should opt-in using YAML to every resource you want created.

## General

- Naming: All resource names, file names, module names, etc., should have clear, descriptive, unambiguous names
  - Names should be lowercase, alphanumeric, with hyphens or underscores
  - Hyphenation should be consistent with nearby existing patterns; e.g., hyphens in file paths, and underscores in resource names
  - Avoid uncommon acronyms/don't be cryptic
  - Avoid shortening names (e.g. repo vs repository), opt for clarity over brevity

## YAML

- Design YAML data structures first, then write Terraform
- Reference existing projects for structure and style before writing ANY YAML!
- YAML that should be user-facing must be in the directory above the terraform
  - This has different codeowners than the terraform
- All YAML has templates and readmes

## Terraform

- Reference existing projects for structure and style before writing ANY Terraform!
- All variables and resources should have excessively descriptive names, nothing cryptic
  - Use names and hyphenation consistently (hyphens over underscores)
  - Try not to shorten names (e.g. repo vs repository), opt for clarity over brevity
- Reuse/reference as many YAML files as possible - keep it DRY
- Don't embed constants throughout your code--put constants in YAML
- Try to only have main.tf, terraform.tf, and validation.tf; add files only as absolutely necessary
- main.tf should be composed of singleton resources driven by YAML
  - These singletons should be named 'this' and all use for_each to iterate
- Use as few input/output variables as absolutely necessary (ideally zero)
- Add assertions to validate YAML references or enums
  - Add assertions every time a user hits a confusing error because of bad input

## Modules

- Don't create modules for encapsulation unless it simplifies code significantly or must be shared
  - They're not DRY, harder to maintain, and you have to duplicate every input through variables
- Put as few resources in these as necessary--don't over-specialize the module for a single use-case
- Don't put embed custom resources for a particular environment in a common module; those resources should be requested/specified by the environment that needs it via YAML
- Don't rename variables as much as possible
- Keep modules in this project and only put them in the module registry
- When symlinking in a module, it should not create _any_ resources by default, and should only create resources that are requested by YAML configurations.
- Changes to common modules should not have ANY material effect in existing environments–they should always be backwards-compatible and only add support that can be opted-into by e.g., adding YAML configuration.

## Miscellaneous

- Add comments liberally. Explain yourself. Don't be clever without documentation.
  - Give every resource a comment explaining what it's for
- Add newlines and comments to separate logical groupings of keys -- make it easy to read
- Set up CODEOWNERS thoughtfully for each new project, follow existing patterns
- Set prevent_destroy=true on resources that cannot be recovered if accidentally deleted
  - E.g. repositories, databases, etc.
  - You don't need to set it on anything that can be rebuilt from a revert of code, e.g. permissions
- Use depends_on explicitly wherever possible to clearly identify relationships and ordering
  - When driving everything from YAML you lose some of the implicit relationships/dependencies
    that Terraform is good at finding. You can sometimes drive one resource from another,
    but this isn't always the case in a YAML-driven workflow.
- Use `try` over `lookup`, and always have a default case at the end
  - It is more general and easier to read
  - It saves you from multiple lookups if multiple nested values may be null
  - It accomplishes the same effect of lookup without separating the map from the key
    (e.g. try(local.map.key, "not-found") vs lookup(local.map, "key", "not-found") )
  - However if planning performance is really bad, switching `try` back to `lookup`
    in tight loops may improve it
- Do all YAML pre-processing in local values rather than inline inside of resources
  - E.g. If you'll automatically replace a user value with a looked-up value or apply defaults
- Don't commit commented-out code unless you leave a comment why or what it's for.
