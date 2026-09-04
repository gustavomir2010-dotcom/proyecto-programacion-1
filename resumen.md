INVESTIGACIÓN SOBRE GITHUB

GitHub es una plataforma que permite guardar proyectos y trabajar en equipo usando Git. Se utiliza una rama principal llamada `main` y ramas de trabajo como `feature/login` para desarrollar nuevas funciones sin afectar la rama principal.

El trabajo comienza con un **Issue**, donde se describe la tarea. Luego se crea una rama `feature/*`, se realizan los cambios y se guardan mediante **commits**. Con `git push` se suben los cambios a GitHub y con `git pull` se descargan los cambios del repositorio remoto.

Cuando la tarea termina, se crea un **Pull Request** hacia `main`. Otro compañero realiza un **Code Review** para revisar el código y, si todo está correcto, se realiza el **Merge**.

Un **Merge Conflict** ocurre cuando dos ramas modifican la misma parte de un archivo de forma diferente. Para solucionarlo se revisan los cambios, se elige la versión correcta y se realiza un nuevo commit.
# INVESTIGACIÓN SOBRE GITHUB

GitHub es una plataforma que permite guardar proyectos y trabajar en equipo usando Git.

- **Repositorio remoto:** Es el proyecto guardado en GitHub. Sirve para compartir y sincronizar el trabajo.
- **`main`:** Es la rama principal. Contiene la versión estable del proyecto.
- **`feature/*`:** Son ramas de trabajo. Sirven para crear nuevas funciones sin modificar directamente `main`.
- **Issues:** Son tareas o problemas registrados en GitHub. Sirven para organizar el trabajo.
- **Commits:** Son registros de cambios. Sirven para guardar y conocer qué modificaciones se hicieron.
- **Push:** Envía los cambios desde la computadora hacia GitHub.
- **Pull:** Descarga los cambios desde GitHub hacia la computadora.
- **Pull Request:** Es una solicitud para unir los cambios de una rama con `main`.
- **Code Review:** Es la revisión del código realizada por otro integrante antes de aceptar los cambios.
- **Merge:** Une los cambios de una rama con otra.
- **Merge Conflict:** Ocurre cuando dos ramas modifican la misma parte de un archivo de manera diferente. Se debe revisar y elegir qué cambios conservar.

### Flujo de trabajo

```text
Issue → Branch → Commit → Push → Pull Request → Code Review → Merge → main
