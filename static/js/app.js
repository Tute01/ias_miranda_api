const tablaClientes = document.getElementById("tabla-clientes");

const formulario = document.getElementById("cliente-form");

const inputId = document.getElementById("cliente-id");
const inputNombre = document.getElementById("nombre");
const inputApellido = document.getElementById("apellido");
const inputEmail = document.getElementById("email");
const inputTelefono = document.getElementById("telefono");

const btnCancelar = document.getElementById("btn-cancelar");
const tituloFormulario = document.getElementById("titulo-formulario");

let clienteEditando = null;


async function cargarClientes() {

    const response = await fetch("/clientes");

    const clientes = await response.json();

    tablaClientes.innerHTML = "";

    clientes.forEach(cliente => {

        tablaClientes.innerHTML += `
            <tr>
                <td>${cliente.id}</td>
                <td>${cliente.nombre}</td>
                <td>${cliente.apellido}</td>
                <td>${cliente.email}</td>
                <td>${cliente.telefono || ""}</td>
                <td>
                    <button onclick="editarCliente(${cliente.id}, '${cliente.nombre}', '${cliente.apellido}', '${cliente.email}', '${cliente.telefono || ""}')">
                        Editar
                    </button>

                    <button onclick="eliminarCliente(${cliente.id})">
                        Eliminar
                    </button>
                </td>
            </tr>
        `;
    });
}


formulario.addEventListener("submit", async (e) => {

    e.preventDefault();

    const cliente = {
        nombre: inputNombre.value,
        apellido: inputApellido.value,
        email: inputEmail.value,
        telefono: inputTelefono.value
    };

    if (clienteEditando === null) {

        await fetch("/clientes", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(cliente)
        });

    } else {

        await fetch(`/clientes/${clienteEditando}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(cliente)
        });

    }

    limpiarFormulario();

    cargarClientes();
});


function editarCliente(id, nombre, apellido, email, telefono) {

    clienteEditando = id;

    tituloFormulario.textContent = "Editar Cliente";

    inputId.value = id;
    inputNombre.value = nombre;
    inputApellido.value = apellido;
    inputEmail.value = email;
    inputTelefono.value = telefono;
}


async function eliminarCliente(id) {

    const confirmar = confirm("¿Eliminar cliente?");

    if (!confirmar) return;

    await fetch(`/clientes/${id}`, {
        method: "DELETE"
    });

    cargarClientes();
}


btnCancelar.addEventListener("click", () => {

    limpiarFormulario();
});


function limpiarFormulario() {

    clienteEditando = null;

    tituloFormulario.textContent = "Alta de Cliente";

    formulario.reset();

    inputId.value = "";
}


cargarClientes();