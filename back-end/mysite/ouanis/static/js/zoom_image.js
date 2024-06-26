document.addEventListener("DOMContentLoaded", function() {
    var modal = document.createElement("div");
    modal.id = "myModal";
    modal.className = "modal";
    modal.innerHTML = `
        <span class="close">&times;</span>
        <img class="modal-content" id="img01">
    `;
    document.body.appendChild(modal);

    var modalImg = document.getElementById("img01");
    var images = document.querySelectorAll(".zoomable");
    images.forEach(function(image) {
        image.onclick = function() {
            modal.style.display = "block";
            modalImg.src = this.src;
        }
    });

    var span = document.getElementsByClassName("close")[0];
    span.onclick = function() {
        modal.style.display = "none";
    }

    modal.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});

// CSS for modal
const style = document.createElement('style');
style.innerHTML = `
    .modal {
        display: none;
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgb(0,0,0);
        background-color: rgba(0,0,0,0.4);
        padding-top: 60px;
    }
    .modal-content {
        margin: auto;
        display: block;
        width: 80%;
        max-width: 700px;
    }
    .close {
        position: absolute;
        top: 15px;
        right: 35px;
        color: #f1f1f1;
        font-size: 40px;
        font-weight: bold;
        transition: 0.3s;
    }
    .close:hover,
    .close:focus {
        color: #bbb;
        text-decoration: none;
        cursor: pointer;
    }
`;
document.head.appendChild(style);
