# Bot-de-Telegram-2

Este proyecto consiste en un bot básico para Telegram desarrollado en Python utilizando la librería TeleBot.

## Descripción

Este bot para Telegram ofrece entretenimiento a través de chistes y adivinanzas. Algunas de sus características incluyen:

Chistes: El bot cuenta con una lista de chistes cortos que pueden alegrar el día de los usuarios.

Adivinanzas: También tiene una colección de adivinanzas para desafiar la mente de los usuarios.

El objetivo principal de este bot es proporcionar diversión y entretenimiento a los usuarios de Telegram.

## Configuración

Sigue estos pasos para configurar y ejecutar el bot en tu entorno local:

1. **Clonar el Repositorio**: Utiliza Git para clonar este repositorio en tu máquina local utilizando el siguiente comando:

    ```bash
    git clone https://github.com/tu_usuario/Bot-de-Telegram-1.git
    ```

2. **Instalar Dependencias**: Navega al directorio del proyecto y utiliza pip para instalar las dependencias necesarias:

    ```bash
    cd Bot-de-Telegram-1
    pip install -r requirements.txt
    ```

3. **Obtener Token de Bot**: Crea un nuevo bot en Telegram utilizando el BotFather y obtén el token del bot recién creado.

4. **Configurar el Token**:
    - Crea un archivo `.env` en el directorio raíz del proyecto.
    - Abre el archivo `.env` en un editor de texto y agrega la siguiente línea, reemplazando `"TU_TOKEN_AQUÍ"` con el token obtenido en el paso anterior:

    ```plaintext
    TELEGRAM_TOKEN=TU_TOKEN_AQUÍ
    ```

5. **Asegurarse de que `.env` esté en `.gitignore`**:
    - Asegúrate de que el archivo `.env` esté incluido en `.gitignore` para que no se suba al repositorio. El contenido de `.gitignore` debería incluir `.env`:

    ```plaintext
    .env
    ```

6. **Ejecutar el Bot**: Ejecuta el script `main.py` utilizando Python para iniciar el bot:

    ```bash
    python main.py
    ```

## Funcionalidades

El bot actualmente cuenta con las siguientes funcionalidades:

- **Comando `/start`**: Inicia el bot y muestra un mensaje de bienvenida al usuario.

- **Comando `/help`**: Proporciona información sobre cómo utilizar el bot y las funcionalidades disponibles.

- **Comando `/about`**: Muestra información sobre el bot, incluyendo detalles sobre su propósito y quién lo creó.

- **Comando `/chiste`**: Cuenta un chiste corto de forma aleatoria para alegrar el día del usuario.

- **Comando `/adivinanza`**: Presenta una adivinanza corta de forma aleatoria para desafiar la mente del usuario.

## El bot en funcionamiento

![bot02](https://github.com/EduardoHernandezGuzman/Bot-de-Telegram-2-/assets/139759297/0cd7380d-10fa-419f-a29c-02cf0bf47add)



## Personalización

Si deseas agregar nuevas funcionalidades o personalizar el comportamiento del bot, puedes modificar el archivo `main.py` según tus necesidades. La documentación de TeleBot puede ser útil para comprender cómo extender la funcionalidad del bot.

## Autoría

Este proyecto fue desarrollado por [Eduardo Hernández Guzmán](https://github.com/EduardoHernandezGuzman). Puedes encontrar más proyectos interesantes en mi perfil de GitHub.
