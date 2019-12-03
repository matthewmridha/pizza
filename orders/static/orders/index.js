document.addEventListener("DOMContentLoaded", function() {
    if (localStorage.getItem("cart") === null) {
        localStorage.setItem("cart", [])
    } else(localStorage.getItem("cart"))
    localStorage.setItem("cart", JSON.stringify(
        [
            { product: "a", price: 1 },
            { product: "b", price: 2 }
        ]))
    let cart = JSON.parse(localStorage.getItem("cart"))
    cart.forEach(function(item) {
        console.log(item.product + ":" + item.price)
    })


});

let carItems = [];
let cartTotal = "";

function addPizzaR(item, price) {
    alert(item + price)
};

function addPizzaS(item, price) {
    alert(item + price)
};

function addToCart(item, price, addOn = null) {

    alert("item " + item + " price : " + price + addOn)
    let cart_list = document.getElementById('cart_list')
    cart_list.innerHTML += `<tr><td>${item}</td><td>${price}</td></tr>`;
    let total_price = document.getElementById("total_price");
    let total = total_price.innerHTML;
    let newTotal = eval(`${total} + ${price}`);
    total_price.innerHTML = newTotal
};

showCart = () => {
    console.log("show")
    let cart = document.getElementById("cart")

    if (cart.style.display == "block") {
        cart.style.display = "none"
    } else {
        cart.style.display = "block";
    }

}