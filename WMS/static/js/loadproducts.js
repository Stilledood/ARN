const xhr = new XMLHttpRequest();
const method =  "GET";
const url = "/producatori/produse"
const responseType = "json";
const productELement = document.getElementById("produse")

// Functie de formatat un product output

function formatProductElement(produs){
    return `<li class="list-group-item">${produs.nume}</li>`
}

xhr.responseType = responseType;
xhr.open(method,url);
xhr.onload = function(){
    const serverResponse = xhr.response;
    console.log(serverResponse.response);
    let listedProducts = serverResponse.response;
    console.log(listedProducts);
    let finalProductString = '';
    for (let i = 0; i < listedProducts.length; i++){
        let displayProduct = formatProductElement(listedProducts[i]);
        finalProductString += displayProduct;
    }

    productELement.innerHTML = finalProductString;

}

xhr.send();