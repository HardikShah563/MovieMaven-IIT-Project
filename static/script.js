// let editVenue = document.querySelectorAll(".editVenue");
// let deleteVenue = document.querySelectorAll(".deleteVenue");
// let popupModal = document.querySelector(".popup-modal");
// editVenue.forEach(element => {
//     element.addEventListener("click", () => {
//         popupModal.classList.add("view-block");
//         console.log("Edit Venue been clicked");
//     })
// });

// deleteVenue.forEach(element => {
//     element.addEventListener("click", () => {
//         console.log("Delete Venue has been clicked");
//     })
// });

// let closeMark = document.querySelector(".closeMark");
// closeMark.addEventListener("click", () => {
//     popupModal.classList.remove("view-block");
// });

// ==========================
// COST CALCULATE FOR TICKETS
// ==========================

// Code for Ticket with cost 349
let plus1 = document.getElementById("plus1");
let minus1 = document.getElementById("minus1");

plus1.addEventListener("click", () => {
    document.getElementById("seats1").value = +(document.getElementById("seats1").value) + 1;
    document.getElementById("ticketCost-1").value = +(document.getElementById("ticketCost-1").value) + 349;
    document.getElementById("totAmount").value = +(document.getElementById("totAmount").value) + 349;
});
minus1.addEventListener("click", () => {
    if (+(document.getElementById("seats1").value) != 0) {
        document.getElementById("seats1").value = +(document.getElementById("seats1").value) - 1;
        document.getElementById("ticketCost-1").value = +(document.getElementById("ticketCost-1").value) - 349;
        document.getElementById("totAmount").value = +(document.getElementById("totAmount").value) - 349;
    }
});
// Code for Ticket with cost 199
let plus2 = document.getElementById("plus2");
let minus2 = document.getElementById("minus2");

plus2.addEventListener("click", () => {
    document.getElementById("seats2").value = +(document.getElementById("seats2").value) + 1;
    document.getElementById("ticketCost-2").value = +(document.getElementById("ticketCost-2").value) + 199;
    document.getElementById("totAmount").value = +(document.getElementById("totAmount").value) + 199;
});
minus2.addEventListener("click", () => {
    if (+(document.getElementById("seats2").value) != 0) {
        document.getElementById("seats2").value = +(document.getElementById("seats2").value) - 1;
        document.getElementById("ticketCost-2").value = +(document.getElementById("ticketCost-2").value) - 199;
        document.getElementById("totAmount").value = +(document.getElementById("totAmount").value) - 199;
    }
});
// Code for Ticket with cost 149
let plus3 = document.getElementById("plus3");
let minus3 = document.getElementById("minus3");

plus3.addEventListener("click", () => {
    document.getElementById("seats3").value = +(document.getElementById("seats3").value) + 1;
    document.getElementById("ticketCost-3").value = +(document.getElementById("ticketCost-3").value) + 149;
    document.getElementById("totAmount").value = +(document.getElementById("totAmount").value) + 149;
});
minus3.addEventListener("click", () => {
    if (+(document.getElementById("seats3").value) != 0) {
        document.getElementById("seats3").value = +(document.getElementById("seats3").value) - 1;
        document.getElementById("ticketCost-3").value = +(document.getElementById("ticketCost-3").value) - 149;
        document.getElementById("totAmount").value = +(document.getElementById("totAmount").value) - 149;
    }
});

// ==========================
// RATING SYSTEM
// ==========================
const btn = document.querySelector("button");
const post = document.querySelector(".post");
const widget = document.querySelector(".star-widget");
const editBtn = document.querySelector(".edit");
btn.onclick = () => {
    widget.style.display = "none";
    post.style.display = "block";
    editBtn.onclick = () => {
        widget.style.display = "block";
        post.style.display = "none";
    }
    return false;
}