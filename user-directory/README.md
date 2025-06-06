# User Directory Application

A responsive, modern user directory app built with React + TypeScript. It fetches user data from the JSONPlaceholder API and provides a professional UI for browsing, viewing, and managing users.

## Features
- Table-like user list with columns for name/email, address, phone, website, and company
- Click a user to view full details in a modal (with map link)
- Delete users from the list (client-side only)
- Responsive, clean design with CSS Modules
- Visual feedback and modal animations
- Fully typed with TypeScript
- Unit and integration tests with React Testing Library + Jest

## Stack
- React 18 + TypeScript
- CSS Modules
- Jest + React Testing Library
- JSONPlaceholder API

## Project Rules
- Use functional components and hooks
- Use CSS Modules for all component styles
- All user data types must be defined in `src/types.ts`
- All API calls must be typed
- All user actions (view, delete) must provide visual feedback
- Modal must be accessible and close on overlay or button click
- Responsive for mobile and desktop

## Test Rules
- All components must have unit tests
- User interactions (open modal, delete) must have integration tests
- Test coverage must be >90%

## Getting Started
```bash
npm install
npm start
```

## Running Tests
```bash
npm test
```

## Documentation Rules
- All components and utilities must be documented with JSDoc
- README must describe features, stack, rules, and test instructions

---

This project was generated and implemented according to [Cursor rules](https://cursor.directory/rules) and best practices for codegen-friendly, maintainable apps.
