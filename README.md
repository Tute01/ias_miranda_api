# API REST de Gestión de Clientes

Desarrollo de una API REST utilizando Flask, SQLAlchemy y PostgreSQL para la gestión de clientes, implementando operaciones CRUD (alta, consulta, modificación y eliminación de registros) y un endpoint de healthcheck para monitoreo del servicio.

El proyecto incluyó la implementación de un pipeline completo de Integración Continua y Entrega Continua (CI/CD) mediante GitHub Actions y Render, siguiendo un flujo de trabajo basado en ramas, Pull Requests y despliegues controlados entre entornos.

## Principales características implementadas

- Desarrollo de endpoints REST para la gestión de clientes.
- Persistencia de datos mediante PostgreSQL y SQLAlchemy.
- Tests unitarios, de integración y seguridad utilizando Pytest.
- Análisis estático de seguridad mediante Bandit.
- Gestión segura de configuraciones y credenciales mediante variables de entorno y GitHub Secrets.
- Automatización de despliegues hacia entornos DEV y QA.
- Despliegue a Producción con aprobación manual previa.
- Uso de Git y GitHub bajo un flujo de trabajo basado en Pull Requests y validaciones automáticas.

## Tecnologías

Python, Flask, SQLAlchemy, PostgreSQL, Pytest, Bandit, GitHub Actions, Render, Git y GitHub.
