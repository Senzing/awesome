# Contributing

Welcome to the project!

We encourage contribution in a manner consistent with the [Code of Conduct].
The following will guide you through the process.

There are a number of ways you can contribute:

1. [Asking questions]
1. [Requesting features]
1. [Reporting bugs]
1. [Contributing code or documentation]

## License Agreements

If your contribution modifies the Git repository, the following agreements must be established.

_Note:_ License agreements are only needed for adding, modifying, and deleting artifacts kept within the repository.
In simple terms, license agreements are needed before pull requests can be accepted.
A license agreement is not needed for submitting feature request, bug reporting, or other project management.

### Individual Contributor License Agreement

In order to contribute to this repository, an [Individual Contributor License Agreement (ICLA)] must be completed, submitted, and accepted.

### Corporate Contributor License Agreement

If the contribution to this repository is on behalf of a company, a [Corporate Contributor License Agreement (CCLA)] must also be completed, submitted, and accepted.

### Project License Agreement

The license agreement for this repository is stated in the [LICENSE] file.

## Questions

Please do not use the GitHub issue tracker to submit questions.

Instead, email <support@senzing.com>.
For open discussions, use GitHub's [Discussions].

## Feature Requests

All feature requests are "GitHub issues".
To request a feature, create a [GitHub issue] in this repository.

When creating an issue, there will be a choice to create a "Bug report" or a "Feature request".
Choose "Feature request".

## Bug Reporting

All bug reports are "GitHub issues".
Before reporting on a bug, check to see if it has [already been reported].
To report a bug, create a [GitHub issue] in this repository.

When creating an issue, there will be a choice to create a "Bug report" or a "Feature request".
Choose "Bug report".

## Contributing code or documentation

To contribute code or documentation to the repository, you must have [License Agreements] in place.
This needs to be complete before a [Pull Request] can be accepted.

### Setting up a development environment

#### Set Environment variables

These variables may be modified, but do not need to be modified.
The variables are used throughout the installation procedure.

```console
export GIT_ACCOUNT=senzing
export GIT_REPOSITORY=awesome
```

Synthesize environment variables.

```console
export GIT_ACCOUNT_DIR=~/${GIT_ACCOUNT}.git
export GIT_REPOSITORY_DIR="${GIT_ACCOUNT_DIR}/${GIT_REPOSITORY}"
export GIT_REPOSITORY_URL="git@github.com:${GIT_ACCOUNT}/${GIT_REPOSITORY}.git"
```

#### Clone repository

Get repository.

```console
mkdir --parents ${GIT_ACCOUNT_DIR}
cd  ${GIT_ACCOUNT_DIR}
git clone ${GIT_REPOSITORY_URL}
cd ${GIT_REPOSITORY_DIR}
```

### Coding conventions

### Testing

### Pull Requests

Code in the main branch is modified via GitHub pull request.
Follow GitHub's [Creating a pull request from a branch] or
[Creating a pull request from a fork] instructions.

Accepting pull requests will be at the discretion of Senzing, Inc. and the repository owner(s).

[already been reported]: https://github.com/search?q=+is%3Aissue+user%3Asenzing
[Asking questions]: #questions
[Code of Conduct]: CODE_OF_CONDUCT.md
[Contributing code or documentation]: #contributing-code-or-documentation
[Corporate Contributor License Agreement (CCLA)]: .github/senzing-corporate-contributor-license-agreement.pdf
[Creating a pull request from a branch]: https://help.github.com/articles/creating-a-pull-request/
[Creating a pull request from a fork]: https://help.github.com/articles/creating-a-pull-request-from-a-fork/
[Discussions]: https://github.com/senzing-garage/awesome/discussions
[GitHub issue]: https://help.github.com/articles/creating-an-issue/
[Individual Contributor License Agreement (ICLA)]: .github/senzing-individual-contributor-license-agreement.pdf
[License Agreements]: #license-agreements
[LICENSE]: LICENSE
[Pull Request]: #pull-requests
[Reporting bugs]: #bug-reporting
[Requesting features]: #feature-requests
