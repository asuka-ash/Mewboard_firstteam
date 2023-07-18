# # Important Instructions

This is the main repository for our project. It contains the source code, documentation, and auxiliary files necessary for the development and deployment of our project. 

## Table of Contents

- [# Important Instructions](#-important-instructions)
  - [Table of Contents](#table-of-contents)
  - [Project Setup](#project-setup)
  - [Contribution Guide](#contribution-guide)
  - [Coding Standards](#coding-standards)
  - [Testing](#testing)
  - [Branch Naming Conventions](#branch-naming-conventions)
  - [Pull Requests](#pull-requests)

## Project Setup

While contributing, keep in mind that we will build the project as a set of microservices which can be resused across multiple tools (EPP, Cloud Security etc.)

## Contribution Guide

We encourage all team members to contribute to the development of this project. However, in order to maintain a consistent codebase, we have established the following rules for contributing:

1. **Create a new branch for each feature.** No work should be done in the `main` branch. Always create a new branch for your work.
2. **Use clear and concise commit messages.** This helps others understand the changes you've made.
3. **Document your code.** Include comments in your code to make it easier for others to understand.
4. **Test your code before committing.** All tests must pass before code can be merged into the `main` branch.

## Coding Standards

- Code Formatting: Use consistent indentation and spacing in your code. Use spaces or tabs, but not both. The code should be neatly formatted and easy to read.

- Naming Conventions: Variables, functions, classes, modules, etc. should have clear, descriptive names. For this project we will be using using camelCase. Avoid using abbreviations or single letter variables (except for common cases like i in a loop).

- Comments: Write meaningful comments for complex sections of code. It's also good to include comments for public methods and functions describing what they do, parameters they take, and what they return.

- Error Handling: Errors and exceptions should be properly handled. Do not leave empty catch blocks.
  
- Code Structure: Organize your code into logically related blocks. Functions and methods should ideally do one thing and be reasonably short. Classes should adhere to the Single Responsibility Principle (SRP).

## Testing

Before committing, always run the project's tests. This helps ensure that your changes don't break existing functionality. Also, write tests for new features you add. The more tests, the better!

## Branch Naming Conventions

When creating a new branch, name it meaningfully, based on the feature or fix you're working on. The following structure is recommended:

- For feature: `feature/feature-name`
- For bug fixes: `fix/bug-name`

## Pull Requests

Once you have committed your changes in your branch, you can open a pull request. The pull request should be clear about what changes have been made and why. It should reference any related issues.

Please ensure the following before submitting a pull request:

1. Your code complies with the coding standards.
2. Your code is well-documented.
3. All tests are passing.
4. There are no merge conflicts.

Once a pull request is opened, other team members should review the code and provide feedback. Once the code has been approved, it can be merged into the `main` branch.

