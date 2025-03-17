document.addEventListener("DOMContentLoaded", function () {
    // Exibe a primeira seção por padrão
    document.querySelector(".section").classList.add("active");

    // Captura todos os links do menu
    let links = document.querySelectorAll("nav ul li a, .btn-cadastrar");

    // Adiciona evento de clique para cada link
    links.forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault();

            // Pega o ID da seção correspondente
            let secao = this.getAttribute("href") ? this.getAttribute("href").substring(1) : "cadastro";

            // Esconde todas as seções
            document.querySelectorAll(".section").forEach(s => s.classList.remove("active"));

            // Exibe apenas a seção correspondente
            document.getElementById(secao).classList.add("active");
        });
    });

    // Esconde a mensagem após 3 segundos
    setTimeout(function() {
        let message = document.querySelector('.flash-message');
        if (message) {
            message.style.display = 'none';
        }
    }, 3000);
});