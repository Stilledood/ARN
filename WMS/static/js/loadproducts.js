const xhr = new XMLHttpRequest();
const method =  "GET";
const url = "/producatori/produse"
const responseType = "json";
const productELement = document.getElementById("produse")

// Functie de formatat un product output

function formatProductElement(produs, positionNumber){

    return `<tr>
    <th scope="row">${positionNumber+1}</th>
                <td>${produs.cod}</td>
                <td>${produs.nume}</td>
                <td>${produs.cantitate}</td>
                <td>${produs.raft}</td>
    </tr>`
    
    
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
        let displayProduct = formatProductElement(listedProducts[i],i);
        finalProductString += displayProduct;
    }

    productELement.innerHTML = finalProductString;

}

xhr.send();