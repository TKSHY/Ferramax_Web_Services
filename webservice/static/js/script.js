// Script para manejar el registro de usuarios
document.addEventListener("DOMContentLoaded", function () {
    const registerForm = document.getElementById("register-form");

    if (registerForm) {
        registerForm.addEventListener("submit", async function (e) {
            e.preventDefault();

            const data = {
                username: document.getElementById("username").value.trim(),
                email: document.getElementById("email").value.trim(),
                rut: document.getElementById("rut").value.trim(),
                phone: document.getElementById("phone").value.trim(),
                password: document.getElementById("password").value
            };

            console.log("Datos que se van a enviar:", data);

            try {
                const response = await fetch("/api/register/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": getCookie("csrftoken") // CSRF solo si es necesario
                    },
                    body: JSON.stringify(data)
                });

                const result = await response.json();

                console.log("Respuesta del servidor:", result);
                alert(result.message || result.error);

                if (response.status === 201) {
                    setTimeout(() => {
                        window.location.href = "/";
                    }, 2000);
                }

            } catch (err) {
                console.error("Error en la conexión con el servidor:", err);
                alert("Error de conexión con el servidor.");
            }
        });
    }

    // Función para obtener el token CSRF de las cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});


// Script para manejar el inicio de sesión con modal
function openLoginModal() {
    document.getElementById('loginModal').style.display = 'flex';
}

function closeLoginModal() {
    document.getElementById('loginModal').style.display = 'none';
    document.getElementById('loginMessage').innerText = '';
    document.getElementById('loginEmail').value = '';
    document.getElementById('loginPassword').value = '';
}

async function submitLogin() {
    const email = document.getElementById('loginEmail').value.trim();
    const password = document.getElementById('loginPassword').value;

    try {
        const response = await fetch('/api/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email, password }),
        });

        const data = await response.json();

        if (response.ok) {
            localStorage.setItem('username', data.username);
            const username = data.username || 'usuario';
            document.getElementById('loginMessage').style.color = 'green';
            document.getElementById('loginMessage').innerText = `Bienvenido, ${username}`;

            setTimeout(() => {
                closeLoginModal();
                location.reload(); // recargar para actualizar el estado si es necesario
            }, 2000);
        } else {
            document.getElementById('loginMessage').style.color = 'red';
            document.getElementById('loginMessage').innerText = data.error || 'Usuario o contraseña incorrectos';
        }
    } catch (error) {
        console.error("Error al iniciar sesión:", error);
        document.getElementById('loginMessage').style.color = 'red';
        document.getElementById('loginMessage').innerText = "Error de conexión con el servidor.";
    }
}
