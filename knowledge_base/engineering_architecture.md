# TaskFlow Engineering Architecture

TaskFlow uses:

- React for frontend development
- REST APIs for backend communication
- relational database storage
- existing authentication services
- reusable React component library

Important engineering limitations:

- authentication APIs should not be replaced during the current release cycle
- major database schema changes should be avoided
- new interfaces should use the existing React component library
- accessibility support is required
- existing user accounts must remain backwards compatible